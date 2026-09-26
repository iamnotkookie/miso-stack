#!/usr/bin/env python3
import ast
import json
import os
from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins/miso-stack"
EXCLUDED = {".git", "evidence", ".miso", ".venv", "venv", "__pycache__", "sandbox", "sandboxes", "runs"}


def source_files():
    for folder, directories, files in os.walk(ROOT):
        directories[:] = [name for name in directories if name not in EXCLUDED]
        for name in files:
            yield Path(folder) / name


def check():
    failures = []
    paths = list(source_files())
    for path in (p for p in paths if p.suffix == ".py"):
        ast.parse(path.read_text(), filename=str(path))
    for path in (p for p in paths if p.suffix == ".json"):
        json.loads(path.read_text())
    for path in (p for p in paths if p.suffix == ".md"):
        if path.name == "HANDOFF.md":
            continue
        for link in re.findall(r"\]\(([^)]+)\)", path.read_text()):
            if re.match(r"[a-z]+://", link) or link.startswith("#"):
                continue
            destination = (path.parent / link.split("#")[0]).resolve()
            if not destination.exists():
                failures.append(f"{path.relative_to(ROOT)}: broken link {link}")
    audit = json.loads((ROOT / "docs/reference-audit.json").read_text())
    sources = [item["source"] for item in audit["items"]]
    if len(set(sources)) != len(sources):
        failures.append("Duplicate reference mapping.")
    for item in audit["items"]:
        if item["status"] == "implemented" and not (PLUGIN / item["target"]).is_file():
            failures.append("Missing mapped capability: " + item["source"])
        if item["status"] not in {"implemented", "out-of-scope"}:
            failures.append("Unresolved capability: " + item["source"])
    print(json.dumps({"valid": not failures, "reference_items": len(sources), "errors": failures}, indent=2))
    return bool(failures)


if __name__ == "__main__":
    raise SystemExit(check())
