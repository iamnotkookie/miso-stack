# Set up anti-slop checks

Use this path only for a requested lint setup or update. MisoStack does not bundle the external plugin. Inspect the target's package manager, installed lint versions, configuration, local changes, and existing custom rules first.

For the named anti-slop project, read its current [installation procedure](https://github.com/dmmulroy/anti-slop/blob/main/skills/install-anti-slop/SKILL.md) and relevant update instructions. Inspect the installer and assets at a specific revision before executing anything. Follow the target project's dependency and third-party code rules. Preserve licenses and any existing customization. Do not run a floating remote shell script.

The external plugin uses Oxlint. Keep `oxlint` and `@oxlint/plugins` at matching compatible versions. Merge configuration rather than replacing it. Enable Effect-specific checks only for a direct Effect dependency or an explicit request. Verify installation with real lint and type checks; report unsupported tooling or unresolved diagnostics.

Installation and codebase cleanup are distinct scopes. If only setup was requested, report existing violations without rewriting the app. When cleanup is authorized, test semantic changes and check that formatting and fixes converge on a second pass. Do not hide violations with new suppressions.

For other languages or projects that prohibit vendoring, use compatible existing checks or explain the constraint. Do not claim that anti-slop was installed when only a proposed configuration was written.
