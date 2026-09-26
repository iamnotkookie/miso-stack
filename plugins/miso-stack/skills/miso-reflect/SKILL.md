---
name: miso-reflect
description: "Turns observed workflow failures into targeted improvements. Use when the user asks to reflect, review a session, or improve an existing skill."
license: MIT
---

# Reflect

Apply the shared rules and current host map in [miso](../miso/SKILL.md). When called directly, run this procedure after reading those rules. When called from a playbook, continue that playbook without restarting routing.

Use only this session or explicitly approved project history. Do not search unrelated private transcripts.

1. List concrete corrections, repeated failures, and successful recoveries, with evidence.
2. Distinguish a general problem from a one-off environmental failure. Check whether an existing rule already covers it and was simply missed.
3. Prefer a validation rule, script, schema, or better tool over another paragraph. For a trigger failure, improve the description before adding a new skill.
4. Propose the smallest repair and a behavioral evaluation that would detect recurrence.
5. Apply reversible local repairs within the user's authorized improvement scope. Changes to shared installed policy or external publication still follow project approval rules. Never infer new personal preferences or write personal memory without a direct request.
6. Run the new evaluation and the affected regression cases. Keep a failed experiment visible in the decision trail.

Return accepted changes, rejected ideas with reasons, test results, and remaining work. Do not create essays to explain a failure a tool can prevent.
