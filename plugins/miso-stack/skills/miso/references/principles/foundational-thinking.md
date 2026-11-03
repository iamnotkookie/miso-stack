# Foundational thinking

**Apply when:** You are about to write the first logic of a subsystem or stateful feature.

**Rule:** Name the domain objects, the state owners, and the proof method before you add behavior.

**Why:** Code follows the data shape. A wrong shape costs more to change after callers depend on it.

- Choose data structures from actual access patterns and invariants.
- Shared domain structure matters more than similar text. Similar statements need not become one abstraction.
- Before actors share mutable state, trace the concurrent writes and choose isolation or one owner.
- Build only the types, checks, and setup that unblock later work.
