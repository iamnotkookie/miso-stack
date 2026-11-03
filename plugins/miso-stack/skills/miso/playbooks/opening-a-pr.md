# Prepare a focused pull request

Use for: Package an authorized change for review.

You own the reviewer's minute. Prefer several narrow pull requests to one large one, each landable and in an order that proves the work.

## Procedure

1. Read the repository contribution rules and its pull request template. Confirm the intended base and the complete diff.
2. Run the required checks and read the full change, including generated files and secrets. Remove leftovers: dead code, debug output, and comments that restate the line.
3. Order commits as a story: a regression test while it fails, its repair directly after, and a subtraction before a reshape. Every commit passes on its own, except that one failing test commit. Use the repository's title convention.
4. Write the description for someone already reading the diff. Explain the motive, the result, any deliberate gaps, the risks, and the commands you ran. Omit any empty section. A template takes precedence over this order.
5. Prepare commits and a branch only when authorized. Do not initialize Git or add a remote as an implicit prerequisite. Open or update the PR only within the granted publication scope. Otherwise leave the description and patch ready.
6. Verify the created PR link and head revision when publication occurred. Do not invent a URL. Do not merge.

## Supporting skills

[miso-review](../../miso-review/SKILL.md), [miso-docs](../../miso-docs/SKILL.md), [miso-verify](../../miso-verify/SKILL.md)

## Completion evidence

The review package accurately describes the full change and its executed checks.

## Reply

When published, give the link and head revision. Otherwise say that the patch is ready and where it is. Name the checks that ran and what the change leaves out.
