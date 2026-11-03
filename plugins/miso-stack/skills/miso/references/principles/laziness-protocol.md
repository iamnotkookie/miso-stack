# Laziness protocol

**Apply when:** You size a diff, refactor, or want to add a layer, option, or helper.

**Rule:** Choose the smallest complete change. Deletion counts as progress.

**Why:** Someone who did not write each added line must read it and keep it correct.

- Inspect forwarding functions, repeated decisions, and representation leaks before you add an abstraction.
- Put a decision with its owner. Do not coordinate copies across callers.
- A flag that must travel through many layers shows that a responsibility is in the wrong place.
- Reuse a proven tool before you invent one.
- Optimize the maintenance burden, not a line count. A deep module can hide substantial work behind a small interface.
