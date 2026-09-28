# Evaluate MisoStack

Use separate layers of evidence. A structural validator checks files. A helper test checks deterministic behavior. A host smoke test checks discovery and loading. A behavioral evaluation checks what the agent actually does.

## Run local checks

```sh
python3 plugins/miso-stack/scripts/miso.py check
python3 -m unittest discover -s tests
python3 scripts/check_repository.py
```

These checks use temporary directories for mutable state. They cover task dependencies, ownership, evidence changes, installation collisions, timeouts, and command argument handling.

## Run a sandbox task

```sh
python3 scripts/create_sandbox.py /tmp/miso-evaluation
```

Use the [case catalog](../../evals/cases.json). Each case defines a prompt, skills under test, and observable grading criteria. Start a fresh target-harness session in the fixture directory. Use its default model. Test native discovery separately from source evaluation. Keep external writes, Git setup, and unrelated files outside the case scope.

The evaluation runner prepares a new fixture, applies bounded test permissions, invokes the installed harness, and saves its trace:

```sh
python3 scripts/run_evaluation.py --harness codex --case bug-fix --output /tmp/miso-codex-check
```

Supported harness arguments are `codex`, `claude`, `grok`, and `opencode`. Use `--case smoke` for read-only loading. The default limit is 240 seconds; set `--timeout` for a longer case. The output directory must not exist. Model IDs are never supplied by the runner. Each prompt names the exact source entry file so a cached installed plugin cannot stand in for the changed code.

The runner closes the child's standard input. The task arrives only through the explicit prompt argument. This prevents a parent shell script from becoming extra task context.

Use `--case routing` to classify all 24 specialist and default scenarios in [routing.json](../../evals/routing.json). The model sees the requests but not their expected labels. This tests workflow selection; it does not execute those workflows.

Use `--case capability-routing` for the 39 skill-and-mode scenarios in [capability-routing.json](../../evals/capability-routing.json). This covers every supporting skill. Expected skills and modes are withheld from the prompt. A single-purpose skill reports mode `default`.

```sh
python3 scripts/run_evaluation.py --harness codex --case capability-routing --output /tmp/miso-capability-routing
```

The `spec`, `tickets`, `review-boundary`, `comments`, `merge-boundary`, and `audit` cases check artifact and scope behavior. The `garden` case checks read-only maintenance inspection. The `loop` and `loop-blocked` cases check verified completion and unavailable prerequisites. The `performance` case checks measurement without unauthorized optimization. The merge-boundary case uses a fixture without Git and must leave it unchanged. A positive merge test requires a separate disposable repository with known changes on both sides. Do not initialize Git in a real project to manufacture this test.

The runner uses normal host account access. It creates no credentials. Grok uses its workspace sandbox. Codex uses its native sandbox. Claude and OpenCode retain their native permission handling; fixture-local rules allow the required local test operations. The fixture boundary is part of the test contract, not a claim that all four hosts provide identical OS isolation.

Save the raw host trace locally and grade the resulting artifacts. Run the fixture's tests and CLI after the agent finishes. Confirm the unrelated marker remains unchanged. Record whether the skill and host map were actually loaded.

Do not feed grading answers into the task prompt. Do not treat a model's own claim of success as the grade. A single successful run is a smoke test, not a reliability estimate.

A headless process can exit zero after a tool permission is rejected. Inspect tool results, preserved markers, file changes, and actual test output before grading. The runner records added, changed, and removed fixture files. It deliberately leaves `grade` as `not-graded`.

## Compare a skill change

Use the same fixture, prompt, rubric, and environment for the baseline and candidate. Keep them in separate directories. Repeat cases when consistency matters. Include a negative case that requires an approval boundary or an honest unavailable-capability result.

## Record results

Update [verification](../verification.md) with the command, version, evidence location, result, and limitation. Keep failed runs. Use `unverified` for a host that could not execute. Keep worker concurrency separate from skill loading.
