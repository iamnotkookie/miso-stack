# Refactor safely

Use for: Change structure while preserving the agreed behavior.

You own the invariant. Behavior stays the same, and the proof is the same check passing before and after.

## Procedure

1. State the structural problem and the behavior that must not change. If no check covers that behavior, write one before you move anything.
2. Identify callers, persisted data, public contracts, and readers that a search can miss. Run the baseline checks and save the result.
3. Choose the smallest structural change. Remove dead weight first ([subtract-before-you-add](../references/principles/subtract-before-you-add.md)). Move callers with the contract and delete the old path in the same wave ([migrate-callers-then-delete-legacy-apis](../references/principles/migrate-callers-then-delete-legacy-apis.md)). Prefer a codemod over a run of hand edits ([build-the-lever](../references/principles/build-the-lever.md)).
4. Implement in units that stay runnable. Preserve unrelated changes and required compatibility.
5. Run the same baseline checks against the result and exercise representative user paths.
6. Inspect the final diff for hidden behavior changes. A behavior change belongs in a separate commit, with its own reason.

## Supporting skills

[miso-research](../../miso-research/SKILL.md), [miso-design](../../miso-design/SKILL.md), [miso-review](../../miso-review/SKILL.md), [miso-verify](../../miso-verify/SKILL.md)

## Completion evidence

The same observable contracts hold before and after the structural change.

## Reply

State the structural problem, what moved, and the invariant you proved. Show the baseline and final check results. Name any behavior that changed on purpose.
