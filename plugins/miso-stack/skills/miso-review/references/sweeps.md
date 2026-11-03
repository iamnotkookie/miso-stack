# Sweep each hunk

Thorough reviews come from applying one question at a time to every hunk, not from a single clever read. Skip a sweep that cannot apply, and say that you skipped it. On a large diff, give each sweep to its own read-only reviewer with [swarm](../../miso-swarm/SKILL.md) when the host permits it. Send the diff, not your conclusions.

- **Duplication.** Compare each addition with the base using [search](search.md), and compare the additions with each other.
- **Unused and leftover code.** List each added symbol with its reader count. A zero becomes a one-line `nit:` or `question:`. Confirm that moved code left its old home.
- **Values and shapes.** Ask why each new threshold or default has that value. Look for raw strings or dictionaries that bypass an existing type, optional parameters that are always required, and hand-written parsing that an existing tool already does.
- **Claims and tests.** Check each claim in the description against the diff. When a bug fix names a failing case, look for a test that fails without the fix.
- **Rollout.** Consider a deployment where both versions serve traffic, a backfill on an empty table, configuration in each environment, and a changed field that should have been a new one.
- **Permissions and identifiers.** Check authorization on each new endpoint and action, on both the client and the server. Check the principal in use, whether another tenant can reach it, and whether private data reaches logs or previews. Confirm that each identifier is the right one for its level in the hierarchy.
- **Scale and concurrency.** Check the complexity and collection choice of each new loop, repeated calls that have a batch form, the scope of each lock, and whether the race being defended can occur.
- **Field choice.** For each value the new logic reads, ask whether it is the authoritative one. Walk one concrete execution, and name the exact replacement when it is not.
- **Removed behavior.** Treat the deleted or replaced code as a specification. List its branches, side effects, caching, ordering, handling of nulls and errors, permissions, locks, retries, timeouts, and filters. Side effects include writes, invalidation, logs, metrics, and notifications. For each item, cite where the new path keeps it. When you cannot, ask where the behavior went.
- **Outside knowledge.** Production scale, deployment layout, flag values in production, and the roadmap cannot be proven from the repository. Write these as questions, at most four in a round.
- **What people see.** Check exact wording, links, large values, and the loading, empty, and error states. Suggest replacement text. Flag comments that only narrate the diff.

Combine the results and remove duplicates by location. Drop what you cannot confirm at the base, or turn it into a question. When the round is too long, cut speculation before a verified one-line note.
