---
name: miso-swarm
description: "Coordinates bounded independent work and verifies returned artifacts. Use when parallel research, coverage partitions, or candidate races are requested."
license: MIT
---

# Swarm

Apply the shared rules and current host map in [miso](../miso/SKILL.md). When called directly, run this procedure after reading those rules. When called from a playbook, continue that playbook without restarting routing.

Read [delegation](../miso/references/delegation.md) first. A named team and a swarm are this procedure. The task ledger, when the work has dependencies, is [miso-plan](../miso-plan/SKILL.md). The writer of a unit does not approve it.

1. State the coverage set, completion condition, and worker limit. Choose partitioned coverage or a race on the same task. Define whether a race stops at the first verified pass or ranks all results.
2. Give each worker an owner ID, narrow scope, input revision, output path, required proof, and stop condition. Only one writer owns a file or app session at a time.
3. Launch no more workers than the harness permits. Track pending, running, completed, failed, and cancelled work. A missing worker API means serial coverage with that limitation reported.
4. Collect every result. Check the cited files and rerun important proofs. A worker's success sentence is not evidence. Retry only with a changed hypothesis or corrected input.
5. Combine compatible results. Verify the integrated artifact. Drain or cancel owned workers before finishing; do not leave background work unaccounted for.

Return completed coverage, evidence, failures, omissions, and actual model use. For persistent dependencies, use [miso-plan](../miso-plan/SKILL.md).
