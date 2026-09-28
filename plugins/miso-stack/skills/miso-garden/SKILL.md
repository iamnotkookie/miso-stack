---
name: miso-garden
description: "Maintains codebase structure and turns recurring defects into enforced constraints. Use for codebase gardening, repeated helpers, growing suppressions, architecture drift, or installing anti-slop checks."
license: MIT
---

# Tend the codebase

Apply the shared rules and current host map in [miso](../miso/SKILL.md). Use this for maintenance across changes; use a normal review for one diff.

## Inspect

Read project boundaries, compiler and lint settings, existing checks, and a bounded set of recent changes. Use a requested commit range or PR set. Without remote access, use local history and say what was unavailable. Read-only monitoring does not authorize PR comments or fixes.

Look for repeated decisions, duplicate business rules, duplicate boundary parsers, forwarding layers, new suppressions, casts that escape types, imports that violate ownership, and repeated allocation or query work. Judge duplication with [structure](../miso/references/principles.md): one rule, one place. Similar names are not proof of one abstraction. Trace representative callers before grouping findings. Similar names or three matching snippets are leads, not proof that one abstraction belongs everywhere. A repeated missing authorization check, secret in the tree, or injection sink becomes an enforced check. A full audit is [miso-audit](../miso-audit/SKILL.md).

For each confirmed pattern, record its locations, consequence, owner, and smallest useful repair. Distinguish domain differences from accidental duplication. Prioritize a recurring failure with a reproducible example over a broad style rewrite. If nothing warrants change, report that result.

## Enforce

For requested cleanup, use [enforced architecture](references/constraints.md). Repair one coherent boundary and encode the rule where contributors already receive feedback. Prefer types, schemas, compiler diagnostics, import checks, or a focused lint rule over another instruction in AGENTS.md.

Run the existing baseline first. Demonstrate that the new check rejects an actual violation and accepts a valid example. Repair the authorized callers, run the relevant checks, and prove caller behavior still works. Keep existing failures visible. Do not make a gate pass by deleting tests, widening ignores, adding casts, or suppressing diagnostics.

For an explicit anti-slop installation or update, read [lint setup](references/lint-setup.md). Ordinary gardening should reuse the project's tools, not replace its stack or install a new linter by default.

Deliver the observed pattern, completed repair, enforced rule, executed proof, and remaining findings. For recurring PR monitoring, prove a manual pass first, then use [miso-automate](../miso-automate/SKILL.md) for an authorized schedule with a watermark, duplicate handling, owner, limits, and disable path. Report inactive automation honestly.
