# Experience first

**Apply when:** You make a product, interface, or scope tradeoff.

**Rule:** Start with how a person calls, operates, and recovers the system. Internal convenience comes second.

**Why:** Users see the interface, the empty state, and the error path. They do not see the implementation.

- Write the caller's example before the internals.
- Check the empty path and the failure path, not only the successful one.
