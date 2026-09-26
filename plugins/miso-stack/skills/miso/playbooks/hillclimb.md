# Improve a metric repeatedly

Use for: Run a bounded series of measured experiments.

## Procedure

1. Define the target metric, workload, correctness constraints, and stopping limit.
2. Capture a baseline and measurement noise. Select the first falsifiable hypothesis.
3. Make one isolated change and run comparable measurements.
4. Retain only a justified improvement. Restore only your own failed change without discarding user work.
5. Log the hypothesis, result, and decision. Continue with a different hypothesis while the run remains productive and within limits.
6. Recheck accepted improvements together. Report the final result, variance, and remaining gap.

## Supporting skills

[miso-plan](../../miso-plan/SKILL.md), [miso-trail](../../miso-trail/SKILL.md), [miso-verify](../../miso-verify/SKILL.md)

## Completion evidence

Each accepted experiment has comparable measurements and the final result passes correctness checks.
