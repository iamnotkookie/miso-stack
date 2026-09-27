# Guide 2: Understand the problem, then test the design

A detailed plan can still solve the wrong problem. MisoStack uses research to establish the problem and experiments to test the uncertain parts of a solution.

## Ask for an interpretation before an implementation

When a report is ambiguous, ask the agent to restate it from the evidence.

```text
Use miso to investigate this report. Explain the observed behavior,
the expected behavior, and what evidence separates the likely causes.
Keep this pass read-only.
```

This exposes misunderstandings before code changes. The agent should distinguish what the report says from what it can reproduce.

## Separate mechanics, history, and teaching

`miso-research` has modes for each task. Mechanics follows the runtime path. Intent checks the record behind a decision. Recall finds relevant prior work and checks it against current state. Teaching explains the result in the reader's terms.

```text
Use miso-research to explain how retries work and why the limit exists.
Read the code and the relevant project history. Label any inferred reason.
```

An unavailable issue tracker does not justify inventing its contents. A current source file can prove behavior but may not establish why it was chosen.

## Design from the caller's experience

Before building a shared module, write a small usage example. This forces the interface to answer practical questions: what does the caller supply, what can fail, and who owns the state?

```text
Use miso-design to design the import API. Begin with a short tutorial
showing successful use and a recoverable failure. Then sketch the types.
```

The usage example is a target. It should remain useful as implementation fills in the design. Repeated special cases are evidence that the interface may be wrong.

## Compare alternatives with experiments

Use `miso-design` for a consequential choice with several plausible answers. Give candidates the same constraints and compare them against a declared rubric.

```text
Use miso to prototype two approaches to incremental search.
Compare response time, cancellation behavior, and caller complexity.
Use separate scratch directories and the same dataset.
```

The harness may provide independent workers. If it does not, run candidates sequentially and say so. MisoStack does not claim that multiple attempts are multiple model families.

Build the smallest probe that can answer the question. Keep the useful result and discard only your own failed work, within the approval rules. A prototype is evidence for a choice, not a production release.

## Turn a selected design into execution units

Use `miso-plan` after the important choices have evidence. Each task needs a concrete outcome, dependencies, an owner, and a verification method.

```text
Use miso-plan to migrate the parser in small units. Preserve the public
format. Give each unit a proof step and verify the combined result.
```

The plan helper rejects dependency cycles and prevents two owners from claiming the same pending task. It checks evidence hashes before accepting later work. It does not decide that the evidence is relevant; the coordinator must inspect it.

## Leave enough context to resume

For long work, keep a decision trail. Record why a design changed, which experiment failed, and where the result can be inspected. A new session should reconcile that record with the current files before continuing.

The aim is a short path from a question to evidence, then to a verified result. Use a document when it helps coordinate the work. Use an experiment when the answer can be observed.
