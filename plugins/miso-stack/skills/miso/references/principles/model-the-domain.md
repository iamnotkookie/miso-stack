# Model the domain

**Apply when:** You write stateful logic, heavy branching, or a shape assumption that repeats across files.

**Rule:** Represent the domain directly. Use explicit states, a typed model, or a table instead of scattered conditionals.

**Why:** Flags have combinations that nobody defined. A named state has one meaning.

- Name the organizing structure before you write logic.
- Prefer a state machine to several booleans, and a table to a long branch.
