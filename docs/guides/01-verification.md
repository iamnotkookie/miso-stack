# Guide 1: Give the agent a way to prove its work

A useful engineering agent needs to observe the result of its own changes. A passing build is valuable, but it cannot show that a user can complete the task.

MisoStack starts with the question: what would we observe if this worked? For a command, the answer may be output and an exit status. For a browser feature, it may be a sequence of actions and a saved screenshot. For a service, it may include both the response and the state it changed.

## Start with an existing control path

Before creating a driver, inspect the project. It may already have browser tests, HTTP fixtures, a terminal harness, or a simulator. Reuse that path when it reaches the real behavior.

```text
Use miso to investigate how this app can be verified locally.
Find its launch command, test data, authentication, and existing controls.
Run the smallest safe journey and show the evidence.
```

If the environment cannot start, fix the authorized setup problem or record the missing prerequisite. Do not write instructions that assume a broken command works.

## Build a small control tool when it earns its place

Repeated browser scripts and manual setup steps are good candidates for a reusable command. Ask for `miso-verify` in create mode inside the app repository.

```text
Use miso-verify to create a project-local control skill for this app.
Reuse the existing browser harness. Include readiness, one real feature
journey, saved evidence, and teardown. Execute the generated instructions.
```

The resulting tool should expose useful operations through help and subcommands. It should return machine-readable results, fail clearly, and explain recovery. A destructive operation needs a tested dry-run path.

Keep app-specific selectors, ports, seed data, and feature flags in the app. MisoStack supplies the method; it does not guess those values.

## Make the feature map useful

A feature map tells the next agent what the app does and how to reach the behavior. Each record should name its entry paths, prerequisites, control commands, expected state, and recovery steps.

A settings page might be reachable from both a menu and a keyboard shortcut. Testing one path does not establish the other. Record both when the app supports both.

Keep the index small. Link to feature details instead of loading the entire app description into every task. See the [feature-map contract](../../plugins/miso-stack/skills/miso/references/feature-map.md).

## Use the same surface before and after

For a bug, save a reproduction before editing. After the repair, repeat that reproduction under the same conditions. Add focused tests where they help prevent recurrence.

```text
Use miso to fix the missing export filename. Drive the export action
through the app, check the saved file, and repeat that path after the fix.
```

For performance, record workload and sample conditions. Compare distributions when timing varies. A single fast run can be noise.

## Keep proof separate from temporary runtime state

Put screenshots, terminal output, traces, and receipts in a named evidence directory. Stop only processes the run started. Confirm that proof survives teardown. Do not erase the evidence while cleaning the app profile.

The local `record` helper can capture a command without invoking a shell:

```sh
python3 plugins/miso-stack/scripts/miso.py record evidence/python-version.json -- python3 --version
```

The file records the command, directory, duration, output, and exit code. A receipt proves what the command returned. A reviewer still decides whether that command proves the intended behavior.

## Maintain the verification path

Ask `miso-verify` to maintain the app's control skill after relevant changes. It compares the feature map with source and drives the documented paths. It distinguishes documentation drift, driver defects, and product defects.

Schedule maintenance only after the manual procedure works and a scheduler is explicitly authorized. A routine that cannot detect its own failure will only repeat that failure.
