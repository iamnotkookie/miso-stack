# Sequence verifiable units

**Apply when:** You do multi-step work, such as a sweep or a migration, or you order commits and pull requests.

**Rule:** Divide the work into small pieces, and give each piece its own check. Do not start the next piece until that check passes.

**Why:** A failure is cheap to locate right after the edit that caused it. After a batch, it hides among other edits.

- Order delivery so that the history proves the work: the failing test, then the fix.
- Other useful orders: subtraction before reshaping, a baseline before the treatment.
