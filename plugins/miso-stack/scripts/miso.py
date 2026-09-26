#!/usr/bin/env python3
import argparse
import json
import sys

import miso_evidence
import miso_package
import miso_plan


def parser():
    root = argparse.ArgumentParser(description="MisoStack local catalog, plan, evidence, and installation tools.")
    commands = root.add_subparsers(dest="command_name", required=True)
    for name, help_text in [("catalog", "List skills and workflow contracts."), ("check", "Validate the skill package."), ("doctor", "Check package and host binary availability.")]:
        commands.add_parser(name, help=help_text)
    install = commands.add_parser("links", help="Preview shared skill links; refuse collisions.")
    install.add_argument("--target", default="~/.agents/skills", help="Skill directory (default: ~/.agents/skills).")
    install.add_argument("--apply", action="store_true", help="Create missing links after collision checks.")
    plans = commands.add_parser("plan", help="Validate and track dependent tasks.").add_subparsers(dest="plan_command", required=True)
    for name in ["init", "check", "next", "start", "finish", "block", "retry"]:
        item = plans.add_parser(name)
        item.add_argument("path", help="Plan JSON file.")
        if name == "init":
            item.add_argument("--goal", required=True)
        if name in {"start", "finish", "block", "retry"}:
            item.add_argument("task", help="Task ID.")
        if name in {"start", "finish", "block"}:
            item.add_argument("--owner", required=True)
        if name == "finish":
            item.add_argument("--evidence", action="append", required=True, help="Proof path relative to the plan directory; repeatable.")
        if name in {"block", "retry"}:
            item.add_argument("--reason", required=True)
    receipt = commands.add_parser("record", help="Run an explicit command without a shell and save its evidence.")
    receipt.add_argument("--timeout", type=float, default=120, help="Seconds, at most 3600 (default: 120). Put before the path.")
    receipt.add_argument("path", help="New evidence JSON path; existing files are never replaced.")
    receipt.add_argument("command", nargs=argparse.REMAINDER, help="-- PROGRAM ARGUMENTS")
    logs = commands.add_parser("trail", help="Keep a decision log.").add_subparsers(dest="trail_command", required=True)
    for name in ["add", "show"]:
        item = logs.add_parser(name)
        item.add_argument("path")
        if name == "add":
            for field in ["decision", "reason", "evidence", "result"]:
                item.add_argument("--" + field, required=True)
    return root


def main():
    args = parser().parse_args()
    functions = {"catalog": lambda: miso_package.catalog(), "check": lambda: miso_package.check(),
                 "doctor": lambda: miso_package.doctor(), "links": lambda: miso_package.links(args),
                 "plan": lambda: miso_plan.run(args), "record": lambda: miso_evidence.record(args),
                 "trail": lambda: miso_evidence.trail(args)}
    try:
        print(json.dumps(functions[args.command_name](), indent=2))
    except (OSError, ValueError, KeyError, TypeError) as error:
        print(json.dumps({"error": str(error), "help": "Run the command with --help and correct the input or prerequisite."}), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
