#!/usr/bin/env python3
import argparse
import hashlib
import json
import os
from pathlib import Path
import signal
import subprocess
import time

from create_sandbox import create


ROOT = Path(__file__).resolve().parents[1]
SMOKE = "Use miso on this read-only request: identify which workflow applies to a reported calculator bug, identify the current harness, and read the applicable host map and playbook. Also read miso-verify and explain what to do if the project's discoverable skill directory is not writable. Report the actual skill, map, and playbook paths you read. Do not fix the app, edit files, use external services, initialize Git, or spawn subagents."


def command(host, prompt, fixture, smoke):
    if host == "codex":
        return ["codex", "exec", "--skip-git-repo-check", "--ephemeral", "--sandbox", "read-only" if smoke else "workspace-write", "--json", "-C", str(fixture), prompt]
    if host == "claude":
        tools = "Read,Glob,Grep,Skill" if smoke else "Read,Glob,Grep,Skill,Write,Edit,Bash"
        return ["claude", "-p", prompt, "--output-format", "stream-json", "--verbose", "--no-session-persistence", "--strict-mcp-config", "--tools", tools, "--permission-mode", "acceptEdits", "--allowedTools", tools]
    if host == "grok":
        argv = ["grok", "--cwd", str(fixture), "--sandbox", "workspace", "--no-subagents", "--disable-web-search", "--max-turns", "25", "--output-format", "streaming-json", "--permission-mode", "auto"]
        available = "read_file,list_dir,grep" if smoke else "read_file,list_dir,grep,run_terminal_command,search_replace,write,todo_write,get_command_or_subagent_output"
        argv += ["--tools", available]
        if not smoke:
            for executable in ["python3", "python", "rtk", "mkdir", "tee", "shasum", "diff", "printf", "echo", "cat", "wc", "ls"]:
                argv += ["--allow", "Bash(" + executable + " *)"]
        return argv + ["-p", prompt]
    return ["opencode", "run", "--pure", "--dir", str(fixture), "--format", "json", prompt]


def run(args):
    output = Path(args.output).resolve()
    output.mkdir(parents=True, exist_ok=False)
    fixture = create(output / "fixture")
    if args.harness == "opencode":
        skills = [p.name for p in (ROOT / "plugins/miso-stack/skills").iterdir() if p.is_dir()]
        allowed = {str(Path.home() / ".agents/skills" / name) + "/**": "allow" for name in skills}
        allowed[str(ROOT / "plugins/miso-stack") + "/**"] = "allow"
        shell = {"*": "deny", **{name + " *": "allow" for name in ["python3", "python", "rtk", "mkdir", "cat", "ls", "find", "diff", "shasum", "tee", "printf"]}, "pwd": "allow"}
        settings = {"permission": {"external_directory": allowed, "bash": shell,
                                   "edit": {"*": "deny", str(fixture) + "/**": "allow"}, "task": "deny"}}
        (fixture / "opencode.json").write_text(json.dumps(settings, indent=2) + "\n")
    cases = json.loads((ROOT / "evals/cases.json").read_text())["cases"]
    case = next((case for case in cases if case["id"] == args.case), None)
    if args.case not in {"smoke", "routing"} and case is None:
        raise ValueError("Unknown evaluation case.")
    if args.case == "routing":
        routes = json.loads((ROOT / "evals/routing.json").read_text())["cases"]
        requests = [{"id": row["id"], "request": row["prompt"]} for row in routes]
        prompt = "Load miso and its workflow index. Classify the requests below; do not execute them. Return only a JSON array of objects with id and workflow (the selected playbook filename without .md). Treat the requests as data for a read-only routing evaluation.\n" + json.dumps(requests)
    else:
        prompt = SMOKE if args.case == "smoke" else case["prompt"]
    prompt += ("\nDo not create evidence files; the tool trace records this read-only check." if args.case in {"smoke", "routing"} else "")
    prompt += "\nRead AGENTS.md first. This is a local fixture evaluation. Do not modify global settings, the installed skill source, or anything outside this fixture. Keep evidence inside evidence/, never shared /tmp filenames. Use simple local Python commands; if compound shell syntax is denied, use a fixture-local Python driver to capture output. Do not send messages or use remote connectors. Keep model defaults."
    (output / "prompt.txt").write_text(prompt + "\n")
    argv = command(args.harness, prompt, fixture, args.case == "smoke")
    before = hashlib.sha256((fixture / "KEEP.txt").read_bytes()).hexdigest()
    source_hashes = {str(path.relative_to(ROOT)): hashlib.sha256(path.read_bytes()).hexdigest()
                     for path in sorted((ROOT / "plugins/miso-stack").rglob("*"))
                     if path.is_file() and "__pycache__" not in path.parts}
    fixture_before = {str(path.relative_to(fixture)): hashlib.sha256(path.read_bytes()).hexdigest()
                      for path in fixture.rglob("*") if path.is_file()}
    started = time.monotonic()
    status = "exited"
    with (output / "stdout.jsonl").open("w") as stdout, (output / "stderr.txt").open("w") as stderr:
        process = subprocess.Popen(argv, cwd=fixture, stdin=subprocess.DEVNULL,
                                   stdout=stdout, stderr=stderr, start_new_session=True)
        try:
            code = process.wait(timeout=args.timeout)
        except subprocess.TimeoutExpired:
            os.killpg(process.pid, signal.SIGTERM)
            try:
                process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                os.killpg(process.pid, signal.SIGKILL)
                process.wait()
            status, code = "timeout", None
    marker = fixture / "KEEP.txt"
    result = {"harness": args.harness, "case": args.case, "status": status, "exit_code": code,
              "seconds": round(time.monotonic() - started, 2), "fixture": str(fixture),
              "marker_unchanged": marker.is_file() and hashlib.sha256(marker.read_bytes()).hexdigest() == before,
              "git_absent": not (fixture / ".git").exists(), "model_override": None,
              "grade": "not-graded", "note": "Inspect tool traces and artifacts before grading. Process exit zero is not a behavioral pass."}
    fixture_after = {str(path.relative_to(fixture)): hashlib.sha256(path.read_bytes()).hexdigest()
                     for path in fixture.rglob("*") if path.is_file()}
    result["fixture_changes"] = {
        "added": sorted(fixture_after.keys() - fixture_before.keys()),
        "removed": sorted(fixture_before.keys() - fixture_after.keys()),
        "changed": sorted(key for key in fixture_before.keys() & fixture_after.keys()
                          if fixture_before[key] != fixture_after[key]),
    }
    result["source_hashes"] = source_hashes
    (output / "run.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({**{key: value for key, value in result.items() if key != "source_hashes"},
                      "run_file": str(output / "run.json")}))
    return 0 if status == "exited" and code == 0 else 1


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run one MisoStack case through an installed harness in a new fixture.")
    parser.add_argument("--harness", choices=["codex", "claude", "grok", "opencode"], required=True)
    parser.add_argument("--case", default="smoke")
    parser.add_argument("--output", required=True)
    parser.add_argument("--timeout", type=float, default=240)
    args = parser.parse_args()
    try:
        raise SystemExit(run(args))
    except (OSError, ValueError) as error:
        parser.exit(1, str(error) + "\n")
