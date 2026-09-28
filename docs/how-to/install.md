# Install MisoStack

Use this guide to install the same skill source on the four supported harnesses. The npm installation does not need a repository checkout. Python 3.10 or later is required for helpers. The plan ledger uses POSIX file locks on macOS and Linux.

## Install with npm

Install the package and open its harness picker:

```sh
npm install -g miso-stack
```

The npm CLI needs Node.js 18+. The helpers need Python 3.10+. No npm runtime dependencies are required.

The picker shows all four supported harnesses. Available harnesses start selected. Missing harnesses are marked **not found** and cannot be selected.

- Use **↑ / ↓** to move the highlight.
- Press **Space** to toggle the highlighted option. **All detected** toggles the whole selection.
- Press **Enter** to install the selected harnesses.
- Press **Esc** to cancel without changing harness settings.

The picker keeps a separate empty row for npm's progress indicator. It restores your terminal after setup. `NO_COLOR=1` disables color; the highlight and checkboxes remain visible. Use a terminal at least 44 columns wide and 18 rows high.

On a plain terminal (`TERM=dumb`), the installer uses numbered choices. Press Enter for all, enter harness names or numbers for a subset, or enter `0` to cancel.

The installer checks the package and existing marketplace sources before changing anything. It refuses to replace another source registered as `miso-local` or an unrelated skill with the same name.

Start a fresh session in your project. Use `$miso` in Codex, `/miso-stack:miso` in Claude Code, or `/miso` in Grok Build. In OpenCode, write `Use miso to…`. The plain-language form works across all four hosts. See [Use Miso](use-miso.md) for examples and invocation details.

### Install without the npm prompt

When npm permits install scripts, the install hook opens the active terminal directly. It does not need `--foreground-scripts`. If npm skips or blocks install scripts, open the picker yourself:

```sh
npm install -g miso-stack
miso-stack install
```

Some npm versions require permission for package install scripts. If npm prints an `allowScripts` warning, the package can be installed while its setup hook stays blocked. The manual command above opens setup without changing npm policy. To permit this package's hook for one global installation, use:

```sh
npm install -g miso-stack --allow-scripts=miso-stack
```

This option applies to npm versions that support [the install-script allowlist](https://docs.npmjs.com/cli/v11/commands/npm-install/#allow-scripts). It permits MisoStack's scripts for that invocation; it does not disable checks for every package.

The automatic prompt runs only for global installs in an interactive terminal, with `CI` unset or empty. Local dependency installs, shell background jobs, and installs without a controlling terminal do not change harness settings. Use `--ignore-scripts` to disable setup explicitly. A cancelled or failed setup leaves the npm CLI installed. Run `miso-stack install` to retry.

For automation, select harnesses explicitly or use `--yes`:

```sh
npm install -g miso-stack --ignore-scripts
miso-stack install --yes
```

| Command | Action |
| --- | --- |
| `miso-stack install` | Open the harness picker. |
| `miso-stack install --yes` | Install for all detected harnesses without prompting. |
| `miso-stack install codex` | Install only for Codex, without prompting. |
| `miso-stack install claude opencode` | Install for the named harnesses, without prompting. |
| `miso-stack install --dry-run` | Check prerequisites and preview all detected harnesses without installing or prompting. |
| `miso-stack --version` | Print the package version. |

Without a terminal, `miso-stack install` requires names or `--yes`. This prevents an unattended process from silently selecting every harness.

### Test a local package

From a checkout, run `npm install -g .`. To test the exact publishable artifact, run `npm pack`, then install its tarball:

```sh
npm install -g ./miso-stack-0.3.0.tgz
```

Keep the global package installed. Shared links and local marketplaces need a stable source directory. Temporary `npx` installs are rejected for setup because clearing the npm cache would break those references. A local-directory npm installation can link to the checkout, so keep that checkout in place too.

An existing marketplace pointing to a different installation is reported as a conflict. Inspect it and choose the source you want before migrating; the installer does not silently replace it. Model access and hook trust remain native host responsibilities.

If a native command fails, the installer stops and prints the error. Earlier successful steps remain in place. Correct the error and run it again.

## Run directly from source

Without npm, run `./install.sh` from this checkout. It accepts the same harness names, `--yes`, and `--dry-run`. With no arguments, it opens the picker. You can invoke it by absolute path from another directory.

The sections below describe the manual commands used by the installer.

## Check the package

```sh
python3 plugins/miso-stack/scripts/miso.py check
python3 plugins/miso-stack/scripts/miso.py doctor
```

The first command checks the package. The second also finds host binaries. It does not check login or model access.

## OpenCode and Grok Build

Preview links before creating them:

```sh
python3 plugins/miso-stack/scripts/miso.py links
python3 plugins/miso-stack/scripts/miso.py links --apply
```

The installer creates links under `~/.agents/skills/`. A conflicting name stops the operation before any planned link is created. Existing links to this source are kept. Move this repository only after updating its links.

Start a fresh session and ask `Use miso to explain this project.` Check discovery with `opencode debug skill` or `grok inspect --json`. These commands can include unrelated configuration; do not publish their raw output.

MisoStack does not depend on a startup hook for these installations. OpenCode discovers agent-compatible skill directories. Grok Build's documented SessionStart event ignores context output. Invoke `miso` explicitly.

OpenCode can ask for permission to read references beside a globally linked skill. Allow only the MisoStack skill paths and their source directory for the project where you use them. In a headless run, an unanswered permission request can be rejected automatically. The evaluation runner adds a narrow allowance to its fixture-local `opencode.json`; it does not change global policy.

## Claude Code

```sh
claude plugin validate plugins/miso-stack
claude plugin marketplace add .
claude plugin install miso-stack@miso-local
```

Start a fresh session. Invoke `/miso-stack:miso` if the host requires a qualified plugin command. The skill's own name is `miso`; there is no `miso-mode` alias. The plugin includes a small SessionStart reminder.

For temporary local testing, Claude Code also supports `--plugin-dir ./plugins/miso-stack`. This does not establish a persistent installation.

When both a plugin and shared links are visible, the host may list both definitions. They come from the same source. Use the qualified plugin entry when you need to verify plugin loading specifically.

## Codex

```sh
codex plugin marketplace add .
codex plugin add miso-stack@miso-local
```

Start a new thread and invoke `$miso`, or select Miso from `/skills`. Codex has a separate hook trust step in `/hooks`. Review the reminder there if you want automatic startup guidance. Installing the plugin does not bypass trust. Explicit invocation remains available.

## Updates and removal

Shared links see source changes on the next discovery pass. Plugin installations can cache files. Reinstall or update the plugin through the host after changing the source, then start a fresh session. Keep proof of which installed version was tested.

Use the host's plugin uninstall command to remove a plugin. For shared links, inspect the target with `ls -l` and remove only links that point to this repository, after approving that cleanup. Do not remove another skill directory with the same name.

## Verify the result

Ask each host to load `miso`, identify its harness, select a bug-fix workflow, and report the file it read. Check the tool trace when available. Test delegation separately. See [qualification results](../verification.md) for what this machine actually proved.

Sources: [OpenCode skill discovery](https://opencode.ai/docs/skills/), [Claude plugin reference](https://code.claude.com/docs/en/plugins-reference), [Codex plugin packaging](https://developers.openai.com/plugins/build/plugins). Grok behavior was checked against its installed user guide.

The npm install hook connects to `/dev/tty` on macOS and Linux. It checks that the process belongs to the terminal's foreground job before reading input. Opening the terminal directly is also documented in [Inquirer's hook guidance](https://github.com/SBoudrias/Inquirer.js#using-as-pre-commitgit-hooks-or-scripts).

The npm package uses the standard [files and bin fields](https://docs.npmjs.com/cli/v11/configuring-npm/package-json/) to include the shared source and expose its command.
