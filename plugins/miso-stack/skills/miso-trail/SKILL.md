---
name: miso-trail
description: "Keeps a concise evidence-backed decision trail for long work. Use for unattended runs, migrations, or an auditable handoff."
license: MIT
---

# Decision trail

Apply the shared rules and current host map in [miso](../miso/SKILL.md). When called directly, run this procedure after reading those rules. When called from a playbook, continue that playbook without restarting routing.

Choose one project-local log path before starting. Keep private evidence local.

Use the bundled command:

```sh
python3 <plugin-root>/scripts/miso.py trail add .miso/trail.jsonl --decision "Use a single writer" --reason "Both workers modify the same state file" --evidence evidence/race.txt --result "The serial run preserved both records"
```

Record a decision when it changes scope, architecture, a hypothesis, or a verification result. Include what changed, why, evidence, and the observed result. Record rejected experiments too. Do not log every tool call or claim that a command ran without its output.

Use `trail show` to read the log. Audit a sample against files and runtime evidence before handing over. Keep the log out of commits unless requested or required by the project. A log records observations; it cannot enforce their truth.

Resolve `<plugin-root>` from this installed skill's real path: its grandparent contains `skills/` and `scripts/`. Resolve symlinks first. Never create a helper at a guessed path.
