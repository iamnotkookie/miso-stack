---
name: miso-automate
description: "Designs bounded engineering routines and handles issue reports with reproduction evidence. Use when drafting a recurring check, triaging a report, or automating a proven workflow."
license: MIT
---

# Automate proven work

Apply the shared rules and current host map in [miso](../miso/SKILL.md). When called directly, run this procedure after reading those rules. When called from a playbook, continue that playbook without restarting routing.

1. Run the manual workflow successfully before scheduling it. Identify the trigger, input source, owner, allowed actions, limits, deduplication key, and completion evidence.
2. For issue reports, restate the reported behavior and expected result. Search for an existing report. Reproduce through the app's verification driver. Separate reproduced, insufficient evidence, and inaccessible cases.
3. Fix only when the user authorized fixes. Verify the original report and nearby behavior. Draft any reply or issue update until sending it is authorized.
4. Define overlap prevention, retry limits, failure reporting, and how to disable the routine. A missed prerequisite must produce a visible failure, not an endless retry loop.
5. Use the current harness's actual scheduler or an explicitly chosen external scheduler. Without one, deliver a runnable command and a schedule specification marked inactive. Do not invent a cloud agent, webhook, or bot service.
6. Test a sample event, a duplicate, a failure, and a disabled run in a sandbox. Show which external actions were simulated.

Automatic deployments, deletion, and messages remain approval-gated. A request to draft a routine does not activate it. Native Grok Bot UI and Cursor cloud hosting are outside MisoStack's four-host scope.
