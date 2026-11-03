# Structure

**Apply when:** A change makes the next change less local.

**Rule:** Shape the code so the next change stays local. Apply the rule that the change actually breaks.

**Why:** A tidy diff can still rot the system. Maintenance costs more than the first build.

- **DRY.** One business rule has one representation. Two copies will disagree.
- **KISS.** A reader follows the change without a tour. Clever loses to clear.
- **YAGNI.** Build the behavior that a current requirement or failing test names.
- **Single responsibility.** A module changes for one reason.
- **Open-closed.** Extend a tested seam. Do not reopen it for a case the seam already absorbs.
- **Substitution.** A subtype honors the parent contract.
- **Interface segregation.** A caller depends only on the operations it uses.
- **Dependency inversion.** Inject the concrete client, database, or clock at the edge.
- **Separation of concerns.** UI, domain, and storage do not share a module.
- **Generality** waits for the second real case. **Incrementality** means a thin slice with a check.
- **Reliability** means a named failure, a retry budget with jitter and a stop, and backpressure on a stream.
