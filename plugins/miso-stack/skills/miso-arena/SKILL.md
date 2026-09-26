---
name: miso-arena
description: "Compares independent candidate solutions against a common rubric. Use when the user asks for alternatives, competing designs, or an arena."
license: MIT
---

# Arena

Apply the shared rules and current host map in [miso](../miso/SKILL.md). When called directly, run this procedure after reading those rules. When called from a playbook, continue that playbook without restarting routing.

1. Define the deliverable and three to six observable selection criteria. Set the number of candidates and a bounded experiment. Two candidates are a useful default.
2. Read [delegation](../miso/references/delegation.md) and the current harness map. Give each candidate the same problem and constraints, with a separate output directory. Do not let one candidate see another's answer before it finishes.
3. Use the harness default model unless project configuration supplies an available alternative. Do not claim model diversity when all candidates use the same model.
4. Run independent workers only when permitted and available. Otherwise create sequential candidates and disclose the reduced independence.
5. Evaluate candidates against the declared rubric and executable checks. A separate reviewer helps when available. Resolve reviewer claims by inspecting artifacts, not voting.
6. Pick a base. Transfer only the useful, compatible parts of other candidates. Verify the combined result again.

Return a comparison table, the chosen base, proof, and remaining tradeoffs. Keep losing artifacts until their useful evidence has been recorded. Deleting them requires the applicable approval.
