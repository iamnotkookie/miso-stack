---
name: miso-author
description: "Creates or improves compact skills from stated requirements and evaluated examples. Use for skill authoring or capturing an explicitly stated working preference."
license: MIT
---

# Author a skill

Apply the shared rules and current host map in [miso](../miso/SKILL.md). When called directly, run this procedure after reading those rules. When called from a playbook, continue that playbook without restarting routing.

1. Check the existing catalog for the capability. Prefer improving one skill over adding a near duplicate.
2. Gather the target task, explicit preferences, success criteria, and counterexamples. Use supplied history only within its authorized scope. Never turn a one-off instruction into a permanent preference without evidence of intent.
3. Write a short SKILL.md with a matching lowercase directory name, a specific description, and a concrete procedure. Put occasional detail in reference files. Use executable tools for deterministic checks.
4. Keep harness names and model IDs out of shared procedure text. Read the host map before delegation. Test relative paths after installation, not only in the source checkout.
5. Add positive, negative, and ambiguous prompts to an evaluation. Use [miso-eval](../miso-eval/SKILL.md) to run the skill in a sandbox. Include a case where the skill must decline scope or state a missing capability.
6. Verify the complete output, then repair the smallest cause of failure and rerun affected cases. Preserve third-party notices if material is adapted.

Use [miso-docs](../miso-docs/SKILL.md) for the user-facing guide. A parsed frontmatter block is only structural validation; label behavior unverified until exercised.
