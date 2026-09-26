# MisoStack

**Engineering workflows for agents that check their work.**

MisoStack gives Codex, Claude Code, Grok Build, and OpenCode a shared way to investigate, build, and verify software. Start with `miso` and describe the result you want. It selects a workflow, reads the project, and uses the tools available in your coding agent.

The work should end with something you can inspect: a reproduced bug, a measured improvement, a working user journey, or a documented limitation.

```text
Use miso to fix the export command. Empty reports crash it.
Reproduce the failure, fix the cause, and show the same command passing.
```

[Install](#install) · [Try a sandbox task](docs/tutorials/first-verified-change.md) · [Read the guides](#learn-the-workflow) · [See test results](docs/verification.md)

## How it works

MisoStack is a set of skills, workflows, and local tools that runs inside your existing coding agent. A **skill** gives the agent a reusable procedure. A **playbook** connects those procedures for a specific kind of work.

1. **Understand the task.** Read the relevant code, project instructions, and available evidence. Separate observed behavior from assumptions.
2. **Choose a path.** Load the relevant playbook and supporting skills. Use the current harness's tools and model configuration.
3. **Build and check.** Reproduce defects before editing. Test uncertain designs with small prototypes. Run the behavior that the user will use.
4. **Show the result.** Report what changed, what actually ran, and what remains unverified. Preserve the evidence needed to review it.

For the export example, a passing unit test helps check the contract. Running the export and inspecting the saved file checks the user outcome. MisoStack asks for both when both matter.

The shared source contains **16 skills and 24 workflows**. Eight workflows cover daily engineering: investigation, bug fixes, features, prototypes, refactoring, performance, plans, and documentation. Specialist workflows cover reviews, traces, visual checks, skill evaluation, PR work, and session recovery.

## Install

Install the CLI with npm, then let it set up your coding agents. From this checkout:

```sh
npm install -g .
miso-stack install
```

The installer detects Codex, Claude Code, Grok Build, and OpenCode on your PATH. It checks the package, installs native plugins, and creates shared skill links where needed.

Start a fresh session and ask for **miso**. In Claude Code, you can also use `/miso-stack:miso`.

To select one harness or preview changes:

```sh
miso-stack install codex
miso-stack install --dry-run
```

Requires **Node.js 18+, Python 3.10+, and macOS or Linux**. Keep the npm package installed; shared skills refer to its files. Model access and hook trust use your harness's normal controls.

This package is not published to npm yet. After publication, `npm install -g miso-stack` will replace the local install command above. You can also use `./install.sh` directly from the checkout without Node.js.

See the [installation guide](docs/how-to/install.md) for options and manual commands, or [troubleshooting](docs/how-to/troubleshoot.md) if something fails.

## Start with a task you can check

Use the [sandbox tutorial](docs/tutorials/first-verified-change.md) to try MisoStack on a small, deliberately broken calculator. It needs no application service or credentials. Your harness still needs model access.

For your own project, describe the expected result and any constraints:

```text
Use miso to add CSV export to the reports page.
Preserve the current filters. Verify an empty report and a report with data.
Open the exported files and check their contents.
```

You do not need to select every supporting skill. The entry chooses them from the task. Call a skill directly when you want a specific procedure.

### Understand an unfamiliar system

```text
Use miso-research to explain how retries work and why the limit exists.
Read the implementation and available history. Label inferred reasons.
Keep this pass read-only.
```

Mechanics, historical intent, and explanation need different evidence. Missing history should stay missing.

### Make a consequential design choice

```text
Use miso-design to design a batch import API from the caller's perspective.
Compare two runnable approaches with miso-arena. Test partial failure
and cancellation before recommending one.
```

Candidates use a common rubric. Independent workers are used only when available and permitted. Otherwise, the work runs serially and says so.

### Improve performance with measurements

```text
Use miso to reduce the report page's loading time.
Capture a baseline, identify the cause, and make a targeted change.
Repeat the same workload and report the samples and correctness checks.
```

A faster single run can be noise. The workflow asks for comparable conditions and evidence for the improvement.

### Build a verification tool for your app

```text
Use miso-verify to create a project-local control skill.
Reuse our existing browser tooling. Add a health check, a feature map,
and one complete user journey. Execute it and preserve the proof.
```

The driver belongs in your app. Its feature map explains how to reach behavior, what to expect, and how to recover. See [Guide 1](docs/guides/01-verification.md).

### Plan work that spans sessions

```text
Use miso-plan to migrate the parser in small, verifiable steps.
Preserve the public format. Record dependencies, evidence, and decisions
so another session can continue the work.
```

The local plan helper checks dependencies, ownership, and accepted evidence hashes. It is a task ledger. The coding agent performs the work.

## Skills you can call directly

| Task | Skills |
| --- | --- |
| Understand code, history, and prior work | `miso-research` |
| Design interfaces and compare alternatives | `miso-design`, `miso-arena` |
| Reproduce, test, review, and prove a change | `miso-tdd`, `miso-review`, `miso-verify` |
| Write tutorials, guides, and reference material | `miso-docs` |
| Coordinate work and preserve decisions | `miso-plan`, `miso-swarm`, `miso-trail` |
| Create, evaluate, and improve skills | `miso-author`, `miso-eval`, `miso-reflect` |
| Check installation and prepare bounded routines | `miso-setup`, `miso-automate` |

The [full catalog](docs/reference/catalog.md) links every skill and playbook, including its completion criteria.

## Learn the workflow

The guides explain the method through practical tasks:

1. **[Give the agent a way to prove its work](docs/guides/01-verification.md).** Build app controls, map features, and retain useful evidence.
2. **[Understand the problem, then test the design](docs/guides/02-research-and-design.md).** Investigate intent, design from usage, and compare prototypes.
3. **[Run larger work without losing control](docs/guides/03-long-running-work.md).** Define completion, track dependencies, and resume from verified state.

For exact commands, use the [CLI reference](docs/reference/cli.md). For the shared rules and implementation boundaries, read [architecture and authority](docs/explanation/architecture.md).

## Defaults and boundaries

- **Models:** use each harness's default unless the project supplies a model configuration. No fixed model IDs are built in.
- **Writing:** use Simplified Technical English and Zinsser's Simplicity, Brevity, Clarity, and Humanity.
- **Autonomy:** complete reversible local work within the request. Force-pushes, deployments, data deletion, and messages require authorization.
- **Permissions:** honor project restrictions and native host controls. Skill instructions are not an operating-system sandbox.
- **Automation:** test a routine before activating it. Without an authorized scheduler, report it as inactive.

## What has been tested

The local suite has **28 passing helper and packaging tests**. Initial agent qualification covered **12 behavioral cases across all 16 skills** and **24 correct routing cases**. All four harnesses loaded MisoStack and completed a repair in separate sandbox fixtures.

The complete behavioral set ran in Codex. The other harnesses ran loading and repair checks. These samples do not establish every workflow in every host. Native worker dispatch, production deployments, remote PR actions, and active schedulers still need project-specific verification.

Read [the results, retained failures, and limitations](docs/verification.md). To reproduce or extend the checks, follow [the evaluation guide](docs/how-to/evaluate.md).

## Development

Run the existing checks after relevant changes:

```sh
python3 plugins/miso-stack/scripts/miso.py check
python3 -m unittest discover -s tests -v
python3 scripts/check_repository.py
```

Use separate sandbox folders for agent evaluations. Keep raw host traces and credentials out of commits. Evidence stays local under the ignored `evidence/` directory. Git contains the test cases, scripts, and results summary.

## Reference and license

MisoStack is an original implementation informed by Lauren Tan's pstack guides. It adapts the ideas to four harnesses, shared source, default models, and Lucas's working rules.

The [pstack comparison](docs/explanation/pstack-comparison.md) maps the reference capabilities and explains deliberate differences. The [provenance record](UPSTREAM.md) identifies the audited revision. No pstack code is vendored.

Original work is licensed under [MIT](LICENSE). See [NOTICE](NOTICE) for attribution.
