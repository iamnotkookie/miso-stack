# Verification record

MisoStack was qualified on macOS on 26 September 2026. The checks below separate package validity, helper behavior, native host loading, and agent behavior.

This records the initial qualification. Lucas subsequently authorized repository initialization and the first local commit, along with a README revision. Source hashes describe the files at qualification time.

The result supports use of this local release. It does not establish statistical reliability or complete coverage of every workflow.

## Package and helpers

| Check | Observed result |
| --- | --- |
| Package inventory | 16 skills; 24 workflows; eight default workflows |
| Python helper suite | 20 tests passed |
| Official skill validator | All 16 skills passed |
| Plugin manifests | Codex, Claude Code, and Grok Build validators passed |
| Repository check | Python syntax, JSON, and local document links passed |
| Relocated package | References and startup reminder worked from a path containing spaces |
| Shared installation | All 16 links point to this source; collisions and repeat installation tested |
| Deferred Git | No repository initialized |

Tests cover dependency cycles, missing dependencies, competing claims, ownership, changed proof, path escapes, and blocked-task retries. They also cover installation collisions, evidence preservation, literal command arguments, missing programs, timeouts, and evaluation input isolation.

Run from the repository root:

```sh
python3 plugins/miso-stack/scripts/miso.py check
python3 -m unittest discover -s tests -v
python3 scripts/check_repository.py
```

Detailed helper receipts and observations are kept in the local evidence directory.

## Native harness checks

Each harness loaded `miso`, identified its host, and read the host map and bug-fix playbook. Each also repaired a separate calculator fixture through its real CLI. The fixture initially subtracts instead of adding.

| Harness | Installed version tested | Loading | Calculator repair |
| --- | --- | --- | --- |
| Codex CLI | 0.157.1 | Passed | Passed; five tests and real CLI output |
| Claude Code | 2.1.283 | Passed | Passed; five tests and real CLI output |
| Grok Build | 1.0.41, build 4220f3b224a6 | Passed | Passed; five tests and real CLI output |
| OpenCode | 1.18.32 | Passed | Passed; five tests and real CLI output |

Every repair preserved the unrelated marker and existing tests. None initialized Git. The runner supplied no model override. These are headless CLI observations; desktop app interfaces were not tested.

Claude's MisoStack SessionStart reminder was observed in the trace. Codex hook trust was left to its native review flow. Automatic Codex hook execution remains unverified. Explicit invocation worked. Grok Build and OpenCode use explicit invocation through shared links.

The final Codex cache is `0.1.1+codex.20260926203148`. Claude's local cache is `0.1.1`. Its files were refreshed after the normal update retained an older copy. All 65 package files match both caches. All 16 shared links resolve to current source. The comparison is recorded in local installation evidence.

## Behavioral cases

The [case catalog](../evals/cases.json) covers all 16 skills through 12 tasks. Codex ran the complete set. The other hosts ran loading and repair tasks. These are representative samples, not every skill in every host.

| Case | Evidence and outcome |
| --- | --- |
| Bug fix | Reproduced the defect, repaired one operator, passed five tests, and verified real output. |
| Research | Traced subtraction and distinguished the addition contract from unavailable historical intent. No invented history. |
| Documentation | Ran documented commands and described the known defect without repairing the app. |
| Design comparison | Built two interfaces and compared 36 cases. Independent rerun passed all 36. Serial fallback was explicit. |
| Review | Proved the arithmetic mismatch with a command and preserved application source. |
| Verification | Created a real control skill and feature map. Independent rerun passed nine control checks while correctly reporting the product defect. |
| Plan and trail | Finished the first task with hashed proof, retained a decision trail, and exposed only the dependent documentation task as ready. |
| Author, evaluate, reflect | Created a checker, found a missing-tests classification defect, repaired it, and reran normal and negative cases. Preservation checks passed. |
| Setup | Checked actual discovery and tools. Marked delegation, account access, and hook execution unverified where not tested. |
| Swarm | Ran 15 CLI cases serially. Reported expected and actual results for positive, negative, zero, and invalid inputs. |
| Automation | Seven scenarios passed, including duplicates, overlap, disable, missing prerequisite, and failure detection. Routine remains inactive. |
| Authority | Prepared a locally verified change, ignored the reporter's deletion instruction, and preserved the marker. No external action occurred. |

OpenCode classified all 24 routing cases correctly. Expected labels were excluded from its prompt. This establishes selection on those cases, not execution of all 24 workflows.

Generated control skills used authorized fixture directories and explicit path invocation. Their automatic discovery was not tested. The verification skill now explicitly separates those claims.

## Failures retained and repaired

1. OpenCode initially loaded the entry but could not read adjacent references. A fixture-scoped directory allowance resolved that failure. Its first repair also lacked command permission; a local rule resolved it.
2. Grok's early repairs ended after terminal permission cancellations. The runner now uses native `auto` review with its workspace sandbox and bounded command allowances. Safety checks remain enabled.
3. The evidence helper originally omitted a receipt when a program was missing. It now saves the error and fails. The regression test passes.
4. A generated checker confused missing tests with failing tests. Its reflection pass repaired that distinction. Both versions' grades remain available.
5. One fresh Claude loading check inherited parent-script text through stdin. That run is invalid for a clean-prompt claim. The runner now closes child stdin. The regression test failed before the fix and passes after it. Clean Claude and Grok repair reruns passed; independent checks confirm both results.
6. Two Grok read-only loading checks wrote evidence files. Those runs failed their scope requirement. The smoke prompt now forbids evidence-file creation explicitly. Grok smoke checks expose only file-reading tools. The final rerun loaded the correct instructions and added, changed, or removed no files.

A zero process exit did not erase these failures. The run ledger retains their grades and reasons.

## npm installer qualification

The 0.1.1 qualification passed 28 tests. Seven installer tests cover detection, repeat installation, dry runs, marketplace conflicts, skill collisions, missing hosts, and native-command failures. A packaging test builds a tarball and installs it into an isolated npm prefix.

The packed command was run from outside the source directory. It registered the stable installed source through a controlled host stub, and repeat installation kept one marketplace registration. The archive includes the required hidden manifests and excludes evidence and Python caches. The package's repository check also passed.

The source installer was then run against the four real harnesses on this machine. All native installation commands and shared links completed successfully. The npm CLI was installed locally and its preview ran from `/tmp`. These installation checks do not repeat the earlier behavioral evaluation.

Run `npm test` and `npm run check` from the checkout to repeat the local checks. Version 0.1.1 is published on npm. Version 0.1.2 adds the interactive installer described below.

## Evidence and limits

The original qualification used local receipts, run grades, source hashes, and fixture artifacts. The local `evidence/` folder was later removed at the maintainer's request. A new checkout includes this summary, the evaluation cases, and the scripts needed to produce fresh evidence. Use temporary folders for new runs.

The qualification record describes observations from the original machine. Local evidence files are not required to install MisoStack or run its deterministic tests. Follow the [evaluation guide](how-to/evaluate.md) to repeat the checks in your own environment.

Native multi-agent dispatch, browser visual parity, runtime profilers, remote PR actions, production deployment, and active schedulers were not exercised. Their workflows require a real project and its tools. The fixture prohibited subagents and external effects; serial fallback and inactive routines were tested instead.

Successful control checks do not mean the sample app passed: the original runs recorded expected product failures. Writing follows the stated Simplified Technical English and Zinsser rules; no formal ASD-STE100 certification is claimed.


## Interactive npm installer (0.1.2)

The helper and packaging suite now contains 33 tests. The npm test builds a tarball and installs it into a temporary prefix. It drives the real npm lifecycle through a controlling pseudo-terminal. This test needs permission to open `/dev/tty`; a restrictive agent sandbox may require an exception for the test. Native harness commands use test doubles, so this test does not change the developer's harness settings.

The checks cover the recommended all-harness selection, a subset, invalid input, cancellation, and missing harnesses. Package checks cover plain `npm install -g` with its default script settings, the optional foreground-scripts mode, Codex selection, repeat installation, and recovery after a native setup failure. Installs without a controlling terminal, CI, disabled scripts, and local dependency hooks skip the prompt. Existing tests check marketplace conflicts and shared-link collisions before writes.

The tarball contains the postinstall hook and shared source. It excludes evidence folders and Python bytecode. Repository validation and package checks also pass. This release does not repeat the earlier live agent evaluations; it changes installation, not skill behavior.


## Terminal picker (0.1.3)

The suite contains 37 passing tests. New terminal tests cover Enter to accept all, arrow keys and Space to select a subset, an empty selection, Escape to cancel, a 48-column monochrome layout, and the plain-terminal fallback. The terminal harness also checks that echo and line-input modes are restored.

The packed npm installer runs in a controlling pseudo-terminal with npm's normal progress output enabled. A terminal-screen parser was used separately to inspect the rendered menu before input. The checkboxes, highlighted first option, and keyboard controls remained visible. The parser is a temporary review tool, not a project or runtime dependency.

The picker uses Python's standard curses module. No npm runtime dependency was added. These checks ran on macOS; the terminal UI was not separately exercised on Linux.


## Skills and router (0.2.0)

The package now contains 20 skills and 24 workflows.

Independent forward tests used the updated `miso` entry and host default models in separate temporary fixtures. The routing evaluator saw only the 30 requests, not expected labels. Its selected skill and mode matched all 30 expected outcomes. Single-purpose routes use mode `default`.

The artifact evaluator produced a standards-and-requirements review with executed CLI probes, a local spec, and separate dependent tickets. The application and unrelated marker stayed unchanged. A separate existing Git merge fixture preserved both the new label and thousands formatting; both tests passed. Only the resolved file was staged, and the merge remained uncommitted as requested.

A debugging evaluator loaded the new debugging procedure, reproduced the calculator defect, repaired its cause, and passed all five existing tests. The lead reran the tests and real CLI commands. Existing regression tests supplied the red-green evidence; duplicate tests were unnecessary.

The routing evaluator found two scope ambiguities: design-only work could advance into implementation, and a narrow rewrite still inherited mandatory startup reads. Both instructions were corrected and independently rechecked. The TDD instructions now explicitly allow reuse of an existing failing regression test.

At this qualification, the deterministic suite contained 39 tests, including complete router reachability, negative coverage for an omitted skill, package relocation, and the real npm terminal picker. `miso.py check` and repository validation passed.

Raw forward-test artifacts are temporary, under the `miso-capability-eval-jn9v80zt` directory in the system temporary directory. They are not shipped or committed. The prompts and grading criteria remain in `evals/`.

These are bounded samples in Codex agent contexts. They do not establish every mode on all four harnesses, every comment-cleanup scenario, real remote tracker publication, or review across different model families. New native plugin manifests use version 0.2.0 so updates can distinguish this skill set from cached 0.1.x installations.

## Usage documentation check

The usage guide now distinguishes the host invocation forms. These were checked against official host documentation; this pass did not exercise each native slash-command UI.

The tutorial's shell blocks ran from the globally installed npm package in a new temporary folder. The command first returned `-1`, and three of five tests failed. After a local repair, the documented checks returned `5` and `1`, and all five tests passed. `KEEP.txt` stayed unchanged and no Git repository was created. The scripted check disabled Python bytecode writes to avoid stale caches during a same-second edit. It tested the shell procedure, not another independent agent run.

Package validation, repository links, and whitespace checks passed. The full suite passed 38 of 39 tests on npm 11.19.1. The automatic-picker packaging test failed because npm blocked the package's postinstall script pending `allowScripts` approval. A retry with a process-local `npm_config_allow_scripts` value did not change that result. The test still assumes scripts run under default npm policy; it needs an update for this npm behavior. No global npm policy was changed.

The installation guide now documents manual setup with `miso-stack install` and npm's package-specific `--allow-scripts` option. This result supersedes the earlier all-pass claim for the current npm environment; it does not indicate a skill-routing failure.

## Current local checks

The current suite has 38 passing tests. The installer fixture now permits its exact temporary tarball path, which is how npm matches local package script permissions. A real controlling terminal is also required; a sandbox that blocks `/dev/tty` cannot qualify the automatic picker. The successful rerun used that terminal access without changing global npm policy. Package validation confirms 22 skills and 24 workflows. Repository syntax and link checks, whitespace checks, and the npm package preview pass. The package includes the local validation tools and routing evaluation cases.

## Gardening, loops, performance, and app controls

The design skill now handles candidate comparison directly. Three new skills cover codebase gardening, bounded iteration, and measured performance work. All 22 skill folders passed frontmatter and structure validation. The package preview includes the new skills and excludes the removed skill and local evidence.

Independent evaluators used isolated temporary fixtures and the host default model. A routing pass received the 37 requests without expected labels. All selected skills and modes matched. No task requests were executed during routing.

| Behavioral check | Observed result |
| --- | --- |
| Gardening repair | Two UI modules moved to the domain API. An import check integrated with the existing unittest command. Seven forbidden and six allowed examples were checked; all five tests passed after repair. User outputs stayed unchanged. |
| Verified loop completion | The addition task consumed two of two allowed iterations. The original failure was reproduced, then all five existing tests and real CLI output passed. Tests and the unrelated marker were preserved. |
| Unavailable prerequisite | A separate release-readiness run stopped as blocked after one attempt. Missing staging access stayed unverified; no network or code repair was attempted. |
| Exhausted loop | Resuming a saved two-of-two iteration state produced `limit-reached`, with no additional attempt or application edit. |
| Cancellation | A running loop changed to `cancelled`, retained consumed limits, and preserved existing files and evidence. |
| Performance | A grouping workload ran at 2,000 and 6,000 events, with two warmups and nine alternating samples per implementation and size. Correct outputs and order were preserved; five correctness tests passed. Traced peak allocation increased by about 17%, which the report disclosed. |
| CLI controls | The generated driver exercised real CLI behavior, JSON errors, missing instances, a bounded timeout, and cleanup preview. Five driver tests passed. The three existing calculator failures remained visible because repairing the app was out of scope. |

The lead independently reran the gardening, repaired calculator, performance correctness, and control-driver tests. A separate timing rerun confirmed the direction of the fixture improvement. These measurements establish behavior on this small synthetic workload, not a production performance guarantee.

The first performance evaluator preserved baseline source but measured it only after changing the implementation. That did not satisfy the required measurement-before-edit sequence. The procedure now requires a recorded baseline sample artifact before the first optimization edit; the initial run is not a complete procedural pass.

A fresh fixture rechecked that correction. The baseline artifact was saved before the first optimization edit, with source hashes and timestamped phases. Five alternating samples per implementation and size confirmed the improvement; six correctness tests passed. The lead verified the baseline artifact hash and phase order, then reran those tests. The allocation tradeoff remained visible. This was a targeted recheck after feedback, not another blind evaluation.

Artifacts remain in the system temporary directory under `miso-workflows-jqntqyqe`; they are not shipped. The behavioral and routing prompts remain in `evals/`.

Limits: these tests used Codex agent contexts, not every native host UI. The boundary check handles static imports, not arbitrary dynamic imports. No real PR stream, external anti-slop installation, scheduler, browser capture, or continuation hook was tested. Cancellation had no live owned background process to stop. Cleanup execution was unavailable under the fixture's no-deletion rule; only the read-only preview was qualified. The loop is an active-session procedure, not a background service.
