# Fix a defect

Use for: Reproduce and repair incorrect behavior.

## Procedure

1. Use [miso-debug](../../miso-debug/SKILL.md) to build a precise failing signal, minimize it, and test the cause. State expected and reported behavior. Reproduce the problem on the user-facing surface before changing code.
2. Save the failing command, input, and output. If the environment prevents reproduction, record that limit and avoid claiming a confirmed fix.
3. Trace the cause with targeted instrumentation. Reject hypotheses that conflict with observed behavior.
4. Write a regression test first when a practical path exists. Apply the smallest change that addresses the demonstrated cause.
5. Repeat the original reproduction on the same surface and run relevant regression checks.
6. Review the change and report cause, fix, failing proof, passing proof, and residual limits.

## Supporting skills

[miso-research](../../miso-research/SKILL.md), [miso-tdd](../../miso-tdd/SKILL.md), [miso-verify](../../miso-verify/SKILL.md), [miso-review](../../miso-review/SKILL.md)

## Completion evidence

The original failing path now passes, with before-and-after evidence.
