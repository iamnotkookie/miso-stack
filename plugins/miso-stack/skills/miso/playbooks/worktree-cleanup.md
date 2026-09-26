# Audit local runtime leftovers

Use for: Inspect worktrees or simulator resources before approved cleanup.

## Procedure

1. Use read-only inventory commands to list resources, owners, activity, and uncommitted state.
2. Check whether branches are merged and whether another process or session uses the resource.
3. List exact cleanup candidates and the evidence that makes each safe. Uncertain ownership excludes a candidate.
4. Show the dry-run list and obtain approval for data deletion.
5. Recheck ownership and state immediately before any approved deletion. Use the platform's normal removal command with an explicit target.
6. Verify the remaining resources and keep the audit evidence. Never use broad recursive cleanup or remove another session's data.

## Supporting skills

[miso-research](../../miso-research/SKILL.md), [miso-review](../../miso-review/SKILL.md)

## Completion evidence

The candidate list is justified; any deletion has scoped approval and a verified outcome.
