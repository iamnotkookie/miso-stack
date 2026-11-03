# Search the repository

Two questions earn more useful notes than any others: is this already here, and does anything use it? The diff cannot answer either one. Read the code as it stood at the base commit, without changing the checkout. Form your findings before you read other reviewers' notes.

Cite a `path:line` you opened for each claim about the repository. Without a citation, write a `question:`. An empty search is weak evidence, so name the terms you tried and do not state that nothing exists.

## Is it already here?

Run this for a new helper, type, constant, endpoint, cache, component, or script.

1. Describe what the code does, and search for that. An existing version rarely has the same name.
2. Vary the query at least three ways: word forms, naming styles, synonyms, and definition syntax for the language.
3. Look first where it belongs: the shared library, the domain package, or the design system.
4. Read the framework or module being extended. It may already support this.
5. Search for an unusual fragment of the new code, such as an error string or a default value.
6. List the target directory and read its neighbors. A new file beside an obvious home deserves a note.
7. Read the repository's convention files for a rule that the change breaks or reinvents.

Point to the existing code by path, and ask whether the change can use it. When reuse is larger than this change, ask only that no further copy is added.

## Does anything use it?

1. List what the diff adds: exports, parameters, columns, configuration keys, enum members, and flags. Count readers, not writers. Definitions and tests do not count.
2. Before you call something unused, rule out indirect references: string-keyed registries, dispatch tables, reflection, route and command tables, dependency injection, generated code, re-exports, and CI files. Also search for the name inside quotes.
3. List what the diff removes. Search for callers that remain, and for where the behavior went. When it went nowhere, ask why.
4. Look for half a migration: both paths present, a shim with one caller, a deprecated field still written, or a flag with only one reachable value.

## Will it hold up?

1. Follow one real use from start to finish. Check that the consumer has what its second step needs.
2. For each value that grows with a customer, ask what the largest one does to it.
3. When a value is hard-coded along an axis that may vary next, ask about it. Do not demand a change.

Before you finish, delete each note you would not defend in person.
