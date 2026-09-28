---
name: miso-tdd
description: "Uses a failing behavioral test to guide a small implementation change. Use when TDD is requested or a bug has a practical regression-test path."
license: MIT
---

# Test-driven change

Apply the shared rules and current host map in [miso](../miso/SKILL.md). When called directly, run this procedure after reading those rules. When called from a playbook, continue that playbook without restarting routing.

1. State the behavior from the caller's point of view. Find the closest existing test harness.
2. Reuse an existing regression test if it already exposes the missing behavior. Otherwise write the smallest useful test. Use a fixed expected result, not a copy of the implementation. Keep real dependencies when safe and practical.
3. Run the test against the unchanged implementation. Confirm it fails for the expected reason. A syntax error or missing dependency is not the required red result.
4. Make the smallest implementation change that passes the behavioral test.
5. Run the test, then the relevant existing suite. Refactor only while checks stay green. Refactor is where DRY, KISS, and a single responsibility land. Red and green add nothing the current test does not demand. See [structure](../miso/references/principles.md).
6. Use [verification](../miso-verify/SKILL.md) for the reported user path when the unit test cannot cover it.

If the test path is unavailable, record the reason and use a reproducible runtime experiment. Do not present that as a completed red-green cycle. Avoid new tests for trivial prose edits or tests that only assert source spelling.
