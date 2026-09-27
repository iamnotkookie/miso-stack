# Put the rules in the code

A useful architecture makes the intended change easy and the invalid change fail early. Start with who owns data, which layer may change it, and which interfaces callers can use. Inspect the existing structure before drawing new boundaries.

| Observed drift | Possible enforcement | Proof |
| --- | --- | --- |
| Repeated runtime shape checks inside domain code | Parse untrusted data once; pass a validated domain type | Invalid boundary input fails; downstream callers need no repeated guard |
| UI code reaches into storage internals | A public module API plus an import restriction | A forbidden import fails; the public path works |
| Flags allow impossible combinations | Explicit states and exhaustive handling | An invalid combination cannot be constructed or fails validation |
| Suppressions hide a recurring type escape | Fix ownership or data shape; forbid the specific escape where appropriate | A negative fixture fails; supported behavior passes |
| A hot loop copies an expanding collection | A suitable data structure and a measured complexity check | Correctness holds across sizes; comparable measurements support the change |

Choose the check that fits the language and the failure. Do not force a TypeScript or Oxlint solution into another ecosystem. A stronger compiler may help a future stack decision; gardening is not permission for a language migration.

Deep modules hide meaningful work behind a small set of concepts. Consolidate a decision with its owner, not in a generic helper that every caller must configure differently. Preserve simple local code when shared infrastructure would add more rules than it removes.

Integrate the check into the repository's existing validation command and CI when that is within scope. Include a useful diagnostic: offending location, violated boundary, and the supported alternative. For existing debt, use explicit, narrow, reviewable exceptions only when authorized; do not baseline new violations silently.

Check both directions: prove the bad example is rejected and the good example stays valid. Run the behavior affected by a refactor. A new lint rule alone does not prove a migration preserved behavior.
