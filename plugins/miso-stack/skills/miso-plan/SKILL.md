---
name: miso-plan
description: "Creates and runs dependency-aware plans with proof for each task. Use for multi-phase work, migrations, orchestration, or a task that has no existing playbook."
license: MIT
---

# Plan and execute

Apply the shared rules and current host map in [miso](../miso/SKILL.md). When called directly, run this procedure after reading those rules. When called from a playbook, continue that playbook without restarting routing.

1. State an observable final result. Ground the scope in current files and runtime evidence. Resolve the highest-risk unknown with an experiment before expanding the plan.
2. Break work into small units. Each task needs an ID, outcome, dependencies, owner, verification method, and evidence. Define review or external-action gates explicitly.
3. Use the bundled plan format and CLI described in [the plan contract](../miso/references/plan.md). Run `plan check` before execution. A cycle or missing dependency blocks the plan.
4. Use `plan next` to find ready work. Claim a task with `plan start`. Give one owner each mutable artifact. Delegation follows the host map and [delegation](../miso/references/delegation.md).
5. Implement one unit, run its verification, and save evidence before `plan finish`. The CLI records an artifact hash; the lead still judges whether the artifact proves the task.
6. Record blockers and experiments in the trail. Continue independent ready work when one task is blocked. Do not repeatedly retry the same failure without new evidence.
7. Verify the whole result after its parts pass. A plan with all tasks done is not a substitute for integration proof. Keep a resumable handoff if the environment prevents completion.

The CLI is a local task ledger, not a worker scheduler. Host tools execute tasks. Plans stay local unless the user requests publication or project rules require it.

Resolve `<plugin-root>` from this installed skill's real path: its grandparent contains `skills/` and `scripts/`. Resolve symlinks first. Never create a helper at a guessed path.
