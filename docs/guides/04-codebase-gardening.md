# Guide 4: Make good changes easier to make

A codebase needs maintenance as new work arrives. A duplicated parser or one lint suppression can be harmless. Repeated across many changes, it can reveal a missing boundary or a poor data model.

Miso's gardening workflow looks for those patterns. It starts with evidence, fixes a coherent problem when requested, and puts a check in the codebase to prevent its return.

## Start with a bounded inspection

Choose a commit range, a set of PRs, or one subsystem:

```text
Use miso to inspect the last ten local commits for structural drift.
Look for repeated helpers, new suppressions, and ownership violations.
Report confirmed patterns and their callers. Do not change files.
```

Expect findings tied to code. If remote PR access is unavailable, Miso should say so and use the available local history. It should not invent a stream of reviewed PRs or post comments without authorization.

Repetition is a reason to investigate. It does not prove that the code needs a shared helper. Two shape checks may protect different trust boundaries. A generic helper can make that distinction harder to see.

## Repair the structure behind a pattern

Suppose several UI files import storage internals. Another review reminder will not stop the next import. A useful repair can expose one domain operation and reject direct UI-to-storage dependencies.

```text
Use miso to fix the UI-to-storage boundary violations you found.
Preserve user behavior. Add a check to our existing validation command
that rejects direct storage imports from UI code.
Prove the forbidden path fails and the supported path passes.
```

This should produce a smaller burden on callers and an executable rule. Depending on the language, that rule might be a compiler restriction, schema, import check, or focused lint rule.

The same approach applies to state. Replace combinations of flags with explicit states when that makes invalid combinations impossible. Parse unknown input at the boundary so inner code can use a stable domain type. Give mutable data an owner before sharing it across concurrent actors.

These changes can matter more than a longer AGENTS.md. They give every contributor the same immediate feedback. They also need tests: an overbroad rule that rejects valid work creates its own maintenance problem.

## Keep the repair small and complete

Before adding a layer, inspect what can be removed. Forwarding methods, repeated choices, and configuration passed through many callers can hide misplaced responsibility.

Prefer a module that does substantial work through a clear interface. Keep its decisions and data close together. Similar lines can stay separate when combining them would require a new vocabulary of flags and exceptions.

Build foundations in the order the task needs them. Shared types and a failing constraint check may unblock all later changes. A new framework, language migration, or broad rewrite needs its own reason and scope.

## Add lint rules deliberately

For a project that requests anti-slop checks:

```text
Use miso to set up anti-slop checks with our existing package manager.
Preserve local lint settings and custom rules. Run lint and type checks.
Report existing violations; do not migrate application code yet.
```

Miso reads the current external installation procedure and checks whether the target supports it. The plugin is not bundled with MisoStack. Setup can require dependencies and project-owned rule files; it must preserve the project's third-party code policy and license files.

A successful install does not mean the app passes lint. Existing violations should remain visible. Request cleanup separately when you want those violations repaired. Miso should not weaken rules to manufacture a clean run.

## Turn a proven pass into a routine

First run a useful manual pass. Then ask for a schedule proposal:

```text
Use miso to draft a daily gardening routine for new PR changes.
Reuse the checks we just proved. Track the last inspected revision,
avoid duplicate findings, and stop on unavailable access.
Keep it inactive until I approve activation.
```

The proposal needs an owner, input source, limits, failure reporting, and a disable path. Without a supported scheduler, it remains inactive. Reading changes, repairing code, and sending review comments are separate permissions.

Use [the skill catalog](../reference/catalog.md) for direct access, or continue to [performance work](../how-to/improve-performance.md).
