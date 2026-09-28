---
name: miso-setup
description: "Checks MisoStack discovery and host capabilities without choosing fixed models. Use when installing MisoStack, diagnosing skill loading, or configuring a project."
license: MIT
---

# Setup

Apply the shared rules and current host map in [miso](../miso/SKILL.md). When called directly, run this procedure after reading those rules. When called from a playbook, continue that playbook without restarting routing.

1. Identify the host and read its map in [miso](../miso/SKILL.md). Inspect available commands before using them.
2. Run the bundled CLI: `python3 <plugin-root>/scripts/miso.py doctor`. This checks files and binaries, not account access or runtime behavior.
3. Use the shared tree for OpenCode and Grok Build. Inspect `links` in dry-run mode before `links --apply`. Never replace an existing skill with a different target.
4. Use the local marketplace for Claude Code and Codex. Follow the repository installation guide. Start a fresh session after installing.
5. Check whether project instructions already define models. Follow supported settings. Otherwise omit model overrides. Do not change the user's global model preference.
6. Invoke `miso` on a bounded read-only task. Confirm the matching playbook and host map were read. Confirm a startup hook separately where supported and trusted.
7. Report discovery, load, routing, and delegation as separate observations. An installed manifest is not proof of any of them. Before relying on a third-party skill, audit it with [miso-audit](../miso-audit/SKILL.md).

If a host requires hook trust, leave that choice to its user interface. Explicit skill invocation remains available without the hook.

Resolve `<plugin-root>` from this installed skill's real path: its grandparent contains `skills/` and `scripts/`. Resolve symlinks first. Never create a helper at a guessed path.
