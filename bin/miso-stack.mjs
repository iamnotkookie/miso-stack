#!/usr/bin/env node
import { readFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';
import { spawnSync } from 'node:child_process';

const root = dirname(dirname(fileURLToPath(import.meta.url)));
const [command, ...args] = process.argv.slice(2);

if (command === '--version' || command === '-v') {
  console.log(JSON.parse(readFileSync(join(root, 'package.json'), 'utf8')).version);
} else if (!command || command === '--help' || command === '-h') {
  console.log(`MisoStack

Usage: miso-stack install [codex claude grok opencode] [--yes] [--dry-run]

Without harness names, choose from detected harnesses in an interactive picker.
Use --yes to install for all detected harnesses without prompting.
Requires Python 3.10+ and a supported harness on PATH.
Keep this package installed: skill links refer to its source.
`);
} else if (command !== 'install') {
  console.error(`Unknown command: ${command}. Use miso-stack --help.`);
  process.exitCode = 2;
} else if (root.split(/[\\/]/).includes('_npx') && !args.includes('--dry-run') && !args.includes('--help')) {
  console.error('Install from a stable location: npm install -g miso-stack. Temporary npx cache paths cannot own shared skill links.');
  process.exitCode = 1;
} else {
  const result = spawnSync('python3', [join(root, 'scripts/install.py'), ...args], {
    stdio: 'inherit',
    env: { ...process.env, PYTHONDONTWRITEBYTECODE: '1' },
  });
  if (result.error) {
    console.error(`Cannot start Python 3: ${result.error.message}. Install Python 3.10 or later and retry.`);
    process.exitCode = 1;
  } else {
    process.exitCode = result.status ?? 1;
  }
}
