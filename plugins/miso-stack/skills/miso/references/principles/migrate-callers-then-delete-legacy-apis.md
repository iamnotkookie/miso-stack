# Migrate callers, then delete legacy APIs

**Apply when:** A new internal API replaces an old one that still has callers.

**Rule:** Move the known callers and remove the old code in one wave, with authorization.

**Why:** Two parallel APIs become permanent, and every new caller must choose.

- Prove compatibility where an external contract requires it.
- Search for readers that grep misses: config, serialized data, and other languages.
