# Test behavior, not implementation

**Apply when:** A test is being added, edited, or kept after a change.

**Rule:** Check a known result through the interface that callers use.

**Why:** A test that restates the source fails on every refactor and passes on real defects.

- Use a fixed expected value, not a copy of the logic.
- Keep real dependencies when that is safe and practical.
