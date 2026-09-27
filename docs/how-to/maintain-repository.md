# Maintain the GitHub repository

This guide is for maintainers of [iamnotkookie/miso-stack](https://github.com/iamnotkookie/miso-stack). For private vulnerability reports, use the [security policy](../../SECURITY.md).

## Submit a change

Create a branch from current `main`. Make a focused change, run the checks below, and open a pull request. Include what changed and how you verified it.

```sh
python3 plugins/miso-stack/scripts/miso.py check
python3 scripts/check_repository.py
python3 -m unittest discover -s tests -v
git diff --check
```

The installer test uses a temporary npm prefix and a pseudo-terminal. It grants script permission only to the local tarball built by the test. Run it in an environment that permits pseudo-terminals.

Wait for all required checks and resolve review conversations. If `main` changes, update your branch and wait for the new results. Merge with **Squash and merge**. GitHub deletes the merged branch.

## Branch and tag rules

The [main ruleset](https://github.com/iamnotkookie/miso-stack/blob/main/.github/rulesets/main.json) requires:

- A pull request, with all review conversations resolved.
- A branch that is current with `main`.
- Passing checks on Linux and macOS, including the declared minimum Python and Node.js versions.
- Passing Python and JavaScript CodeQL scans and dependency review.
- No new CodeQL errors or high/critical security alerts.
- Linear history, with force pushes and deletion blocked.

The ruleset has no bypass actors. The required review approval count is zero because the repository has one maintainer: GitHub does not let an author approve their own pull request. `CODEOWNERS` routes review requests to `@iamnotkookie`. Add a required independent approval when another maintainer is available.

The [release tag ruleset](https://github.com/iamnotkookie/miso-stack/blob/main/.github/rulesets/release-tags.json) prevents tags that start with `v` from being deleted or moved. It permits new release tags. A tag does not publish a package to npm.

The JSON files describe the rulesets; committing a file does not apply its settings. A repository administrator must apply changes through GitHub. Review the current rules under **Settings → Rules → Rulesets**, then update the matching ruleset:

```sh
gh api repos/iamnotkookie/miso-stack/rulesets \
  --jq '.[] | {id, name, enforcement}'
gh api --method PUT repos/iamnotkookie/miso-stack/rulesets/RULESET_ID \
  --input .github/rulesets/main.json
```

Replace `RULESET_ID` with the ID of **Protect main**. Use the release tag file only for **Protect release tags**. Keep check names in the ruleset aligned with workflow job names.

## Security controls

Secret scanning and push protection are enabled. Dependabot reports vulnerable dependencies and proposes security fixes. Weekly updates cover npm dependencies and GitHub Actions. Review each update and let the required checks run.

CodeQL scans Python and JavaScript on pull requests, pushes to `main`, and a weekly schedule. Dependency review blocks a pull request that introduces a known high or critical dependency vulnerability. These checks do not replace code review or runtime verification.

GitHub Actions is restricted to GitHub-owned actions, with full commit SHA pins required. The default token is read-only, and workflows cannot approve pull requests. CodeQL receives the permission needed to upload scan results. All external contributors need maintainer approval before fork workflows run. Review the workflow and source changes before approving a run. Logs and artifacts expire after 14 days.

When adding an action, check its source and required permissions. Keep its commit pin and version comment together. Do not add a privileged `pull_request_target` workflow that executes pull request code. Do not put credentials or raw local evidence in commits or artifacts.

## Check the live settings

Use **Settings → Actions → General** for action permissions and **Settings → Advanced Security** for scanning and reporting. The [Actions page](https://github.com/iamnotkookie/miso-stack/actions) shows actual run results. The [Security page](https://github.com/iamnotkookie/miso-stack/security) shows alerts and private reports.

Repository rules do not enforce account two-factor authentication or npm account settings. Maintain those controls on each account. npm publication remains a separate, explicit release step.
