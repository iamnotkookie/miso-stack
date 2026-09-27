# Project control contract

A project control tool drives the real app. Keep it in that app's repository and use existing browser, terminal, HTTP, or simulator tooling.

| Operation | Required behavior |
| --- | --- |
| help | Describe commands, prerequisites, examples, and exit status. |
| doctor | Check the intended instance, readiness, auth, and owned runtime state without changes. |
| drive | Perform a real user operation using stable selectors or public commands. |
| observe | Capture output and side effects, including the state before and after a change. |
| measure | State the workload, units, warm-up, sample count, and environment. |
| cleanup | Stop only owned runtime processes. Preserve proof. Require approval for data deletion. |

Use JSON for automation output. Send diagnostics to stderr. Exit nonzero on a failed operation. Include a suggested recovery action in errors. Compose small subcommands rather than one opaque script. Destructive operations need a dry-run path; verify that dry run does not mutate state or send requests with effects.

Document setup, test accounts, seed data, isolated ports and profiles, readiness, teardown, and evidence paths. Keep secrets in environment variables or the project's secret store. An authenticated page is not proof that the requested action worked.

## Choose controls from the real app

This is a vocabulary for project drivers, not a list of implemented MisoStack commands. Add only controls the app and available runtime can support. List unsupported controls with a reason. A CLI-only app does not need pretend screenshots or browser navigation.

| Group | Candidate controls | What to expose |
| --- | --- | --- |
| Inspection | `info`, `snapshot`, `screenshot`, `components` | Instance and runtime identity; semantic UI state; actual images; component data when observable |
| Navigation | `home`, `new-session`, `select-project`, `select-runtime`, `scroll` | Explicit context and destination, with confirmation of the selected surface |
| Interaction | `send`, `click`, `click-xy`, `aria-click`, `type`, `press`, `eval`, `upload-image`, `add-context`, `feature-flag` | User actions through stable controls, followed by observed state |
| Performance | `trace`, `profile`, `record`, `perf-metrics`, `wait-settle` | Real runtime captures, timing units, sample conditions, and bounded settling |
| Streaming | `console`, `network-log`, `network-summary` | Bounded capture windows with cursor or cancellation support and redacted payloads |
| Health and cleanup | `doctor`, `cleanup`, `watch --restart` | Readiness, owned resources, a mutation-free cleanup preview, and bounded restarts |

## Make commands compose

Keep a small interface that hides launch, transport, and selector details. Pass stable instance, session, or capture IDs between commands. An agent should not need to reconstruct internal app state before each action. Group controls under subcommands when the surface grows, for example `control inspect snapshot` and `control perf trace`.

Provide root and subcommand `--help` with prerequisites, examples, flags, output fields, and exit codes. Return JSON for automation, with a stable success/error shape. An error should identify the operation and target, explain the failed precondition, and suggest a concrete recovery command. Keep diagnostics on stderr and exit nonzero for failed or unsupported operations. Do not hide partial results or empty captures behind success.

For a mutating command, return what changed and enough identity to inspect it. Commands that can delete data, clear sessions, or stop shared resources need `--dry-run`. The preview must use read-only discovery and show exact planned targets and exclusions. It must not send an effectful request. Execution must recheck ownership and the target before acting; preview is not approval.

Prefer accessible names and semantic selectors. Use coordinates only from a recent observed screen, then verify the result. Treat `eval` as arbitrary execution in the app context, subject to normal permissions. Scope feature flags to the test session when possible and restore only values changed by the run.

Define `wait-settle` in observable terms, such as a completed stream and stable layout over a stated interval. Always set a timeout. An open websocket is not necessarily unfinished work. Bound `watch --restart` by time or restart count and retry delay; stop only processes owned by this run.

## Prove the control contract

Run one complete user journey plus a missing-instance failure, invalid input, and a timeout. Parse JSON output as JSON. For destructive commands, compare state before and after the dry run and verify it is unchanged. Test cleanup against an unrelated resource and retain it. Keep proof outside runtime teardown paths. Do not claim commands are supported until their real adapter has run.
