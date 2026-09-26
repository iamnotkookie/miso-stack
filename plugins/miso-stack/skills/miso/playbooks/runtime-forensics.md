# Diagnose a live runtime

Use for: Investigate leaks, CPU use, or intermittent behavior without assuming a fix.

## Procedure

1. Identify the process, build, ownership, workload, and symptom.
2. Check that instrumentation targets the intended instance. Keep measurement overhead visible.
3. Capture logs, profiles, lifecycle events, or resource counts while reproducing the symptom.
4. Correlate the observation with source paths and competing mechanisms.
5. Run a discriminating probe if safe. Preserve the raw evidence.
6. Return the diagnosis and confidence. A diagnosis request does not authorize an unrelated repair.

## Supporting skills

[miso-research](../../miso-research/SKILL.md), [miso-verify](../../miso-verify/SKILL.md)

## Completion evidence

Captured runtime observations support the diagnosed mechanism or a bounded set of hypotheses.
