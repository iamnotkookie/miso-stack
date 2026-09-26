# Coordinate a multi-phase program

Use for: Own dependent tasks across sessions or workers.

## Procedure

1. Create a plan with explicit task dependencies, owners, gates, and evidence requirements.
2. Partition by stable boundaries and assign separate mutable outputs.
3. Dispatch only ready tasks through available host tools. The plan CLI records state but does not run workers.
4. Verify returned artifacts before accepting completion. Release dependent tasks only after proof.
5. Resolve integration conflicts and rerun combined checks. Track every worker until completion or cancellation.
6. Checkpoint plan state and evidence for session pickup. Report real coverage and unresolved gates.

## Supporting skills

[miso-plan](../../miso-plan/SKILL.md), [miso-swarm](../../miso-swarm/SKILL.md), [miso-trail](../../miso-trail/SKILL.md), [miso-review](../../miso-review/SKILL.md)

## Completion evidence

Task ownership and dependency order are valid, and integrated artifacts pass their declared checks.
