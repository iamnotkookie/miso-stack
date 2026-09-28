# Skill and workflow catalog

Start with `miso` and describe the task. [The router](../../plugins/miso-stack/skills/miso/references/routing.md) covers every supporting skill. Call a supporting skill directly when you need only that capability. All skills follow the same model, writing, and authority rules.

## Skills

| Skill | Purpose |
| --- | --- |
| [miso](../../plugins/miso-stack/skills/miso/SKILL.md) | Routes plain-language engineering requests to MisoStack skills and workflows. Use miso to investigate, design, specify, build, review, verify, or explain work without remembering sub-skill names. |
| [miso-audit](../../plugins/miso-stack/skills/miso-audit/SKILL.md) | Audits authorized source or a skill for security defects and confirms findings independently. Use for a repository security audit or for checking a skill before install. |
| [miso-author](../../plugins/miso-stack/skills/miso-author/SKILL.md) | Creates or improves compact skills from stated requirements and evaluated examples. Use for skill authoring or capturing an explicitly stated working preference. |
| [miso-automate](../../plugins/miso-stack/skills/miso-automate/SKILL.md) | Designs bounded engineering routines and handles issue reports with reproduction evidence. Use when drafting a recurring check, triaging a report, or automating a proven workflow. |
| [miso-debug](../../plugins/miso-stack/skills/miso-debug/SKILL.md) | Diagnoses bugs and performance regressions with a reproducible failure and controlled experiments. Use for broken, intermittent, or unexpectedly slow behavior. |
| [miso-design](../../plugins/miso-stack/skills/miso-design/SKILL.md) | Designs interfaces from usage and tests architectural choices with prototypes. Use when creating a subsystem, changing ownership, or comparing substantial designs. |
| [miso-docs](../../plugins/miso-stack/skills/miso-docs/SKILL.md) | Writes and verifies technical documentation in Simplified Technical English. Use for tutorials, how-to guides, references, explanations, READMEs, or documentation reviews. |
| [miso-eval](../../plugins/miso-stack/skills/miso-eval/SKILL.md) | Evaluates skill behavior with sandbox tasks and explicit grading criteria. Use when testing prompts, skill changes, routing, or harness compatibility. |
| [miso-garden](../../plugins/miso-stack/skills/miso-garden/SKILL.md) | Maintains codebase structure and turns recurring defects into enforced constraints. Use for codebase gardening, repeated helpers, growing suppressions, architecture drift, or installing anti-slop checks. |
| [miso-loop](../../plugins/miso-stack/skills/miso-loop/SKILL.md) | Repeats a scoped task with verification until it succeeds or reaches a stop condition. Use for a bounded build-test-fix loop, a Ralph-style loop, or resuming and cancelling repeated work. |
| [miso-merge](../../plugins/miso-stack/skills/miso-merge/SKILL.md) | Resolves an existing Git merge or rebase conflict by preserving the intent of both changes. Use for conflicted files or a stopped merge/rebase, not to start a new merge or publish code. |
| [miso-perf](../../plugins/miso-stack/skills/miso-perf/SKILL.md) | Measures and improves latency, throughput, memory, or startup behavior. Use for performance improvements, profiling, benchmark design, or repeated optimization experiments. |
| [miso-plan](../../plugins/miso-stack/skills/miso-plan/SKILL.md) | Creates and runs dependency-aware plans with proof for each task. Use for multi-phase work, migrations, orchestration, or a task that has no existing playbook. |
| [miso-reflect](../../plugins/miso-stack/skills/miso-reflect/SKILL.md) | Turns observed workflow failures into targeted improvements. Use when the user asks to reflect, review a session, or improve an existing skill. |
| [miso-research](../../plugins/miso-stack/skills/miso-research/SKILL.md) | Traces behavior, decision history, and relevant prior work. Use when investigating how or why something works, recalling project context, or explaining a system. |
| [miso-review](../../plugins/miso-stack/skills/miso-review/SKILL.md) | Reviews correctness, security, change impact, and code quality against evidence. Use for code review, adversarial review, blast-radius analysis, or final quality checks. |
| [miso-setup](../../plugins/miso-stack/skills/miso-setup/SKILL.md) | Checks MisoStack discovery and host capabilities without choosing fixed models. Use when installing MisoStack, diagnosing skill loading, or configuring a project. |
| [miso-spec](../../plugins/miso-stack/skills/miso-spec/SKILL.md) | Turns the conversation and repository evidence into a scoped specification with acceptance checks. Use when the user asks for a spec, requirements, or a written definition of what to build. |
| [miso-swarm](../../plugins/miso-stack/skills/miso-swarm/SKILL.md) | Coordinates bounded independent work and verifies returned artifacts. Use when parallel research, coverage partitions, or candidate races are requested. |
| [miso-tdd](../../plugins/miso-stack/skills/miso-tdd/SKILL.md) | Uses a failing behavioral test to guide a small implementation change. Use when TDD is requested or a bug has a practical regression-test path. |
| [miso-tickets](../../plugins/miso-stack/skills/miso-tickets/SKILL.md) | Splits an agreed spec or plan into small verifiable tickets with explicit blockers. Use for breaking work into issues or preparing a backlog, with local files or an authorized tracker. |
| [miso-trail](../../plugins/miso-stack/skills/miso-trail/SKILL.md) | Keeps a concise evidence-backed decision trail for long work. Use for unattended runs, migrations, or an auditable handoff. |
| [miso-verify](../../plugins/miso-stack/skills/miso-verify/SKILL.md) | Runs, creates, or maintains project-specific verification tools and feature maps. Use when proving a change works, creating a control skill, or auditing verification coverage. |

## Workflows

| Workflow | When to use it | Completion evidence |
| --- | --- | --- |
| [Investigate a question](../../plugins/miso-stack/skills/miso/playbooks/investigation.md) | Explain a mechanism, establish a cause, or compare evidence. | Cited code or recorded observations answer the question; unknowns are explicit. |
| [Fix a defect](../../plugins/miso-stack/skills/miso/playbooks/bug-fix.md) | Reproduce and repair incorrect behavior. | The original failing path now passes, with before-and-after evidence. |
| [Build a feature](../../plugins/miso-stack/skills/miso/playbooks/feature.md) | Add or change user-visible behavior. | The acceptance journey runs on the real artifact, including a relevant failure path. |
| [Compare prototypes](../../plugins/miso-stack/skills/miso/playbooks/prototype.md) | Resolve a design or behavioral uncertainty with executable alternatives. | Comparable observations support the chosen design or explicitly show an unresolved result. |
| [Refactor safely](../../plugins/miso-stack/skills/miso/playbooks/refactoring.md) | Change structure while preserving the agreed behavior. | The same observable contracts hold before and after the structural change. |
| [Improve performance](../../plugins/miso-stack/skills/miso/playbooks/performance.md) | Fix a specific measured performance problem. | Comparable samples show an improvement without violating correctness. |
| [Plan verified work](../../plugins/miso-stack/skills/miso/playbooks/plan.md) | Split a multi-phase change into dependent, checkable units. | The plan is valid and each completed task has evidence; the final integration is checked separately. |
| [Write documentation](../../plugins/miso-stack/skills/miso/playbooks/documentation.md) | Create or correct a tutorial, how-to, reference, or explanation. | A reader can follow the documented procedure and obtain the stated result. |
| [Improve a metric repeatedly](../../plugins/miso-stack/skills/miso/playbooks/hillclimb.md) | Run a bounded series of measured experiments. | Each accepted experiment has comparable measurements and the final result passes correctness checks. |
| [Diagnose a live runtime](../../plugins/miso-stack/skills/miso/playbooks/runtime-forensics.md) | Investigate leaks, CPU use, or intermittent behavior without assuming a fix. | Captured runtime observations support the diagnosed mechanism or a bounded set of hypotheses. |
| [Analyze a captured trace](../../plugins/miso-stack/skills/miso/playbooks/trace-forensics.md) | Explain a profile, trace, heap snapshot, or crash artifact. | The diagnosis points to concrete trace events and states capture limitations. |
| [Verify visual equivalence](../../plugins/miso-stack/skills/miso/playbooks/visual-parity.md) | Compare two UI implementations under matched conditions. | The agreed state matrix matches the baseline within declared tolerances. |
| [Author a skill](../../plugins/miso-stack/skills/miso/playbooks/authoring-a-skill.md) | Create or change a skill and prove its behavior. | The skill loads and produces the intended behavior on representative sandbox cases. |
| [Evaluate agent behavior](../../plugins/miso-stack/skills/miso/playbooks/eval.md) | Measure a prompt or skill change against explicit cases. | Recorded cases and artifacts support each evaluation verdict. |
| [Bring a PR to review readiness](../../plugins/miso-stack/skills/miso/playbooks/babysit.md) | Resolve CI failures, review findings, or conflicts on an existing PR. | Readiness is established for the current PR revision; merge remains a separate action. |
| [Prepare and ship an approved change](../../plugins/miso-stack/skills/miso/playbooks/shipping.md) | Verify a release or merge candidate before an authorized external action. | The exact candidate is verified and the remote outcome is confirmed only if an authorized action ran. |
| [Run until a defined outcome](../../plugins/miso-stack/skills/miso/playbooks/autonomous-run.md) | Execute one long task while the user is away. | The declared outcome has evidence, or remaining blockers and exact next steps are documented. |
| [Coordinate a multi-phase program](../../plugins/miso-stack/skills/miso/playbooks/orchestrate.md) | Own dependent tasks across sessions or workers. | Task ownership and dependency order are valid, and integrated artifacts pass their declared checks. |
| [Process an independent work queue](../../plugins/miso-stack/skills/miso/playbooks/autopilot-full.md) | Build and verify independent changes with explicit publication gates. | Each queue item has independent proof and external effects remain within explicit authority. |
| [Build a stack for later landing](../../plugins/miso-stack/skills/miso/playbooks/autopilot-stack.md) | Prepare an ordered sequence of dependent changes. | Each unit and the combined tip are verified, with a clear dependency order. |
| [Resume prior work](../../plugins/miso-stack/skills/miso/playbooks/session-pickup.md) | Continue from a handoff or prior task state. | The resumed state is reconciled against current artifacts rather than accepted from a prior summary. |
| [Pause with a usable handoff](../../plugins/miso-stack/skills/miso/playbooks/pause-safely.md) | Suspend work without losing state or proof. | A new session can identify current state and resume without reconstructing lost context. |
| [Audit local runtime leftovers](../../plugins/miso-stack/skills/miso/playbooks/worktree-cleanup.md) | Inspect worktrees or simulator resources before approved cleanup. | The candidate list is justified; any deletion has scoped approval and a verified outcome. |
| [Prepare a focused pull request](../../plugins/miso-stack/skills/miso/playbooks/opening-a-pr.md) | Package an authorized change for review. | The review package accurately describes the full change and its executed checks. |
