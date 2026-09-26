#!/usr/bin/env python3
import argparse
import json
from pathlib import Path
import urllib.request


ROOT = Path(__file__).resolve().parents[1]
API = "https://api.github.com/repos/cursor/plugins"


def fetch(url):
    request = urllib.request.Request(url, headers={"User-Agent": "MisoStack-reference-audit"})
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.load(response)


def live_inventory():
    commit = fetch(API + "/commits/main")
    tree = fetch(API + "/git/trees/" + commit["sha"] + "?recursive=1")
    if tree.get("truncated"):
        raise ValueError("GitHub truncated the inventory. Do not report complete coverage.")
    return {"sha": commit["sha"], "paths": [item["path"] for item in tree["tree"]
            if item["type"] == "blob" and item["path"].startswith("pstack/")]}


def compare(inventory):
    audit = json.loads((ROOT / "docs/reference-audit.json").read_text())
    paths = inventory.get("paths")
    if not isinstance(paths, list) or not all(isinstance(path, str) for path in paths):
        raise ValueError("Inventory paths must be a list of strings.")
    relevant = {path for path in paths if path.endswith("/SKILL.md") or "/playbooks/" in path and path.endswith(".md")}
    recorded = {row["source"] for row in audit["items"]}
    return {"reference_sha": audit["reference_sha"], "checked_sha": inventory.get("sha"),
            "new_capabilities": sorted(relevant - recorded), "removed_capabilities": sorted(recorded - relevant),
            "mapped": len(relevant & recorded), "note": "Inventory coverage is not behavioral qualification. Read changed content when the revision changes."}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Compare a public pstack inventory with MisoStack's recorded capability map.")
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--inventory", help="Local JSON with sha and paths fields.")
    source.add_argument("--live", action="store_true", help="Read the public GitHub API; no repository or user data is uploaded.")
    args = parser.parse_args()
    try:
        inventory = live_inventory() if args.live else json.loads(Path(args.inventory).read_text())
        result = compare(inventory)
        print(json.dumps(result, indent=2))
        raise SystemExit(1 if result["new_capabilities"] else 0)
    except (OSError, ValueError, KeyError, TypeError) as error:
        parser.exit(1, str(error) + "\n")
