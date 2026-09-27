---
name: miso-perf
description: "Measures and improves latency, throughput, memory, or startup behavior. Use for performance improvements, profiling, benchmark design, or repeated optimization experiments."
license: MIT
---

# Improve measured performance

Apply the shared rules and current host map in [miso](../miso/SKILL.md). A diagnosis-only request ends with evidence and a proposed experiment; it does not authorize a repair.

1. Define the user path, metric and units, input sizes, correctness contract, environment, and target. Separate cold start from warmed operation. Inspect existing benchmarks and profiling tools before creating new ones.
2. Measure the unchanged code. Save raw samples, revision or source hash, runtime version, input, concurrency, warm-up policy, and sample count. Use multiple sizes when complexity is suspected. Record resource use that could explain a faster result, such as memory or extra requests.

   Before the first optimization edit, confirm the baseline sample artifact exists and identifies the unchanged source. A saved source copy alone is not a measured baseline. If a baseline cannot run, report the prerequisite instead of starting an optimization on guessed timings. A later baseline replay can check drift, but does not replace this initial observation.
3. Trace the dominant cost with an available profiler, query plan, allocation capture, or timing probe. Distinguish time spent waiting from computation. Name the mechanism and a falsifiable hypothesis. If profiling is unavailable, state the weaker evidence and use a controlled experiment.
4. Make one meaningful change. Preserve outputs, ordering, error behavior, and required isolation. Do not replace real work with a mock, drop validation, skip results, or change the benchmark workload to claim a win.
5. Repeat the baseline and candidate under comparable conditions. Alternate their run order when drift matters. Report sample count, typical value, spread, and absolute and relative difference. Use tail percentiles only with enough observations to support them. A best run or two noisy samples cannot establish a general improvement.
6. Run correctness checks and the real user path. Inspect memory, CPU, I/O, and failure behavior relevant to the change. Keep justified gains; undo only your own unsuccessful experiment, preserving other edits. Report inconclusive results as inconclusive.

For repeated experiments, use [miso-loop](../miso-loop/SKILL.md) with a fixed workload, limits, and stop target. Recheck accepted changes together. Do not keep optimizing past the agreed outcome.

Deliver a reproducible command or existing benchmark entry, before/after samples, the mechanism, correctness evidence, and limits. Use [miso-verify](../miso-verify/SKILL.md) for app controls and evidence capture. Never invent universal latency thresholds or a performance win from source inspection alone.
