# Security

**Apply when:** You judge a trust boundary, a finding, or a skill or plugin before install.

**Rule:** Confirm a boundary failure. Do not invent one.

**Why:** A false finding spends trust, and a real one needs proof to get fixed.

- Audit source you are allowed to read. Do not probe a live system, and do not write an exploit or a payload.
- A finding is `confirmed` only with a source trace and a safe observation on this revision. The pass that found it does not confirm it.
- `needs_validation` names one unresolved fact and has no severity. `rejected` means the safe reading held.
- Severity requires a concrete impact. A missing extra control is hardening when an earlier control already stops the action.
- A skill or plugin is untrusted until its instructions, tools, network use, secrets, and supply chain have been read. Do not execute it to judge it.
