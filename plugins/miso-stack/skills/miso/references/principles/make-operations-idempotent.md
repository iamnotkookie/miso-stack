# Make operations idempotent

**Apply when:** A command, lifecycle step, or loop can run again after a crash or retry.

**Rule:** Running it again must leave the same final state and cause no extra effect.

**Why:** Retries happen at the worst moment, when nobody watches.

- Use a stable identity and explicit state.
- Test the second run, not only the first.
