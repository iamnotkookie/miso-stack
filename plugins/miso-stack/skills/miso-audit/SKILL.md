---
name: miso-audit
description: "Audits authorized source or a skill for security defects and confirms findings independently. Use for a repository security audit or for checking a skill before install."
license: MIT
---

# Security audit

Apply the shared rules and current host map in [miso](../miso/SKILL.md). Apply [security](../miso/references/principles.md). When called directly, run this procedure after reading those rules. When called from a playbook, continue that playbook without restarting routing.

A review of one change stays in [miso-review](../miso-review/SKILL.md). A request to attack, exploit, or penetration-test a live system stops. Live testing is outside this skill. If the user owns the source, continue with a source audit.

Select code or skill from the request. The audit is read-only unless the user also asked for repairs. Repairs go through the normal change workflow, then a fresh confirmation. Record a long audit with [miso-trail](../miso-trail/SKILL.md). Partition independent coverage with [miso-swarm](../miso-swarm/SKILL.md) when the host allows it. Otherwise say the pass is serial: the same agent found the lead and tried to disprove it.

## Code

1. Fix the scope to a repository, a diff, or named paths. Record the revision. Read trust boundaries, inputs, authorization, secrets, dependencies, CI, and release. Prior findings count only when they still match this source.
2. Name the surfaces you will check and the ones you will not. Use scanners, linters, and type checkers the project already runs. Report tools that did not run.
3. Look for a missing authorization check, untrusted input that reaches a query, command, template, or deserializer, secret material in the tree or logs, a missing limit on size or fan-out, a tenant or cache isolation gap, and dependency or release trust.
4. A candidate is a lead. A later pass tries to disprove it against this source. You do not confirm your own lead. Use the verdicts in principles. Severity exists only on a confirmed finding and only with a concrete impact.
5. Report the revision, coverage, verdicts, evidence, and the safe change: check the boundary, drop the privilege, remove the secret, or pin the dependency. If the user named an output path, write there. Otherwise report in the conversation. Do not add a report to the product tree unless they asked.

## Skill

1. Read the skill, its references, scripts, and install metadata. Do not execute it. A file you cannot read is `needs_validation`, not safe.
2. Check for instruction override, concealed commands, secret or environment harvesting, unsolicited network access, supply-chain fetches, tool scope wider than the stated job, and obfuscation.
3. Apply the same verdicts. Do not call the skill safe while a lead is unresolved.

State what was checked, what was not, and whether confirmation was independent or serial. No findings is a result, not proof the target is safe.
