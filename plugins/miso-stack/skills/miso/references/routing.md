# Route the request

The user only needs to remember `miso`. Select by the requested result, not by a keyword that happens to occur in the prompt. Load only the relevant skill and its required references. Do not list this whole menu back to the user.

For a routing evaluation, return the skill name and the mode named after the link in the table. If the table names no mode, use `default`. Plain restatement is the narrow case under the research skill's Teach section; the entry handles it without additional tool calls.

## Select a capability

| What the user wants | Skill and mode |
| --- | --- |
| Explain how code runs, where it belongs, or who owns state | [miso-research](../../miso-research/SKILL.md), mechanics |
| Explain the reason for an existing design | [miso-research](../../miso-research/SKILL.md), intent |
| Recall recent work or reconstruct current context | [miso-research](../../miso-research/SKILL.md), recall |
| Teach a subsystem or explain a change | [miso-research](../../miso-research/SKILL.md), teach |
| Say the previous answer plainly; “bro” | [miso-research](../../miso-research/SKILL.md), plain restatement |
| Design architecture or simplify a module interface | [miso-design](../../miso-design/SKILL.md) |
| Compare alternative designs or implementations | [miso-design](../../miso-design/SKILL.md) |
| Tend recurring code smells, duplicate helpers, or architecture drift | [miso-garden](../../miso-garden/SKILL.md), inspect |
| Enforce structural rules or install anti-slop lint checks | [miso-garden](../../miso-garden/SKILL.md), enforce |
| Repeat build/check/fix work, resume a loop, or cancel it | [miso-loop](../../miso-loop/SKILL.md) |
| Measure or improve latency, throughput, memory, or startup | [miso-perf](../../miso-perf/SKILL.md) |
| Diagnose broken, intermittent, or slow behavior | [miso-debug](../../miso-debug/SKILL.md) |
| Review code against standards and requirements | [miso-review](../../miso-review/SKILL.md), code review |
| Find what a change could break elsewhere | [miso-review](../../miso-review/SKILL.md), impact |
| Challenge a design or change; independent adversarial review | [miso-review](../../miso-review/SKILL.md), challenge |
| Remove redundant comments or fix the problems they conceal | [miso-review](../../miso-review/SKILL.md), comments |
| Prove that a change works in the app | [miso-verify](../../miso-verify/SKILL.md), run |
| Create a project control skill or driver | [miso-verify](../../miso-verify/SKILL.md), create |
| Repair a stale driver or feature map | [miso-verify](../../miso-verify/SKILL.md), maintain |
| Use test-driven development or add a regression test | [miso-tdd](../../miso-tdd/SKILL.md) |
| Write a tutorial, guide, reference, or explanation | [miso-docs](../../miso-docs/SKILL.md), write |
| Remove jargon, filler, or AI phrasing from supplied text | [miso-docs](../../miso-docs/SKILL.md), edit |
| Turn the conversation into requirements or a spec | [miso-spec](../../miso-spec/SKILL.md) |
| Split agreed work into tickets with blockers | [miso-tickets](../../miso-tickets/SKILL.md) |
| Implement an agreed spec or tickets | [miso-plan](../../miso-plan/SKILL.md), execute; use TDD, verification, and review where relevant |
| Plan a migration or resume dependent work | [miso-plan](../../miso-plan/SKILL.md) |
| Resolve a merge or rebase already in progress | [miso-merge](../../miso-merge/SKILL.md) |
| Run independent coverage or a race in parallel | [miso-swarm](../../miso-swarm/SKILL.md) |
| Set up the package or diagnose skill discovery | [miso-setup](../../miso-setup/SKILL.md) |
| Create or improve a reusable skill | [miso-author](../../miso-author/SKILL.md) |
| Test routing or skill behavior in a sandbox | [miso-eval](../../miso-eval/SKILL.md) |
| Learn from an observed workflow failure | [miso-reflect](../../miso-reflect/SKILL.md) |
| Design a routine or automate a proven check | [miso-automate](../../miso-automate/SKILL.md) |
| Keep an evidence-backed record for a long task | [miso-trail](../../miso-trail/SKILL.md) |

## Keep the task boundary

- A review is read-only unless fixes are also requested. “Challenge this” is review, not implementation.
- A spec defines the work. Tickets divide it. A plan executes it only when execution is requested. Do not silently move between these stages.
- “Explain that more simply” only rewrites the existing answer. It does not authorize tools, repository searches, or new claims.
- A bug report routes to diagnosis. A repair request adds the bug-fix workflow and verification. A diagnosis-only request stops at evidence and a cause or explicit uncertainty.
- “What would this break?” selects impact review even if the diff is small. “Remove comments” selects comment cleanup, not prose editing.
- A conflict in an existing merge/rebase selects merge resolution. “Merge my PR” is a separate shipping action with its own authority.
- Missing history, a tracker, a worker API, or an app runtime must be stated. Use the supported local or serial path; do not invent access or completed work.
- Parallel workers follow project configuration or host defaults. A request mentioning several skills does not automatically request a swarm.
- Gardening inspection is read-only; a request to fix recurring smells adds enforcement. A request to install lint rules does not also authorize migration of every existing violation.
- Performance work selects miso-perf; an unexplained failure or timeout selects diagnosis. A bounded repeated optimization uses miso-perf with miso-loop. A recurring scheduled check selects automation, not an active-session loop.

For a combined request, sequence only the stages requested. For “spec this, split it into tickets, then implement”, use spec → tickets → plan, with verification and review before claiming completion. Honor any explicit stop point.

When the result is clear, proceed. If two interpretations would produce materially different work, state your best interpretation and ask one focused question while doing independent discovery. Never ask the user to pick a skill name.
