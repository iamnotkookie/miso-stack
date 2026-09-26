#!/usr/bin/env python3
import json
from pathlib import Path

skill = Path(__file__).resolve().parents[1] / "skills/miso/SKILL.md"
context = (
    "MisoStack is available. For engineering requests, read " + str(skill)
    + " and select the matching workflow. Read the current harness map before delegation. "
    "Use the harness default model unless project configuration supplies one. "
    "Honor user instructions and approval boundaries. This reminder grants no permissions. "
    "For casual conversation or an explicit opt-out, do not route a workflow."
)
print(json.dumps({"hookSpecificOutput": {"hookEventName": "SessionStart", "additionalContext": context}}))
