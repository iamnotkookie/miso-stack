# MisoStack

**Engineering workflows for agents that check their work.**

MisoStack gives Codex, Claude Code, Grok Build, and OpenCode a shared way to investigate, build, and verify software. Start with `miso` and describe the result you want. It selects a workflow, reads the project, and uses the tools available in your coding agent.

The work should end with something you can inspect: a reproduced bug, a measured improvement, a working user journey, or a documented limitation.

```text
Use miso to fix the export command. Empty reports crash it.
Reproduce the failure, fix the cause, and show the same command passing.
```

[Install](#install) · [Use Miso](docs/how-to/use-miso.md) · [Try a sandbox task](docs/tutorials/first-verified-change.md) · [Read the guides](#learn-the-workflow) · [See test results](docs/verification.md)

## Just ask miso

Open your project in your coding agent. Send a task in its chat:

| Agent | Example |
| --- | --- |
| Codex | `$miso explain how this project works` |
| Claude Code | `/miso-stack:miso explain how this project works` |
| Grok Build | `/miso explain how this project works` |
| OpenCode | `Use miso to explain how this project works.` |

**Can you use `/miso`?** Yes in Grok Build. In Codex, use `$miso` or select Miso from `/skills`. Claude Code uses the plugin prefix. OpenCode uses its skill loader; this package does not add a `/miso` command there. See [invocation details and host documentation](docs/how-to/use-miso.md#can-i-type-miso).

You can also use `Use miso to…` in every supported agent. Describe the result you want:

```text
Use miso to explain how this cache works and why it exists.
Use miso to turn our discussion into a spec and separate tickets. Do not implement yet.
Use miso to implement the approved spec and verify the result.
Use miso to challenge this diff. Review only.
Use miso to resolve the conflicts in this rebase.
```

Miso selects the supporting skills. A review stays read-only. A spec request produces a spec. Implementation starts when you request it. For a combined task, Miso runs the relevant steps in order and honors your stop points.

Read [Use Miso for everyday work](docs/how-to/use-miso.md) for a walkthrough, ready-to-use prompts, and help when a skill does not load.

The [routing table](plugins/miso-stack/skills/miso/references/routing.md) covers every supporting skill.

## How it works

MisoStack is a set of skills, workflows, and local tools that runs inside your existing coding agent. A **skill** gives the agent a reusable procedure. A **playbook** connects those procedures for a specific kind of work.

1. **Understand the task.** Read the relevant code, project instructions, and available evidence. Separate observed behavior from assumptions.
2. **Choose a path.** Load the relevant playbook and supporting skills. Use the current harness's tools and model configuration.
3. **Build and check.** Reproduce defects before editing. Test uncertain designs with small prototypes. Run the behavior that the user will use.
4. **Show the result.** Report what changed, what actually ran, and what remains unverified. Preserve the evidence needed to review it.

For the export example, a passing unit test helps check the contract. Running the export and inspecting the saved file checks the user outcome. MisoStack asks for both when both matter.

The shared source contains **23 skills and 24 workflows**. Eight workflows cover daily engineering: investigation, bug fixes, features, prototypes, refactoring, performance, plans, and documentation. Specialist workflows cover reviews, traces, visual checks, skill evaluation, PR work, and session recovery.

## Install

Install from npm and choose your coding agents:

```sh
npm install -g miso-stack
```

The installer opens a keyboard picker with all detected harnesses selected. Use the arrow keys to move, Space to toggle, and Enter to install. It installs native plugins for Codex and Claude Code, and shared skill links for Grok Build and OpenCode.

The prompt opens during installation on macOS and Linux when npm permits install scripts. If npm reports blocked scripts, run `miso-stack install` to open setup yourself. Press Esc to cancel setup. To change your selection later, run the same command.

Start a fresh session in your project and use [the entry for your agent](#just-ask-miso).

To select one harness, install without prompts, or preview changes:

```sh
miso-stack install codex
miso-stack install --yes
miso-stack install --dry-run
```

Requires **Node.js 18+, Python 3.10+, and macOS or Linux**. Keep the npm package installed; shared skills refer to its files. Model access and hook trust use your harness's normal controls.

To test a checkout, use `npm install -g .`. You can also run `./install.sh` without Node.js.

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
Use miso to explain how retries work and why the limit exists.
Read the implementation and available history. Label inferred reasons.
Keep this pass read-only.
```

Mechanics, historical intent, and explanation need different evidence. Missing history should stay missing.

### Make a consequential design choice

```text
Use miso to design a batch import API from the caller's perspective.
Compare two runnable approaches. Test partial failure and cancellation
before recommending one. Stop before production implementation.
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
Use miso to create a project-local control skill.
Reuse our existing browser tooling. Add a health check, a feature map,
and one complete user journey. Execute it and preserve the proof.
```

The driver belongs in your app. Its feature map explains how to reach behavior, what to expect, and how to recover. See [Guide 1](docs/guides/01-verification.md).

### Plan work that spans sessions

```text
Use miso to migrate the parser in small, verifiable steps.
Preserve the public format. Record dependencies, evidence, and decisions
so another session can continue the work.
```

The local plan helper checks dependencies, ownership, and accepted evidence hashes. It is a task ledger. The coding agent performs the work.

## Skills you can call directly

| Task | Skills |
| --- | --- |
| Understand code, history, and prior work | `miso-research` |
| Design interfaces and compare alternatives | `miso-design` |
| Maintain architecture and enforce recurring rules | `miso-garden` |
| Repeat work with limits and resumable state | `miso-loop` |
| Measure and improve performance | `miso-perf` |
| Write a spec and divide it into tickets | `miso-spec`, `miso-tickets` |
| Diagnose, test, review, and prove a change | `miso-debug`, `miso-tdd`, `miso-review`, `miso-verify` |
| Audit a repository or a skill for security defects | `miso-audit` |
| Resolve merge or rebase conflicts | `miso-merge` |
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
4. **[Make good changes easier to make](docs/guides/04-codebase-gardening.md).** Find recurring problems and prevent them with types, boundaries, and executable checks.

For measured optimization, use [Improve performance with evidence](docs/how-to/improve-performance.md). For a bounded work loop, state the acceptance checks and an iteration or time limit. Loops execute within the active session; they do not install a background service.

For exact commands, use the [CLI reference](docs/reference/cli.md). For the shared rules and implementation boundaries, read [architecture and authority](docs/explanation/architecture.md).

## Defaults and boundaries

- **Models:** use each harness's default unless the project supplies a model configuration. No fixed model IDs are built in.
- **Writing:** use Simplified Technical English and Zinsser's Simplicity, Brevity, Clarity, and Humanity.
- **Autonomy:** complete reversible local work within the request. Force-pushes, deployments, data deletion, and messages require authorization.
- **Permissions:** honor project restrictions and native host controls. Skill instructions are not an operating-system sandbox.
- **Automation:** test a routine before activating it. Without an authorized scheduler, report it as inactive.

## What has been tested

The local suite has **38 passing helper and packaging tests**. The installer test permits only its temporary tarball to run its setup hook. The [installation guide](docs/how-to/install.md#install-without-the-npm-prompt) covers manual setup and npm script permission.

Initial agent qualification covered **12 behavioral cases across all 16 skills** and **24 correct routing cases**. All four harnesses loaded MisoStack and completed a repair in separate sandbox fixtures.

The complete behavioral set ran in Codex. The other harnesses ran loading and repair checks. These samples do not establish every workflow in every host. Native worker dispatch, production deployments, remote PR actions, and active schedulers still need project-specific verification.

Read [the results, retained failures, and limitations](docs/verification.md). To reproduce or extend the checks, follow [the evaluation guide](docs/how-to/evaluate.md).

## Development

Run the existing checks after relevant changes:

```sh
python3 plugins/miso-stack/scripts/miso.py check
python3 -m unittest discover -s tests -v
python3 scripts/check_repository.py
```

Use separate sandbox folders for agent evaluations. Keep raw host traces and credentials out of commits. Keep new evaluation artifacts in temporary folders. Git contains the test cases, scripts, and results summary.

## License

Original work is licensed under [MIT](LICENSE). See [NOTICE](NOTICE) for attribution.

Report vulnerabilities through the private channel in [the security policy](SECURITY.md).
