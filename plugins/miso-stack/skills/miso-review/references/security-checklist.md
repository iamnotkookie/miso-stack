# Security checklist

Use this on every change. Start at entry points: handlers, queue consumers, command lines, webhooks, scheduled jobs, uploads, and deserializers. Follow untrusted input to each sensitive sink.

A confirmed finding in this file makes the verdict `request changes`. Give the entry point, the boundary crossed, the trigger, the impact, and the fix. Describe exploit conditions in words. Never repeat a secret value in a note. Do not exploit a live system or use real user data.

## Blocks the change

- A secret, token, key, or credential in code, configuration, logs, fixtures, or CI output.
- A token or role with more scope than the task needs, such as wildcard IAM or a repository-wide deploy key.
- Production or SSH access with no restriction, expiry, or review path.
- A missing or late authorization check, access to another user's object by identifier, or a role or tenant that the client supplies.
- Injection: SQL, shell, template, path traversal, server-side request forgery, unsafe deserialization, or an open redirect.

## Check each time

- **Dependencies.** Provenance, maintainer, install scripts, lockfile integrity, and pinning.
- **CI and release.** Untrusted input in a run step, secrets reachable from forks, a privileged trigger that runs contributed code, write-scoped tokens, and actions pinned by a movable tag.
- **Cryptography.** Homemade primitives, ECB mode, a fixed initialization vector, comparisons that are not constant-time, and weak randomness for tokens.
- **Data exposure.** Personal data in logs or errors, API responses that return too much, and cached private data.
- **Infrastructure.** Public storage, open ingress, disabled certificate checks, and containers that run as root or in privileged mode.
- **Exhaustion.** Unbounded input size, regular expressions that backtrack, and unbounded fan-out.

## Escalate to a scoped audit

Run [miso-audit](../../miso-audit/SKILL.md) in code mode, scoped to the diff between base and head, when the change:

- Alters authentication, authorization, sessions, tokens, or permissions.
- Touches cryptography, key handling, secret storage, or certificate validation.
- Adds a network entry point, webhook, upload, deserializer, or parser of untrusted input.
- Changes tenant scoping, export, backup, deletion, or retention.
- Changes CI, release, signing, or dependency resolution.
- Changes IAM, infrastructure as code, or container or ingress configuration.
- Grants or changes production access, SSH keys, or service account scope.
- Adds model tool use, agent actions, or an MCP integration.

State that the audit is a partial pass. Map its results into the review: `confirmed` is an `issue:` with severity and the smallest fix, `needs_validation` is a `question:` that names the open fact, and `rejected` is dropped. Skip escalation for docs, tests, style, and changes with no path from untrusted input to a sensitive sink. When you are unsure, ask once, because an audit costs far more than this list.
