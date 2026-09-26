# Prepare and ship an approved change

Use for: Verify a release or merge candidate before an authorized external action.

## Procedure

1. Identify the exact revision, destination, release scope, and authorization.
2. Review code, required checks, dependencies, migrations, and rollback instructions.
3. Verify the artifact that would be released. Recheck the head after any change.
4. For a stack, verify dependency order and only the contiguous ready portion.
5. Require approval before deployment, force-push, or another project-gated action. Prepare the reviewable result first.
6. If authorized, perform the action and verify the remote outcome. Otherwise leave the candidate ready and record the gate.

## Supporting skills

[miso-review](../../miso-review/SKILL.md), [miso-verify](../../miso-verify/SKILL.md), [miso-trail](../../miso-trail/SKILL.md)

## Completion evidence

The exact candidate is verified and the remote outcome is confirmed only if an authorized action ran.
