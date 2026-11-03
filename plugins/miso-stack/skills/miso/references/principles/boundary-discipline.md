# Boundary discipline

**Apply when:** You add validation, error handling, or a framework adapter.

**Rule:** Validate untrusted input at the boundary. Trust internal types after that point.

**Why:** Checks repeated inside domain code hide which data can really be invalid.

- Parse external data once into a validated type.
- Keep integration failures out of pure domain logic.
