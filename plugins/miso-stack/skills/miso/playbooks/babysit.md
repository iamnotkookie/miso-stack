# Bring a PR to review readiness

Use for: Resolve CI failures, review findings, or conflicts on an existing PR.

## Procedure

1. Read the PR, current head revision, check results, and unresolved reviews through the project's approved tools.
2. Classify each finding as a real defect, unsupported claim, or missing context.
3. Repair accepted findings locally and resolve conflicts against current branches without discarding others' work.
4. Run the relevant checks. Re-read the PR head before relying on earlier CI results.
5. Draft replies with evidence. Send them only when communication is authorized.
6. Stop when the declared readiness condition is met or a human-owned gate remains. Use bounded polling with a deadline, not an endless watch.

## Supporting skills

[miso-research](../../miso-research/SKILL.md), [miso-review](../../miso-review/SKILL.md), [miso-verify](../../miso-verify/SKILL.md)

## Completion evidence

Readiness is established for the current PR revision; merge remains a separate action.
