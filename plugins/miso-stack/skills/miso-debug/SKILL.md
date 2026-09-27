---
name: miso-debug
description: "Diagnoses bugs and performance regressions with a reproducible failure and controlled experiments. Use for broken, intermittent, or unexpectedly slow behavior."
license: MIT
---

# Debug

Apply the shared rules and current host map in [miso](../miso/SKILL.md). When called from a workflow, continue that workflow without restarting routing.

Read relevant project context and decisions. Separate diagnosis from repair: a request to investigate does not authorize a code fix.

1. Build one repeatable command that detects the user's exact symptom. Use the existing test, real CLI, HTTP call, browser interaction, replay, or an isolated driver. Assert the wrong result, not just whether the process crashes. Read enough code to locate the path; do not settle on a cause before a failing signal exists.
2. Run the unchanged system and record the result. Minimize the input and setup one change at a time, retaining the failure. Control time, seeds, data, and network where practical. For an intermittent defect, record attempts and failures; absence in one run is not a fix.
3. List plausible causes with a prediction that would distinguish each. Rank by the observations. Do not manufacture several hypotheses when the cause is already demonstrated.
4. Test one prediction at a time. Prefer a breakpoint or narrow instrumentation. Tag temporary logs so they can be removed. For slowness, compare a measured baseline or profile; do not infer a performance win from code size.
5. When repair is authorized, use [miso-tdd](../miso-tdd/SKILL.md) at the public boundary that reaches the actual defect. Apply the smallest cause-level fix. Re-run the minimized check, original scenario, and relevant existing checks.
6. Remove instrumentation that this investigation introduced. Preserve useful reproduction artifacts in the agreed temporary directory. Verify the result after cleanup.

If no reproducible signal is available, report the attempted commands and missing condition. You may present evidence-backed hypotheses, clearly marked unproven. Do not claim a cause or start speculative fixes. Never add production instrumentation without authority. Keep secrets out of commands and saved output.

Return the observed failure, discriminating experiment, cause or remaining hypotheses, and before/after proof. For performance, include comparable sample conditions and variability.
