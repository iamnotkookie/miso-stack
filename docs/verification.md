# Verification record

MisoStack was qualified on macOS on 26 September 2026. The checks below separate package validity, helper behavior, native host loading, and agent behavior.

This records the initial qualification. Lucas subsequently authorized repository initialization and the first local commit, along with a README revision. Source hashes describe the files at qualification time.

The result supports use of this local release. It does not establish statistical reliability or complete runtime parity with pstack.

## Package and helpers

| Check | Observed result |
| --- | --- |
| Package inventory | 16 skills; 24 workflows; eight default workflows |
| Python helper suite | 20 tests passed |
| Official skill validator | All 16 skills passed |
| Plugin manifests | Codex, Claude Code, and Grok Build validators passed |
| Repository check | Python syntax, JSON, local document links, and 73 reference mappings passed |
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
| Design and arena | Built two interfaces and compared 36 cases. Independent rerun passed all 36. Serial fallback was explicit. |
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

## Reference comparison loop

The reference is pstack revision `ecc249f1e306fc64ddf83c7bed16cacf7c2239db`: 50 skills and 23 playbooks, including 23 principle skills.

The first pass mapped gaps and built the original MisoStack capabilities. Later passes tested helpers, host loading, and agent behavior, then repaired observed failures. A final public inventory check returned the same revision, with no new or removed entries.

The [audit](reference-audit.json) maps 72 entries to MisoStack implementations. Grok Bot UI is excluded because it is outside the four agreed harnesses. Several entries share a skill or reference. This is capability coverage, not 72 independent runtime tests.

Repeat the inventory check with:

```sh
python3 scripts/check_reference.py --live
```

## npm installer qualification

The current local suite has 28 passing tests. Seven installer tests cover detection, repeat installation, dry runs, marketplace conflicts, skill collisions, missing hosts, and native-command failures. A packaging test builds a tarball and installs it into an isolated npm prefix.

The packed command was run from outside the source directory. It registered the stable installed source through a controlled host stub, and repeat installation kept one marketplace registration. The archive includes the required hidden manifests and excludes evidence and Python caches. The package's repository check also passed.

The source installer was then run against the four real harnesses on this machine. All native installation commands and shared links completed successfully. The npm CLI was installed locally and its preview ran from `/tmp`. These installation checks do not repeat the earlier behavioral evaluation.

Run `npm test` and `npm run check` from the checkout to repeat the local checks. Public npm distribution remains pending; the package is marked private.

## Evidence and limits

Detailed receipts, run grades, source hashes, and fixture artifacts remain local under `evidence/qualification/`. This directory is ignored by Git. Raw host traces remain under `/tmp/miso-evals/` and may contain unrelated host configuration. A new checkout includes this summary, the evaluation cases, and the scripts needed to produce fresh evidence.

The qualification record describes observations from the original machine. Local evidence files are not required to install MisoStack or run its deterministic tests. Follow the [evaluation guide](how-to/evaluate.md) to repeat the checks in your own environment.

Native multi-agent dispatch, browser visual parity, runtime profilers, remote PR actions, production deployment, and active schedulers were not exercised. Their workflows require a real project and its tools. The fixture prohibited subagents and external effects; serial fallback and inactive routines were tested instead.

Successful control checks do not mean the sample app passed: expected product failures remained in the local evidence. Writing follows the stated Simplified Technical English and Zinsser rules; no formal ASD-STE100 certification is claimed.
