---
name: miso-review
description: "Reviews correctness, security, change impact, and code quality against evidence. Use for code review, adversarial review, blast-radius analysis, or final quality checks."
license: MIT
---

# Review

Apply the shared rules and current host map in [miso](../miso/SKILL.md). When called directly, run this procedure after reading those rules. When called from a playbook, continue that playbook without restarting routing.

1. Fix the scope to a revision or explicit file set. Read the intended behavior and repository rules before the diff.
2. Trace changed contracts beyond direct callers. Include serialization, data migrations, configuration, permissions, background tasks, teardown, and old consumers when relevant.
3. Identify the assumption on which safety depends. Try to falsify it with the real code. Distinguish a proven defect from an untested hypothesis.
4. Inspect input validation, authorization, secret handling, error exposure, injection risks, and destructive operations. Use existing scanners where available. Report tools that could not run.
5. Check unnecessary layers, dead code, hidden mutation, duplicated state, misleading comments, and suppressed checks. Keep comments that explain a real constraint the code cannot express. Do not delete license notices.
6. For TypeScript, read [type review](../miso/references/typescript.md). For broad changes, partition review lenses with [swarm](../miso-swarm/SKILL.md) if permitted. Reviewers inspect independently; the lead validates findings.
7. Fix accepted findings within scope and rerun affected checks. Do not change expected results just to make a failing test pass.

Report actionable findings first. Each needs severity, a concrete trigger, impact, source location, and evidence or an explicit uncertainty label. State what was reviewed and what was not. No findings is a result, not proof of perfection.
