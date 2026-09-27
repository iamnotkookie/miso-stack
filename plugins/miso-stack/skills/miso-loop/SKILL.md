---
name: miso-loop
description: "Repeats a scoped task with verification until it succeeds or reaches a stop condition. Use for a bounded build-test-fix loop, a Ralph-style loop, or resuming and cancelling repeated work."
license: MIT
---

# Work in a bounded loop

Apply the shared rules and current host map in [miso](../miso/SKILL.md). This is a procedure run by the active agent. It does not install a stop hook, schedule a daemon, or keep a closed session alive.

## Start or resume

Keep the original task, acceptance checks, scope, and authorization stable. Use a project-local task directory for `loop.json` and evidence. Choose a fresh directory for new work; never replace another loop. Default to at most 10 iterations and 30 minutes of active work unless the user supplies limits. State the limits and proceed within existing authorization. Host and user limits take precedence.

Save the task, checks, limits, completed iteration count, elapsed active time, last evidence paths, next action, and status in `loop.json`. Status is `running`, `complete`, `blocked`, `limit-reached`, or `cancelled`. Update it after each attempt. Use the existing [plan](../miso-plan/SKILL.md) for dependent tasks rather than duplicating that ledger.

On resume, read the saved task and current files, verify the previous evidence still applies, and preserve consumed limits. A fresh session is not a fresh budget. Resume a cancelled or exhausted run only when the user requests it; obtain new limits for exhausted work. Missing state means no claimed previous progress.

## Iterate

1. Check cancellation, remaining limits, and prerequisites before another attempt. Never launch work whose known duration exceeds the remaining time. Bound external commands by the remaining time where the host supports it.
2. Inspect the current result. Choose one concrete hypothesis or unfinished acceptance condition. Make the smallest authorized change.
3. Execute its check. Record the attempt, command, expected and observed result, and resulting file changes. A failed attempt consumes an iteration too.
4. Use that evidence to choose the next action. Two consecutive attempts with no new evidence or progress stop as blocked. Do not repeat the same failure blindly, weaken the task, or edit acceptance checks to manufacture success.
5. When the checks appear satisfied, run the final relevant integration checks against the current files. Mark complete only when all required outcomes have evidence. A completion word or `<promise>` tag is not proof.

Stop immediately for cancellation or an authority boundary. Save a resumable handoff for blockers or limits; neither is completion. Cancelling stops further loop actions and any owned background work through supported controls; it does not revert user files or delete evidence.

In a host without automatic continuation, work only while the session can execute. If it ends early, checkpoint and state that the run needs an explicit resume. Do not claim a background loop is active. External schedulers or continuation hooks require a separate, supported setup and their own qualification.
