# Fix root causes

**Apply when:** You debug a symptom or feel tempted to add a guard.

**Rule:** Follow the symptom back to the earliest wrong state, and repair that.

**Why:** A guard at the symptom leaves the wrong state alive for the next caller.

- Each line you ship needs an observation behind it. An untested "maybe this helps" stays out of the diff.
- When a test disproves your theory, undo the edits that the theory led to.
- Add a guard only for a state that the system should allow.
