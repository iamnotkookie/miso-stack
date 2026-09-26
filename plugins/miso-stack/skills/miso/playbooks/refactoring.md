# Refactor safely

Use for: Change structure while preserving the agreed behavior.

## Procedure

1. State the structural problem and the behavior that must remain unchanged.
2. Identify callers, persisted data, public contracts, and the baseline checks.
3. Choose the smallest structural change. Move callers with the contract instead of leaving accidental parallel APIs.
4. Implement in units that remain runnable. Preserve unrelated changes and required compatibility.
5. Run baseline checks against the result and exercise representative user paths.
6. Inspect the final diff for hidden behavior changes. Update ownership documentation where needed.

## Supporting skills

[miso-research](../../miso-research/SKILL.md), [miso-design](../../miso-design/SKILL.md), [miso-review](../../miso-review/SKILL.md), [miso-verify](../../miso-verify/SKILL.md)

## Completion evidence

The same observable contracts hold before and after the structural change.
