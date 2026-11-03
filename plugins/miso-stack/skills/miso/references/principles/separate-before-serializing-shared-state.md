# Separate before serializing shared state

**Apply when:** Two workers or processes could change one file, branch, key, or object at the same time.

**Rule:** Remove the sharing first. Prefer separate state or one clear owner over competing writes and more locks.

**Why:** A lock keeps the conflict and adds waiting. Separation removes the conflict.

- Serialize only for a real invariant, and name it.
