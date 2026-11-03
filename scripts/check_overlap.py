#!/usr/bin/env python3
"""Report skill lines that share a word sequence with an upstream tree, to keep prose original."""
import argparse
from pathlib import Path
import re
import subprocess


ROOT = Path(__file__).resolve().parents[1]
SKILLS = "plugins/miso-stack/skills"


def grams(text, size):
    words = re.findall(r"[a-z0-9']+", text.lower())
    return {" ".join(words[index:index + size]) for index in range(len(words) - size + 1)}


def check(upstream, base, size):
    known = set()
    for path in Path(upstream).rglob("*.md"):
        known |= grams(path.read_text(errors="ignore"), size)
    if base:
        text = subprocess.run(["git", "-C", str(ROOT), "grep", "-h", "", base, "--", SKILLS],
                              capture_output=True, text=True, check=True).stdout
        known -= grams(text, size)
    hits = []
    for path in sorted((ROOT / SKILLS).rglob("*.md")):
        for number, line in enumerate(path.read_text().splitlines(), 1):
            shared = sorted(grams(line, size) & known)
            if shared:
                hits.append({"file": str(path.relative_to(ROOT)), "line": number, "shared": shared[0]})
    return hits


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Find skill prose that repeats an upstream tree. Exit 1 on a match.")
    parser.add_argument("upstream", help="Directory of the design reference, such as a pstack checkout.")
    parser.add_argument("--base", help="Ignore sequences already present at this Git revision.")
    parser.add_argument("--size", type=int, default=6, help="Words in a sequence (default: 6).")
    args = parser.parse_args()
    found = check(args.upstream, args.base, args.size)
    for hit in found:
        print(f"{hit['file']}:{hit['line']}: {hit['shared']}")
    raise SystemExit(1 if found else 0)
