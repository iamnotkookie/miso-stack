# Encode lessons in structure

**Apply when:** You give the same correction a second time, or a rule depends on someone remembering it.

**Rule:** Make the mistake fail early. Choose the strongest option available. In order: a design that rules it out, a type, a lint or CI check, a test, and last, a written rule.

**Why:** A sentence can be skipped without any error. A check reports every violation.

- Prove that the check rejects a real violation and accepts a valid case.
- When the structural fix exists, delete the instruction that it replaces.
- Use [miso-garden](../../../miso-garden/SKILL.md) for the repair.
