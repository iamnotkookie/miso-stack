# Engineering principles

These rules guide engineering decisions in MisoStack. Apply them when they help resolve a concrete choice.

## laziness-protocol

**Choose the smallest complete change.** Remove unnecessary work and reuse a proven tool before inventing a layer.

Inspect forwarding functions, repeated decisions, and representation leaks before adding an abstraction. Put a decision with its owner instead of coordinating copies across callers. If a new flag must travel through many layers, inspect whether the responsibility is in the wrong place. Prefer a direct path that preserves boundaries. Optimize the maintenance burden, not a line-count target; a deep module can hide substantial work without a long chain of pass-through calls.

## foundational-thinking

**Start with ownership and data.** Name the domain objects, state owners, and proof method before adding behavior.

Choose data structures from actual access patterns and invariants. Similar statements need not become a generic abstraction; shared domain structure matters more than textual duplication. Before actors share mutable state, trace concurrent writes and choose isolation or an explicit owner. Remove obsolete structure within scope, then build only the types, checks, and setup that unblock later work. Each increment should make a coherent capability easier to use.

## enforced-architecture

**Make invalid changes fail early.** Use module boundaries, schemas, type checks, compiler diagnostics, and targeted lint rules to enforce the architecture. A rule in a document needs a person or agent to remember it; an executable check can reject a violation. Test both a forbidden case and a valid case. Invest in these constraints before growing a longer instruction file. See [gardening](../../miso-garden/SKILL.md) for recurring maintenance.

## redesign-from-first-principles

**Reconsider the structure.** When a new requirement conflicts with the design, compare a simpler integrated shape with another workaround.

## attack-the-premise

**Question repeated failure.** When experiments fail for the same reason, test the shared assumption before another patch.

## subtract-before-you-add

**Remove dead weight.** Delete obsolete paths only within authorized scope, then build on the smaller design.

## minimize-reader-load

**Keep the path visible.** Reduce hidden state, needless indirection, and names that conceal ownership.

## outcome-oriented-execution

**Finish the intended migration.** Use temporary compatibility only with an explicit need and removal condition.

## experience-first

**Start with the user outcome.** Evaluate how the person calls, operates, and recovers the system before internal convenience.

## exhaust-the-design-space

**Compare consequential alternatives.** Use a few executable candidates when a choice has no reliable precedent.

## build-the-lever

**Build a reusable tool.** Turn repeated manual operations or proof steps into small inspectable commands.

## model-the-domain

**Represent the domain directly.** Use explicit states and types instead of flags whose combinations have unclear meanings.

## boundary-discipline

**Validate at boundaries.** Validate untrusted inputs and keep integration failures out of pure domain logic.

## type-system-discipline

**Make contracts checkable.** Use narrow types and validated construction. Do not suppress evidence of a bad model with casts.

## make-operations-idempotent

**Make retries safe.** Use stable identity and explicit state so a retry converges without repeating effects.

## migrate-callers-then-delete-legacy-apis

**Retire obsolete interfaces.** Move known callers, prove compatibility where required, then remove old code with authorization.

## separate-before-serializing-shared-state

**Separate writers.** Prefer separate state or one clear owner over competing writes and more locks.

## prove-it-works

**Prove the actual result.** Exercise the relevant artifact and user path. Do not replace runtime evidence with a claim.

## fix-root-causes

**Test the mechanism.** Reproduce the symptom and verify the cause before selecting a fix.

## sequence-verifiable-units

**Verify each unit.** Order changes so each unit has a useful, repeatable acceptance check.

## test-behavior-not-implementation

**Test the contract.** Check a known result through the caller-facing interface rather than restating source structure.

## guard-the-context-window

**Keep context relevant.** Search before reading broadly. Retain decisions and evidence pointers, not huge raw outputs.

## never-block-on-the-human

**Use granted autonomy.** Resolve observable facts with tools and continue reversible work. Keep explicit approval boundaries.

## encode-lessons-in-structure

**Prevent repeat failures.** Prefer a schema, test, lint, or better tool when it can enforce a recurring lesson.

## structure

**Shape the code so the next change stays local.** Apply the rule the change actually breaks.

- **DRY.** One business rule has one representation. Two copies will disagree.
- **KISS.** A reader follows the change without a tour. Clever loses to clear.
- **YAGNI.** Build the behavior a current requirement or a current failing test names.
- **Single responsibility.** A module changes for one reason.
- **Open-closed.** Extend a tested seam. Do not reopen it for a case the seam already absorbs.
- **Substitution.** A subtype honors the parent contract. An override that changes the contract is a new type.
- **Interface segregation.** A caller depends only on the operations it uses.
- **Dependency inversion.** Domain code depends on an abstraction. The concrete client, database, or clock is injected at the edge.
- **Encapsulation.** State stays private. Callers see the contract.
- **Separation of concerns.** UI, domain, and storage do not share a module.
- **Loose coupling, high cohesion.** Neighbors talk through contracts. Related code sits together.
- **Modularity and abstraction.** A part can be replaced. Hide what changes. Expose what is stable.
- **The seven system rules.** Abstraction, modularity, anticipation of change, separation of concerns, generality, incrementality, and reliability. Generality waits for the second real case. Incrementality means a thin slice with a check. Reliability means a named failure, a retry budget with jitter and a stop, and backpressure on a stream.

Development rules govern the change in front of you: names, tests, commits, duplication. Engineering rules govern the system for years: boundaries, failure, and cost. A tidy diff can still rot the system.

## production

**Bound the work and make the effect single.**

- A retried write, payment, or export is idempotent. The second call does not double the effect.
- Fan-out, exports, queries, and token use have a budget. Unbounded work is a defect.
- The dependency graph is data: lockfile, manifest, or call graph. Blast radius comes from that graph.
- A pipeline has stages with contracts. Retrieve, rank, and present do not share one function.
- One store owns a fact. Caches say they are derived.
- Defense in depth: validation, authorization, and limits stack. An edge check is not the only check on a dangerous action.
- Cost is a design input. Name queries, egress, retained data, and model spend.

## with-agents

**Humans own intent, architecture, and verification. Agents own generation and mechanical edits.**

- The spec, the acceptance criteria, or the failing test is the source of truth. The diff is a projection of that source.
- Context files are code. Keep them short. Add a rule after the same mistake repeats.
- The writer of a change does not approve it. Review runs in a fresh context against the spec and the artifact.
- A constraint is a gate, not a paragraph asking for care.
- Agent output is untrusted until the same gates a human change must pass are green on that revision.
- Use the tool that fits the job, including a non-model tool. Buy a commodity system when running a homegrown one costs more than renting it.
- Measure defects, revert rate, and time to a verified change. Do not score token use or "used an agent."
- Commit a verified slice the author can explain. Do not land a commit nobody can describe.

## refuse-these

- "Clean it up later." Later does not arrive. Fix it here or file an owned follow-up.
- "More people will make it faster." A tangled system gets slower as the team grows.
- "Working code needs no why." Record the non-obvious constraint. Skip a comment that restates the line.
- "If it works, do not touch it." Working code that cannot be changed safely is a liability. Change it in a verified slice.
- "More code is more progress." Deletion counts.

Good software is maintainable by someone who did not write it, dependable in a named way, inside its stated budget, and usable on the empty and error paths. Maintenance costs more than the first build. Design for the second change.
