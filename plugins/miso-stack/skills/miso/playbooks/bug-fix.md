# Fix a defect

Use for: Reproduce and repair incorrect behavior.

You own the cause. Each line you ship needs an observation behind it. An untested "maybe this helps" stays out of the diff.

## Procedure

1. Use [miso-debug](../../miso-debug/SKILL.md). State the expected and reported behavior. Reproduce the problem yourself on the user-facing surface before you change code. Ask the user only for something your tools cannot reach, and only after you drive them as far as they go.
2. Save the failing command, input, and output. If it does not reproduce, tighten the conditions or add instrumentation. If evidence shows that the report or the requested fix is wrong, show the evidence and stop ([attack-the-premise](../references/principles/attack-the-premise.md)). If the environment prevents reproduction, record that limit and claim no confirmed fix.
3. Cut the problem space. List the candidate causes, take the probe that rules out the most, and read the runtime result. Add targeted instrumentation instead of guessing. Confirm the surviving mechanism before you plan the fix.
4. Write a regression test first when a cheap path exists. Apply the smallest change that the evidence justifies. When a test disproves your theory, undo the edits that the theory led to ([fix-root-causes](../references/principles/fix-root-causes.md)).
5. Repeat the original reproduction on the same surface and run the relevant regression checks. An inconclusive result does not count. Neither does a check on a different surface.
6. When commits are authorized, commit the regression test first, while it fails, and the repair directly after it, so the history shows both states. Review the change.

## Supporting skills

[miso-research](../../miso-research/SKILL.md), [miso-tdd](../../miso-tdd/SKILL.md), [miso-verify](../../miso-verify/SKILL.md), [miso-review](../../miso-review/SKILL.md)

## Completion evidence

The original failing path now passes, with before-and-after evidence.

## Reply

State the cause, the fix, and how you verified it. Paste the failing output and the passing output verbatim. Name what remains unverified.
