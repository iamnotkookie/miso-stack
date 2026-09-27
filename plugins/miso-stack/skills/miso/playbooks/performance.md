# Improve performance

Use for: Fix a specific measured performance problem.

## Procedure

1. Use [miso-perf](../../miso-perf/SKILL.md). Define the workload, metric, units, environment, and acceptable outcome.
2. Capture a repeatable baseline with warm-up and enough samples for the expected variance.
3. Use profiles or traces to locate the mechanism. Avoid optimizing from source appearance alone.
4. Change one meaningful variable. Keep the benchmark conditions comparable.
5. Measure again and inspect distribution and correctness, not only the best run.
6. Keep a demonstrated improvement. Report regressions, noise, and limits; do not claim a win from inconclusive data.

## Supporting skills

[miso-perf](../../miso-perf/SKILL.md), [miso-verify](../../miso-verify/SKILL.md), [miso-review](../../miso-review/SKILL.md)

## Completion evidence

Comparable samples show an improvement without violating correctness.
