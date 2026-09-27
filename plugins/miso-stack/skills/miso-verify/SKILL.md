---
name: miso-verify
description: "Runs, creates, or maintains project-specific verification tools and feature maps. Use when proving a change works, creating a control skill, or auditing verification coverage."
license: MIT
---

# Verify

Apply the shared rules and current host map in [miso](../miso/SKILL.md). When called directly, run this procedure after reading those rules. When called from a playbook, continue that playbook without restarting routing.

Use existing project tools first. Select run, create, or maintain from the request.

## Run

1. Name the user-visible behavior and the failure that would disprove success. Choose its real surface: browser, CLI, API, library, desktop, or infrastructure.
2. Read the project's launch and verification instructions. Establish a clean baseline. Use isolated data, ports, and profiles. Verify instance ownership before driving it.
3. Run the action and observe the resulting state and side effects. Use tests for focused contracts and the real surface for the reported behavior. A mock proves only the boundary it simulates.
4. Save commands, exit status, relevant output, and artifact paths inside the authorized workspace. Avoid shared fixed paths in `/tmp`. Compare before and after for a fix or performance change. Redact secrets before storing evidence.
5. Stop only processes this run started. Keep evidence outside disposable runtime state and verify it survives teardown. A destructive cleanup still requires approval.

## Create

Create a control skill inside the target app only when requested or needed for the authorized app work. Never create a fictional app driver in the MisoStack catalog. Inspect the app's actual launch command, authentication, test data, and available controls. Use [the control contract](../miso/references/verification.md). Provide an executable CLI with help, machine-readable output, clear errors, health checks, and a safe dry run for destructive actions. Reuse an existing driver before writing one.

Use a project skill directory that the current host discovers. If that directory is not writable, use an authorized local directory and document explicit file-path invocation. Test discovery separately; a working driver does not prove that the host loads its skill automatically.

Add a feature index and records using [the feature contract](../miso/references/feature-map.md). Start with the app's real reachable features. Run launch, health check, one complete feature journey, evidence capture, and teardown. An unexecuted driver is a draft.

Use the control contract's inspection, navigation, interaction, performance, streaming, and health vocabulary only where the real app supports it. Keep a capabilities list so an absent control is explicit. Exercise JSON output, useful errors, timeouts, and mutation-free dry runs as well as the successful path.

## Maintain

Compare the feature index with routes, commands, recent changes, and existing feature files. Drive each documented feature on the current app. Separate stale documentation, broken driver behavior, and product defects. Repair the first two within scope and rerun them. Record product defects without silently expanding the task. Mark inaccessible features with the missing prerequisite and attempted path.

Return verified, failed, or unverified per check, with the exact evidence. Tests, static checks, and live proof remain separate.

If a headless command is denied, do not assume the user cancelled the task. Identify the blocked permission and continue through an already authorized tool when possible. Use simple commands or the bundled `record` helper instead of a shell chain that the host cannot safely authorize. Never bypass the host's security controls.
