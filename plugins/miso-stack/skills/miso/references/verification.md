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
