from pathlib import Path
import re

from miso_io import create_json, evidence, lock, now, read_json, replace_json, require, text


STATES = {"pending", "running", "blocked", "done"}
TASK_KEYS = {"id", "outcome", "depends_on", "verification", "status", "owner", "evidence"}


def validate_task(task):
    require(isinstance(task, dict), "Each task must be an object.")
    require(TASK_KEYS <= task.keys(), "Task fields missing: " + ", ".join(sorted(TASK_KEYS - task.keys())))
    require(not (task.keys() - TASK_KEYS - {"note", "updated_at"}), "Unknown task fields.")
    require(isinstance(task["id"], str) and re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", task["id"]), "Invalid task ID.")
    for field in ["outcome", "verification"]:
        text(task[field], field)
    require(isinstance(task["status"], str) and task["status"] in STATES, "Invalid task status.")
    dependencies = task["depends_on"]
    require(isinstance(dependencies, list) and all(isinstance(d, str) for d in dependencies), "Dependencies must be a list of IDs.")
    require(len(dependencies) == len(set(dependencies)), "Duplicate dependency.")
    require(task["owner"] is None or isinstance(task["owner"], str), "Owner must be text or null.")
    if task["status"] != "pending":
        text(task["owner"], "owner")
    require(isinstance(task["evidence"], list), "Evidence must be a list.")
    if task["status"] == "done":
        require(task["evidence"], "Completed tasks need evidence.")
    else:
        require(not task["evidence"], "Only completed tasks may have accepted evidence.")


def validate(data, base):
    require(isinstance(data, dict), "Plan must be an object.")
    require(set(data) == {"version", "goal", "tasks"}, "Plan needs exactly version, goal, and tasks.")
    require(type(data["version"]) is int and data["version"] == 1, "Unsupported plan version.")
    text(data["goal"], "goal")
    require(isinstance(data["tasks"], list) and 0 < len(data["tasks"]) <= 1000, "Plan needs 1 to 1000 tasks.")
    for task in data["tasks"]:
        validate_task(task)
    tasks = {task["id"]: task for task in data["tasks"]}
    require(len(tasks) == len(data["tasks"]), "Duplicate task ID.")
    for task in tasks.values():
        for dependency in task["depends_on"]:
            require(dependency in tasks, f"Unknown dependency: {dependency}")
            if task["status"] in {"running", "done"}:
                require(tasks[dependency]["status"] == "done", "Active and completed tasks need completed dependencies.")
        for proof in task["evidence"]:
            require(isinstance(proof, dict) and set(proof) == {"path", "sha256"}, "Invalid evidence record.")
            require(evidence(base, proof["path"]) == proof, "Evidence changed after acceptance: " + proof["path"])
    remaining = set(tasks)
    visited = set()
    while remaining:
        ready = {key for key in remaining if set(tasks[key]["depends_on"]) <= visited}
        require(ready, "Dependency cycle detected.")
        visited |= ready
        remaining -= ready
    return tasks


def initial(goal):
    return {"version": 1, "goal": text(goal, "goal"), "tasks": [{
        "id": "first-proof", "outcome": goal, "depends_on": [],
        "verification": "Replace this instruction with the concrete acceptance check before starting.",
        "status": "pending", "owner": None, "evidence": [],
    }]}


def transition(task, tasks, args, base):
    command = args.plan_command
    if command == "start":
        require(task["status"] == "pending", "Task is not pending. Check its current owner and status.")
        require(all(tasks[d]["status"] == "done" for d in task["depends_on"]), "Dependencies are incomplete.")
        require(not task["verification"].startswith("Replace this instruction"), "Set a concrete acceptance check before starting.")
        return {**task, "status": "running", "owner": text(args.owner, "owner"), "updated_at": now()}
    if command == "retry":
        require(task["status"] == "blocked", "Only a blocked task can be retried.")
        return {**task, "status": "pending", "owner": None, "note": text(args.reason, "reason"), "updated_at": now()}
    require(task["status"] == "running", "Only a running task can finish or block.")
    require(task["owner"] == args.owner, "Owner mismatch. The current owner must update this task.")
    if command == "block":
        return {**task, "status": "blocked", "note": text(args.reason, "reason"), "updated_at": now()}
    proofs = [evidence(base, name) for name in args.evidence]
    require(proofs, "Attach evidence before completing a task.")
    return {**task, "status": "done", "evidence": proofs, "updated_at": now()}


def run(args):
    path = Path(args.path)
    if args.plan_command == "init":
        create_json(path, initial(args.goal))
        return {"created": str(path), "next": "Edit tasks and verification methods, then run plan check."}
    if args.plan_command in {"check", "next"}:
        data = read_json(path)
        tasks = validate(data, path.parent)
        if args.plan_command == "check":
            return {"valid": True, "tasks": len(tasks), "complete": all(t["status"] == "done" for t in tasks.values())}
        ready = [t for t in tasks.values() if t["status"] == "pending" and all(tasks[d]["status"] == "done" for d in t["depends_on"])]
        return {"ready": ready, "blocked": [t["id"] for t in tasks.values() if t["status"] == "blocked"]}
    with lock(path):
        data = read_json(path)
        tasks = validate(data, path.parent)
        require(args.task in tasks, "Unknown task ID: " + args.task)
        changed = transition(tasks[args.task], tasks, args, path.parent)
        result = {**data, "tasks": [changed if t["id"] == args.task else t for t in data["tasks"]]}
        validate(result, path.parent)
        replace_json(path, result)
    return {"task": changed}
