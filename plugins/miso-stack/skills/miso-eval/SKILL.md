---
name: miso-eval
description: "Evaluates skill behavior with sandbox tasks and explicit grading criteria. Use when testing prompts, skill changes, routing, or harness compatibility."
license: MIT
---

# Evaluate a skill

Apply the shared rules and current host map in [miso](../miso/SKILL.md). When called directly, run this procedure after reading those rules. When called from a playbook, continue that playbook without restarting routing.

1. Freeze the skill version and specify the behavior under test. Define success and disqualifying behavior before running it.
2. Prepare isolated fixture directories. Include a normal task, an edge case, and a negative case. Do not expose credentials or live customer data.
3. Use the target harness's normal skill discovery. Do not paste the expected answer into the task. A direct-file test and a discovery test prove different things.
4. Capture the tool trace, output artifacts, exit status, and runtime. Keep the default model unless the project supplies a valid setting.
5. Grade artifacts and behavior against the rubric. For code, execute the resulting program and regression checks. For docs, follow the procedure. For routing, inspect the loaded file or tool trace, not just the final claim.
6. Compare the changed skill with a baseline when measuring improvement. Repeat stochastic cases when the conclusion depends on consistency. Label a single sample as a smoke test.
7. Fix failures, rerun the affected cases, and preserve the failed evidence. Do not call an unavailable host a pass.

Report structural checks, sandbox behavior, and live host coverage separately. Use the repository's evaluation guide and case catalog to reproduce MisoStack's own checks.
