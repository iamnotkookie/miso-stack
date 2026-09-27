# Design modules that hide complexity

A module exposes an interface and contains an implementation. Its interface includes everything callers must know: parameters, failure modes, ordering, configuration, ownership, and performance constraints. A small signature can still impose a large burden on callers.

A useful module lets callers do substantial work while knowing few internal rules. Assess it from a usage example and its tests, not from a ratio of code lines. Check whether removing it would spread real complexity across callers or merely remove a forwarding layer.

A seam is a place where behavior can be replaced without editing the caller. An adapter is one implementation at that seam. Prefer existing public seams for tests. Introduce a new seam for an observed variation or testing need, not an imagined future provider. Internal implementation seams need not become public configuration.

Keep state, decisions, and their verification near the module that owns them. Warning signs include callers repeating setup sequences, exposing internal data structures, long forwarding chains, and tests coupled to internal steps. Dependencies that perform effects should be substitutable where necessary; pure decisions should return values that can be checked directly.

For a substantial choice, compare structurally different caller examples and interfaces using the same scenarios. Consider who owns state, what facts escape, how errors travel, and what must change to support the next real requirement. Build the smallest prototype that distinguishes the candidates.

When implementing reveals repeated workarounds, revisit the design rather than accumulating parameters or casts. Preserve valid caller behavior and other people's edits while replacing the failed approach.
