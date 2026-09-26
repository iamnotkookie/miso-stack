# How MisoStack relates to pstack

MisoStack is an original stack. Lauren Tan's two guides are its design references. The comparison below uses [this pstack revision](https://github.com/cursor/plugins/tree/ecc249f1e306fc64ddf83c7bed16cacf7c2239db/pstack). It records capability coverage, not identical implementation or a claim that every host has executed every workflow.

MisoStack keeps one entry skill, loads workflows when needed, and uses 15 supporting skills. The 23 engineering principles share one reference. The eight default workflows remain the starting set. Specialist workflows cover the broader product.

The main deliberate differences are model defaults, explicit approval for messages and destructive actions, four native harness maps, and no dependency on Cursor cloud hosting or Grok Bot UI. Routine setup produces a tested specification when the host has no scheduler. It does not pretend to activate a service.

| pstack capability | MisoStack implementation |
| --- | --- |
| `reproduce-and-fix-issues` | [skills/miso-automate/SKILL.md](../../plugins/miso-stack/skills/miso-automate/SKILL.md) |
| `setup-benny` | [skills/miso-automate/SKILL.md](../../plugins/miso-stack/skills/miso-automate/SKILL.md) |
| `triage-issue-reports` | [skills/miso-automate/SKILL.md](../../plugins/miso-stack/skills/miso-automate/SKILL.md) |
| `architect` | [skills/miso-design/SKILL.md](../../plugins/miso-stack/skills/miso-design/SKILL.md) |
| `arena` | [skills/miso-arena/SKILL.md](../../plugins/miso-stack/skills/miso-arena/SKILL.md) |
| `automate-me` | [skills/miso-author/SKILL.md](../../plugins/miso-stack/skills/miso-author/SKILL.md) |
| `blast-radius` | [skills/miso-review/SKILL.md](../../plugins/miso-stack/skills/miso-review/SKILL.md) |
| `bro` | [skills/miso-research/SKILL.md](../../plugins/miso-stack/skills/miso-research/SKILL.md) |
| `create-verification-skill` | [skills/miso-verify/SKILL.md](../../plugins/miso-stack/skills/miso-verify/SKILL.md) |
| `figure-it-out` | [skills/miso-plan/SKILL.md](../../plugins/miso-stack/skills/miso-plan/SKILL.md) |
| `how` | [skills/miso-research/SKILL.md](../../plugins/miso-stack/skills/miso-research/SKILL.md) |
| `interrogate` | [skills/miso-review/SKILL.md](../../plugins/miso-stack/skills/miso-review/SKILL.md) |
| `maintain-verification-skill` | [skills/miso-verify/SKILL.md](../../plugins/miso-stack/skills/miso-verify/SKILL.md) |
| `make-bot-ui` | Grok Bot UI is outside the four approved harnesses. |
| `no-comments` | [skills/miso-review/SKILL.md](../../plugins/miso-stack/skills/miso-review/SKILL.md) |
| `poteto-mode` | [skills/miso/SKILL.md](../../plugins/miso-stack/skills/miso/SKILL.md) |
| `authoring-a-skill` | [skills/miso/playbooks/authoring-a-skill.md](../../plugins/miso-stack/skills/miso/playbooks/authoring-a-skill.md) |
| `autonomous-run` | [skills/miso/playbooks/autonomous-run.md](../../plugins/miso-stack/skills/miso/playbooks/autonomous-run.md) |
| `autopilot-full` | [skills/miso/playbooks/autopilot-full.md](../../plugins/miso-stack/skills/miso/playbooks/autopilot-full.md) |
| `autopilot-stack` | [skills/miso/playbooks/autopilot-stack.md](../../plugins/miso-stack/skills/miso/playbooks/autopilot-stack.md) |
| `babysit` | [skills/miso/playbooks/babysit.md](../../plugins/miso-stack/skills/miso/playbooks/babysit.md) |
| `bug-fix` | [skills/miso/playbooks/bug-fix.md](../../plugins/miso-stack/skills/miso/playbooks/bug-fix.md) |
| `eval` | [skills/miso/playbooks/eval.md](../../plugins/miso-stack/skills/miso/playbooks/eval.md) |
| `feature` | [skills/miso/playbooks/feature.md](../../plugins/miso-stack/skills/miso/playbooks/feature.md) |
| `hillclimb` | [skills/miso/playbooks/hillclimb.md](../../plugins/miso-stack/skills/miso/playbooks/hillclimb.md) |
| `investigation` | [skills/miso/playbooks/investigation.md](../../plugins/miso-stack/skills/miso/playbooks/investigation.md) |
| `multi-phase-plan` | [skills/miso/playbooks/plan.md](../../plugins/miso-stack/skills/miso/playbooks/plan.md) |
| `opening-a-pr` | [skills/miso/playbooks/opening-a-pr.md](../../plugins/miso-stack/skills/miso/playbooks/opening-a-pr.md) |
| `orchestrate` | [skills/miso/playbooks/orchestrate.md](../../plugins/miso-stack/skills/miso/playbooks/orchestrate.md) |
| `pause-safely` | [skills/miso/playbooks/pause-safely.md](../../plugins/miso-stack/skills/miso/playbooks/pause-safely.md) |
| `perf-issue` | [skills/miso/playbooks/performance.md](../../plugins/miso-stack/skills/miso/playbooks/performance.md) |
| `prototype` | [skills/miso/playbooks/prototype.md](../../plugins/miso-stack/skills/miso/playbooks/prototype.md) |
| `refactoring` | [skills/miso/playbooks/refactoring.md](../../plugins/miso-stack/skills/miso/playbooks/refactoring.md) |
| `runtime-forensics` | [skills/miso/playbooks/runtime-forensics.md](../../plugins/miso-stack/skills/miso/playbooks/runtime-forensics.md) |
| `session-pickup` | [skills/miso/playbooks/session-pickup.md](../../plugins/miso-stack/skills/miso/playbooks/session-pickup.md) |
| `shipping` | [skills/miso/playbooks/shipping.md](../../plugins/miso-stack/skills/miso/playbooks/shipping.md) |
| `trace-forensics` | [skills/miso/playbooks/trace-forensics.md](../../plugins/miso-stack/skills/miso/playbooks/trace-forensics.md) |
| `visual-parity` | [skills/miso/playbooks/visual-parity.md](../../plugins/miso-stack/skills/miso/playbooks/visual-parity.md) |
| `worktree-cleanup` | [skills/miso/playbooks/worktree-cleanup.md](../../plugins/miso-stack/skills/miso/playbooks/worktree-cleanup.md) |
| `principle-attack-the-premise` | [skills/miso/references/principles.md](../../plugins/miso-stack/skills/miso/references/principles.md) |
| `principle-boundary-discipline` | [skills/miso/references/principles.md](../../plugins/miso-stack/skills/miso/references/principles.md) |
| `principle-build-the-lever` | [skills/miso/references/principles.md](../../plugins/miso-stack/skills/miso/references/principles.md) |
| `principle-encode-lessons-in-structure` | [skills/miso/references/principles.md](../../plugins/miso-stack/skills/miso/references/principles.md) |
| `principle-exhaust-the-design-space` | [skills/miso/references/principles.md](../../plugins/miso-stack/skills/miso/references/principles.md) |
| `principle-experience-first` | [skills/miso/references/principles.md](../../plugins/miso-stack/skills/miso/references/principles.md) |
| `principle-fix-root-causes` | [skills/miso/references/principles.md](../../plugins/miso-stack/skills/miso/references/principles.md) |
| `principle-foundational-thinking` | [skills/miso/references/principles.md](../../plugins/miso-stack/skills/miso/references/principles.md) |
| `principle-guard-the-context-window` | [skills/miso/references/principles.md](../../plugins/miso-stack/skills/miso/references/principles.md) |
| `principle-laziness-protocol` | [skills/miso/references/principles.md](../../plugins/miso-stack/skills/miso/references/principles.md) |
| `principle-make-operations-idempotent` | [skills/miso/references/principles.md](../../plugins/miso-stack/skills/miso/references/principles.md) |
| `principle-migrate-callers-then-delete-legacy-apis` | [skills/miso/references/principles.md](../../plugins/miso-stack/skills/miso/references/principles.md) |
| `principle-minimize-reader-load` | [skills/miso/references/principles.md](../../plugins/miso-stack/skills/miso/references/principles.md) |
| `principle-model-the-domain` | [skills/miso/references/principles.md](../../plugins/miso-stack/skills/miso/references/principles.md) |
| `principle-never-block-on-the-human` | [skills/miso/references/principles.md](../../plugins/miso-stack/skills/miso/references/principles.md) |
| `principle-outcome-oriented-execution` | [skills/miso/references/principles.md](../../plugins/miso-stack/skills/miso/references/principles.md) |
| `principle-prove-it-works` | [skills/miso/references/principles.md](../../plugins/miso-stack/skills/miso/references/principles.md) |
| `principle-redesign-from-first-principles` | [skills/miso/references/principles.md](../../plugins/miso-stack/skills/miso/references/principles.md) |
| `principle-separate-before-serializing-shared-state` | [skills/miso/references/principles.md](../../plugins/miso-stack/skills/miso/references/principles.md) |
| `principle-sequence-verifiable-units` | [skills/miso/references/principles.md](../../plugins/miso-stack/skills/miso/references/principles.md) |
| `principle-subtract-before-you-add` | [skills/miso/references/principles.md](../../plugins/miso-stack/skills/miso/references/principles.md) |
| `principle-test-behavior-not-implementation` | [skills/miso/references/principles.md](../../plugins/miso-stack/skills/miso/references/principles.md) |
| `principle-type-system-discipline` | [skills/miso/references/principles.md](../../plugins/miso-stack/skills/miso/references/principles.md) |
| `recall` | [skills/miso-research/SKILL.md](../../plugins/miso-stack/skills/miso-research/SKILL.md) |
| `reflect` | [skills/miso-reflect/SKILL.md](../../plugins/miso-stack/skills/miso-reflect/SKILL.md) |
| `setup-pstack` | [skills/miso-setup/SKILL.md](../../plugins/miso-stack/skills/miso-setup/SKILL.md) |
| `show-me-your-work` | [skills/miso-trail/SKILL.md](../../plugins/miso-stack/skills/miso-trail/SKILL.md) |
| `swarm` | [skills/miso-swarm/SKILL.md](../../plugins/miso-stack/skills/miso-swarm/SKILL.md) |
| `tdd` | [skills/miso-tdd/SKILL.md](../../plugins/miso-stack/skills/miso-tdd/SKILL.md) |
| `teach` | [skills/miso-research/SKILL.md](../../plugins/miso-stack/skills/miso-research/SKILL.md) |
| `technical-writing` | [skills/miso-docs/SKILL.md](../../plugins/miso-stack/skills/miso-docs/SKILL.md) |
| `typescript-best-practices` | [skills/miso-review/SKILL.md](../../plugins/miso-stack/skills/miso-review/SKILL.md) |
| `unslop` | [skills/miso-docs/SKILL.md](../../plugins/miso-stack/skills/miso-docs/SKILL.md) |
| `why` | [skills/miso-research/SKILL.md](../../plugins/miso-stack/skills/miso-research/SKILL.md) |

## Executable support

| pstack support | MisoStack approach |
| --- | --- |
| Plan-format checker | The `plan check` helper validates a dependency graph and accepted proof hashes. |
| Orchestration store and command | The local plan ledger owns task state. Native harness tools perform dispatch and execution. It does not provide a background scheduler. |
| PR watch command | The babysit workflow uses the project's existing forge CLI or connector, with bounded polling and an exact-head check. No second forge API client is shipped. |
| Worktree audit script | The cleanup workflow requires a read-only ownership and merge audit before approved deletion. It does not perform automatic cleanup. |
| Decision-log script | The `trail` helper appends a structured record with existing evidence. |
| Cursor cloud and Grok Bot services | Outside the four-harness scope. No hosted service is claimed. |

These are deliberate implementation boundaries. MisoStack provides workflows and local tools; it does not duplicate each upstream script.

The machine-readable inventory is [reference-audit.json](../reference-audit.json). Qualification results live in [verification](../verification.md). A source mapping does not establish runtime support.
