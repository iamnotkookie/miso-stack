import json
from pathlib import Path
import re
import shutil

from miso_io import lock, read_json, require


ROOT = Path(__file__).resolve().parents[1]
HOSTS = ("codex", "claude", "grok", "opencode")


def catalog():
    return read_json(ROOT / "catalog.json")


def links(args):
    target = Path(args.target).expanduser().absolute()
    sources = sorted((ROOT / "skills").iterdir())
    items = []
    for source in sources:
        dest = target / source.name
        same = dest.is_symlink() and dest.resolve() == source.resolve()
        exists = dest.exists() or dest.is_symlink()
        status = "linked" if same else "collision" if exists else "missing"
        items.append({"name": source.name, "source": str(source), "target": str(dest), "status": status})
    collisions = [item["name"] for item in items if item["status"] == "collision"]
    require(not collisions, "Existing skills would be replaced: " + ", ".join(collisions) + ". Nothing was changed.")
    if args.apply:
        target.mkdir(parents=True, exist_ok=True)
        with lock(target / ".miso-install"):
            for item in items:
                dest = Path(item["target"])
                require(not dest.exists() or (dest.is_symlink() and dest.resolve() == Path(item["source"])), "Installation target changed. Retry the dry run.")
            for item in items:
                if item["status"] == "missing":
                    Path(item["target"]).symlink_to(item["source"], target_is_directory=True)
    result = [{**item, "status": "linked"} for item in items] if args.apply else items
    return {"applied": args.apply, "skills": result}


def check():
    data = catalog()
    errors = []
    skills = data["skills"]
    names = {item["name"] for item in skills}
    if len(names) != len(skills):
        errors.append("Duplicate skill name in catalog.")
    discovered = {p.parent.name for p in (ROOT / "skills").glob("*/SKILL.md")}
    if names != discovered:
        errors.append("Skill inventory does not match catalog.")
    routing = data.get("routing", {})
    routing_path = ROOT / routing.get("path", "")
    if routing.get("entry") != data.get("entry") or not routing_path.is_file():
        errors.append("Missing or invalid entry router.")
    else:
        destinations = {(routing_path.parent / link).resolve()
                        for link in re.findall(r"\]\(([^)#]+)\)", routing_path.read_text())}
        required = {(ROOT / item["path"]).resolve() for item in skills if item["name"] != data["entry"]}
        if not required <= destinations:
            errors.append("Entry router does not reach every supporting skill.")
    for item in skills:
        path = ROOT / item["path"]
        content = path.read_text()
        match = re.match(r"---\nname: ([a-z0-9-]+)\ndescription: (.+)\nlicense: MIT\n---\n", content)
        if not match or match[1] != item["name"]:
            errors.append(f"Invalid frontmatter: {path}")
        elif json.loads(match[2]) != item["description"]:
            errors.append(f"Stale description in catalog: {path}")
        if len(content.splitlines()) >= 100:
            errors.append(f"Skill needs a reference split: {path}")
        if not 1 <= len(item["description"]) <= 1024:
            errors.append(f"Invalid description length: {path}")
    for workflow in data["workflows"]:
        if not (ROOT / workflow["path"]).is_file():
            errors.append("Missing workflow: " + workflow["id"])
        if not set(workflow["skills"]) <= names:
            errors.append("Unknown supporting skill: " + workflow["id"])
    for path in (ROOT / "skills").rglob("*.md"):
        for link in re.findall(r"\]\(([^)]+)\)", path.read_text()):
            if re.match(r"[a-z]+://", link) or link.startswith("#"):
                continue
            dest = (path.parent / link.split("#")[0]).resolve()
            if not dest.is_relative_to(ROOT) or not dest.exists():
                errors.append(f"Broken or escaping link in {path.relative_to(ROOT)}: {link}")
    require(not errors, "Package check failed:\n" + "\n".join(errors))
    return {"valid": True, "skills": len(skills), "workflows": len(data["workflows"])}


def doctor():
    return {"package": check(), "python_requirement": "3.10+", "hosts": {host: shutil.which(host) for host in HOSTS},
            "runtime_verified": False, "note": "Binary presence does not prove login, skill loading, routing, or delegation."}
