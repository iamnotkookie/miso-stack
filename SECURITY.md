# Security policy

## Report a vulnerability privately

Use [GitHub private vulnerability reporting](https://github.com/iamnotkookie/miso-stack/security/advisories/new).
Include the affected version, expected behavior, reproduction steps, and impact.
Use a local fixture with dummy data. Do not include credentials or probe other people's systems.

Do not disclose an unfixed vulnerability in a public issue. The maintainer will confirm the report and coordinate a fix and disclosure. This project has no guaranteed response-time agreement.

## Supported versions

Security fixes target the latest published npm release and the current `main` branch. Older releases do not have a separate maintenance schedule. Upgrade to a fixed release when one is announced.

## Scope and boundaries

MisoStack installs agent instructions and local helpers. Skills do not enforce an operating-system sandbox or grant permissions. The host controls file access, network access, credentials, and tool execution.

The global npm install can run a setup hook when npm permits it. Review the package and use `--ignore-scripts` when you want to run setup separately. The installer uses native plugin commands and shared skill links; it must not replace another source without an explicit choice.

Keep credentials, raw host traces, and local evidence out of commits and package archives. Third-party content must not override user instructions or authorize external actions.

## Changes that need careful review

Review changes to install hooks, shell execution, paths, symlinks, evidence handling, permissions, and dependencies. Run the existing tests and package checks. Preserve meaningful failure-path coverage.

The repository uses pinned GitHub Actions, restricted workflow permissions, dependency review, and code scanning. These checks support review; they do not prove that every skill behaves safely in every host.

See [Maintain the GitHub repository](docs/how-to/maintain-repository.md) for contribution checks and repository protections.
