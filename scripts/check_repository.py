#!/usr/bin/env python3
import ast
import json
import os
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
EXCLUDED = {".git", "evidence", ".miso", ".venv", "venv", "__pycache__", "sandbox", "sandboxes", "runs"}
MANIFESTS = ["plugins/miso-stack/.claude-plugin/plugin.json", "plugins/miso-stack/.codex-plugin/plugin.json",
             "plugins/miso-stack/.grok-plugin/plugin.json"]
MARKETPLACES = [".claude-plugin/marketplace.json", ".grok-plugin/marketplace.json"]


def source_files():
    for folder, directories, files in os.walk(ROOT):
        directories[:] = [name for name in directories if name not in EXCLUDED]
        for name in files:
            yield Path(folder) / name


def version_failures():
    """package.json owns the version. Hosts use manifest versions to decide when to refresh a plugin."""
    owner = json.loads((ROOT / "package.json").read_text())["version"]
    found = {name: json.loads((ROOT / name).read_text())["version"] for name in MANIFESTS}
    found |= {name: json.loads((ROOT / name).read_text())["plugins"][0]["version"] for name in MARKETPLACES}
    return [f"{name}: version {version} differs from package.json {owner}"
            for name, version in found.items() if version != owner]


def check():
    failures = version_failures()
    paths = list(source_files())
    for path in (p for p in paths if p.suffix == ".py"):
        ast.parse(path.read_text(), filename=str(path))
    for path in (p for p in paths if p.suffix == ".json"):
        json.loads(path.read_text())
    for path in (p for p in paths if p.suffix == ".md"):
        for link in re.findall(r"\]\(([^)]+)\)", path.read_text()):
            if re.match(r"[a-z]+://", link) or link.startswith("#"):
                continue
            destination = (path.parent / link.split("#")[0]).resolve()
            if not destination.exists():
                failures.append(f"{path.relative_to(ROOT)}: broken link {link}")
    print(json.dumps({"valid": not failures, "errors": failures}, indent=2))
    return bool(failures)


if __name__ == "__main__":
    raise SystemExit(check())
