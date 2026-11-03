# Outcome-oriented execution

**Apply when:** You plan a rewrite or migration with phases.

**Rule:** Go to the target design. Keep a temporary compatibility state only with a named need and a removal condition.

**Why:** Compatibility states outlive their plans, and every later reader must learn both worlds.

- Write the end state before the first phase.
- Judge each phase by how far it moves toward the end state.
