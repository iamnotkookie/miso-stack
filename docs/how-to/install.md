# Install MisoStack

Use this guide to install the same skill source on the four supported harnesses. Run commands from the MisoStack directory. Python 3.10 or later is required for helpers. The plan ledger uses POSIX file locks on macOS and Linux.

## Install with npm

From this checkout:

```sh
npm install -g .
miso-stack install
```

The npm CLI needs Node.js 18+. The existing helpers need Python 3.10+. No npm runtime dependencies are required. Package installation registers the command; setup runs only when you invoke it. There is no automatic postinstall hook.

The installer detects supported harnesses on PATH. It checks the package and existing marketplace sources before changing anything. It refuses to replace another source registered as `miso-local` or an unrelated skill with the same name.

Start a fresh session and ask for `miso`. Claude Code also accepts `/miso-stack:miso`.

| Command | Action |
| --- | --- |
| `miso-stack install` | Install for all detected harnesses. |
| `miso-stack install codex` | Install only for Codex. |
| `miso-stack install claude opencode` | Install for the named harnesses. |
| `miso-stack install --dry-run` | Check prerequisites and preview without installing. |
| `miso-stack --version` | Print the package version. |

The package is not published to the npm registry yet. To distribute it locally, run `npm pack` and install the resulting tarball with `npm install -g /path/to/miso-stack-0.1.1.tgz`. After an authorized publication, use `npm install -g miso-stack`. The package is marked private until that release decision.

Keep the global package installed. Shared links and local marketplaces need a stable source directory. Temporary `npx` installs are rejected for setup because clearing the npm cache would break those references. A local-directory npm installation can link to the checkout, so keep that checkout in place too.

An existing marketplace pointing to a different installation is reported as a conflict. Inspect it and choose the source you want before migrating; the installer does not silently replace it. Model access and hook trust remain native host responsibilities.

If a native command fails, the installer stops and prints the error. Earlier successful steps remain in place. Correct the error and run it again.

## Run directly from source

Without npm, run `./install.sh` from this checkout. It accepts the same harness names and `--dry-run`. You can invoke it by absolute path from another directory.

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

Start a new thread and ask for `miso`. Codex has a separate hook trust step in `/hooks`. Review the reminder there if you want automatic startup guidance. Installing the plugin does not bypass trust. Explicit invocation remains available.

## Updates and removal

Shared links see source changes on the next discovery pass. Plugin installations can cache files. Reinstall or update the plugin through the host after changing the source, then start a fresh session. Keep proof of which installed version was tested.

Use the host's plugin uninstall command to remove a plugin. For shared links, inspect the target with `ls -l` and remove only links that point to this repository, after approving that cleanup. Do not remove another skill directory with the same name.

## Verify the result

Ask each host to load `miso`, identify its harness, select a bug-fix workflow, and report the file it read. Check the tool trace when available. Test delegation separately. See [qualification results](../verification.md) for what this machine actually proved.

Sources: [OpenCode skill discovery](https://opencode.ai/docs/skills/), [Claude plugin reference](https://code.claude.com/docs/en/plugins-reference), [Codex plugin packaging](https://developers.openai.com/plugins/build/plugins). Grok behavior was checked against its installed user guide.

The npm package uses the standard [files and bin fields](https://docs.npmjs.com/cli/v11/configuring-npm/package-json/) to include the shared source and expose its command.
