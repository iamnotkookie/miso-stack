# Working with agents

**Apply when:** An agent writes, reviews, or configures the change.

**Rule:** Humans own intent, architecture, and verification. Agents own generation and mechanical edits.

**Why:** An agent produces plausible work at any speed, so verification sets the real pace.

- The spec, the acceptance criteria, or the failing test is the source of truth. The diff is a projection of it.
- Context files are code. Keep them short. Add a rule after the same mistake repeats.
- The writer of a change does not approve it. Review runs in a fresh context against the spec and the artifact.
- Agent output is untrusted until the gates a human change must pass are green on that revision.
- Use the tool that fits the job, including a non-model tool.
- Measure defects, revert rate, and time to a verified change. Do not score token use.
- Commit a verified slice the author can explain.
