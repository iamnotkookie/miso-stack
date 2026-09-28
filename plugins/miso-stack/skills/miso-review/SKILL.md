---
name: miso-review
description: "Reviews correctness, security, change impact, and code quality against evidence. Use for code review, adversarial review, blast-radius analysis, or final quality checks."
license: MIT
---

# Review

Apply the shared rules and current host map in [miso](../miso/SKILL.md). Read [structure](../miso/references/principles.md) before judging design. When called directly, run this procedure after reading those rules. When called from a playbook, continue that playbook without restarting routing.

## Written round

A code review is one written round. Approve when the change improves the health of the code, even if it is imperfect. Withhold approval when the change is incorrect, unsafe, untrustworthy, or makes the codebase worse. A nit never blocks. Approving does not merge.

1. Recover intent from the title, the description, the linked ticket, and the discussion that pointed at the review. Reject early, with one alternative, when the change should not land.
2. Record the tip SHA. Read the full diff and the existing threads.
3. Prove gates on that SHA: pipeline URL and status, mergeability, approvals, open blockers. Do not call an unknown gate green. Skip notes a formatter or linter already owns.
4. When the description says the issue is already fixed, or that this change replaces another, check the default branch and the other change. The same tip on another open change changes the verdict.
5. Above about 400 changed lines, review design and name a split. Above about 1000, do not review line by line. Require a split.
6. Judge the main design first. Send design notes and stop the round when the design is wrong. Naming and polish wait. Follow [comment style](references/comment-style.md). Keep the round at 20 notes or fewer. One sincere `praise:` when something is genuinely good.
7. Choose `approve`, `request changes`, or `hold merge`. Hold means the code is acceptable and the merge waits on a parent, a conflict, or a red gate that is not this diff.
8. Publish the summary and inline notes on the pull request before the chat reply. On approve, submit the host approval and do not merge. If the tip moved after an earlier approval, review the new tip before approving again. Do not message the author unless the user asked in this turn.
9. Tell the user in one short note: verdict, URL, tip SHA, what the change does, what blocks merge, and what was posted. No em dash.

A thread that links several open changes is a pack. Review each open change still in scope. Skip a closed change unless the survivor absorbed it. One chat note for the pack. Publish on each change.

1. Fix the scope to a revision or explicit file set. Read the intended behavior and repository rules before the diff.
2. Trace changed contracts beyond direct callers. Include serialization, data migrations, configuration, permissions, background tasks, teardown, and old consumers when relevant.
3. Identify the assumption on which safety depends. Try to falsify it with the real code. Distinguish a proven defect from an untested hypothesis.
4. Inspect input validation, authorization, secret handling, error exposure, injection risks, and destructive operations. Use existing scanners where available. Report tools that could not run. A repository audit, or a question about installing a skill, is [miso-audit](../miso-audit/SKILL.md). On this diff, apply [security](../miso/references/principles.md).
5. Check unnecessary layers, dead code, hidden mutation, duplicated state, misleading comments, and suppressed checks. Keep comments that explain a real constraint the code cannot express. Do not delete license notices.
6. For TypeScript, read [type review](../miso/references/typescript.md). For broad changes, partition review lenses with [swarm](../miso-swarm/SKILL.md) if permitted. Reviewers inspect independently; the lead validates findings.
7. A review request is read-only. Fix findings only when the user also requested repairs or implementation. In that case, fix accepted findings within scope and rerun affected checks. Do not change expected results just to make a failing test pass.

## Choose the review mode

- **Code review:** compare separately against repository standards and the requested behavior. Pin a supplied base to a commit and capture the intended diff, including working-tree edits if requested. For branch changes, use the merge base. Report missing standards or spec sources instead of inventing them. Distinguish a concrete violation from a design heuristic. Keep standards findings and requirement findings separate so one cannot hide the other.
- **Impact:** identify the safety assumption, trace indirect consumers, and run the real dependency or app path that could disprove it. Read the pinned dependency version and local patches. Report confirmed risks, cleared risks, and unproven assumptions separately. A caller list alone is incomplete.
- **Challenge:** use the same intent, revision, context, and rubric for independent reviewers when permitted. Use project model configuration or host defaults; never invent model diversity. With no delegation, disclose a serial review. Validate each finding against source or a probe, deduplicate, and explain disagreements. Agreement is a lead, not proof. Classify findings as fix now, consider, or dismissed with reasons. Return a verdict without auto-applying edits.
- **Comments:** use [the comment review](references/comments.md) for requested cleanup of comments, suppressions, and workarounds. This is not a command to remove every comment.

Report actionable findings first. Each needs severity, a concrete trigger, impact, source location, and evidence or an explicit uncertainty label. State what was reviewed and what was not. No findings is a result, not proof of perfection.
