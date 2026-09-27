# Improve performance with evidence

Use this guide when you have a slow user path or a measurable resource problem. You need a repeatable workload and access to the runtime that exhibits it.

## State the outcome

```text
Use miso to reduce report generation time on this dataset.
Preserve row order, validation, and error behavior.
Capture a baseline, identify the dominant cost, and verify the change.
```

Miso selects `miso-perf`. It should establish the metric, units, input, environment, and correctness checks before changing code. If you only want diagnosis, say “stop before modifying the app.”

## Check the baseline

Expect more than one timing. The baseline should identify the runtime, input size, concurrency, warm-up policy, and number of samples. Cold startup and warm requests answer different questions; keep their measurements separate.

For suspected growth problems, test several input sizes. For example, doubling a collection may expose repeated scanning that a tiny fixture hides. Run a profiler or a controlled probe to connect the measurement to a mechanism.

## Compare the same work

The candidate must process the same inputs and produce the same required outputs. A benchmark that removes validation, skips records, or substitutes a mock measures another task.

Expect raw samples and a summary of typical time and spread. Alternating baseline and candidate runs can expose environmental drift. Tail percentiles need enough samples to be useful. A single fast run is not proof.

Check related costs. Lower latency may use more memory, more queries, or more CPU. The report should make that tradeoff visible and run correctness checks against the changed code.

## Bound repeated experiments

```text
Use miso to improve startup time with at most four experiments and 20 minutes.
Keep the workload fixed. Stop when the agreed target is verified.
Preserve raw samples and explain any inconclusive result.
```

Miso combines performance verification with the bounded loop. It keeps supported improvements and stops at the target or limits. Rejected experiments must not erase your unrelated changes.

For browser and desktop captures, use the project's control tool. See [verification tools](../guides/01-verification.md). For resumable loops, see [long-running work](../guides/03-long-running-work.md).
