#!/usr/bin/env python3
"""Install the local shared source through each available harness's native path."""
import argparse
import json
from pathlib import Path
import shutil
import subprocess
import sys
from types import SimpleNamespace


ROOT = Path(__file__).resolve().parents[1]
HOSTS = ("codex", "claude", "grok", "opencode")
MARKETPLACE = "miso-local"
PLUGIN = "miso-stack@" + MARKETPLACE
TIMEOUT = 120


def select_targets(args):
    if args.harnesses:
        return list(dict.fromkeys(args.harnesses))
    detected = [host for host in HOSTS if shutil.which(host)]
    if not detected:
        raise ValueError("No supported harness found on PATH. Install Codex, Claude Code, Grok Build, or OpenCode first.")
    if args.dry_run or args.yes:
        return detected
    if not (sys.stdin.isatty() and sys.stdout.isatty()):
        raise ValueError("No interactive terminal. Use --yes for all detected harnesses, or name them: miso-stack install codex claude")
    from install_ui import choose
    return choose(detected)


def run(argv):
    result = subprocess.run(argv, cwd=ROOT, stdin=subprocess.DEVNULL,
                            capture_output=True, text=True, timeout=TIMEOUT)
    if result.returncode:
        detail = result.stderr.strip() or result.stdout.strip()
        raise ValueError(f"{' '.join(argv)} failed: {detail}")
    return result.stdout


def registered(host):
    data = json.loads(run([host, "plugin", "marketplace", "list", "--json"]))
    rows = data.get("marketplaces") if host == "codex" and isinstance(data, dict) else data
    if not isinstance(rows, list) or not all(isinstance(row, dict) for row in rows):
        raise ValueError(f"Unexpected {host} marketplace list. Update the harness or use the manual installation guide.")
    matches = [row for row in rows if row.get("name") == MARKETPLACE]
    if not matches:
        return False
    field = "root" if host == "codex" else "path"
    if len(matches) != 1 or not isinstance(matches[0].get(field), str):
        raise ValueError(f"Cannot verify {host}'s existing {MARKETPLACE} source. Nothing was changed.")
    if Path(matches[0][field]).resolve() != ROOT:
        raise ValueError(f"{host} already uses {MARKETPLACE} for another source. Nothing was changed. Inspect its marketplace settings.")
    return True


def install(args):
    sys.path.insert(0, str(ROOT / "plugins/miso-stack/scripts"))
    from miso_package import check, links

    targets = select_targets(args)
    if not targets:
        print("Cancelled. No harness settings changed.")
        return
    missing = [host for host in targets if not shutil.which(host)]
    if missing:
        raise ValueError("Harness not found on PATH: " + ", ".join(missing))
    check()
    shared = any(host in targets for host in ("grok", "opencode"))
    link_args = SimpleNamespace(target=str(Path.home() / ".agents/skills"), apply=False)
    if shared:
        links(link_args)
    existing = {host: registered(host) for host in targets if host in ("codex", "claude")}
    print("\nInstalling MisoStack for " + ", ".join(targets) + "…", flush=True)
    for host, present in existing.items():
        commands = [] if present else [[host, "plugin", "marketplace", "add", str(ROOT)]]
        commands.append([host, "plugin", "add" if host == "codex" else "install", PLUGIN])
        for command in commands:
            if args.dry_run:
                print("Would run: " + " ".join(command), flush=True)
            if not args.dry_run:
                run(command)
        if not args.dry_run:
            print(f"  ✓ {host} plugin installed", flush=True)
    if shared:
        print(("Would link" if args.dry_run else "Linking") + " shared skills into ~/.agents/skills/", flush=True)
        if not args.dry_run:
            links(SimpleNamespace(target=link_args.target, apply=True))
            print("  ✓ Shared skills installed", flush=True)
    print("Preview complete; nothing changed." if args.dry_run else "Installed. Start a fresh session and ask for miso.")
    if not args.dry_run and "claude" in targets:
        print("Claude Code also accepts /miso-stack:miso.")


def main():
    parser = argparse.ArgumentParser(description="Choose harnesses interactively, or select them by name.")
    parser.add_argument("harnesses", nargs="*", metavar="HARNESS", help="codex, claude, grok, opencode (default: interactive picker)")
    parser.add_argument("--yes", "-y", action="store_true", help="Install for all detected harnesses without prompting.")
    parser.add_argument("--dry-run", action="store_true", help="Check prerequisites and preview changes without installing.")
    args = parser.parse_args()
    unknown = sorted(set(args.harnesses) - set(HOSTS))
    if unknown:
        parser.error("Unknown harness: " + ", ".join(unknown))
    if sys.version_info < (3, 10):
        parser.error("Python 3.10 or later is required.")
    try:
        install(args)
    except (KeyboardInterrupt, EOFError):
        parser.exit(130, "\nInterrupted. If installation had started, earlier successful steps remain.\n")
    except (OSError, ValueError, subprocess.TimeoutExpired) as error:
        parser.exit(1, str(error) + "\nInstallation stopped. Earlier successful steps are retained; correct the error and rerun.\n")


if __name__ == "__main__":
    main()
