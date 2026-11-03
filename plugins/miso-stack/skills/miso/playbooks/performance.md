# Improve performance

Use for: Fix a specific measured performance problem.

You own the number. Find what limits it before you believe it, and keep only a win you can explain.

## Procedure

1. Use [miso-perf](../../miso-perf/SKILL.md). Define the workload, metric, units, environment, and acceptable outcome. Write what each result would make you do ([explain-the-number](../references/principles/explain-the-number.md)).
2. Capture a repeatable baseline with warm-up and enough samples for the expected variance. Check that the baseline measures the work, not the harness.
3. Use profiles or traces to locate the mechanism. Do not optimize from how the source looks.
4. Change one meaningful variable. Keep the benchmark conditions comparable.
5. Measure again and inspect the distribution and correctness, not only the best run. Explain why the number moved.
6. Keep a demonstrated improvement. Revert a change that shows no effect. Report regressions, noise, and limits.

## Supporting skills

[miso-perf](../../miso-perf/SKILL.md), [miso-verify](../../miso-verify/SKILL.md), [miso-review](../../miso-review/SKILL.md)

## Completion evidence

Comparable samples show an improvement without violating correctness.

## Reply

Give the main result with its unit, the sample count, the mechanism, and the earlier and later values. Report a null result plainly.
