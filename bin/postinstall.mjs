#!/usr/bin/env node
import { closeSync, openSync, writeSync } from 'node:fs';
import { spawnSync } from 'node:child_process';
import { fileURLToPath } from 'node:url';

const recovery = 'MisoStack CLI installed. Run miso-stack install to choose your harnesses.';

function setup() {
  if (process.env.npm_config_global !== 'true' || process.env.CI) {
    console.log(recovery);
    return;
  }
  let terminal;
  try {
    // npm captures lifecycle stdio. Use the terminal of the invoking shell.
    terminal = openSync('/dev/tty', 'r+');
  } catch (error) {
    if (!['ENXIO', 'ENODEV', 'ENOENT', 'ENOTTY', 'EACCES', 'EPERM'].includes(error.code)) {
      console.error(`Cannot open the setup terminal: ${error.message}`);
    }
    console.log(recovery);
    return;
  }
  try {
    // A shell background job must not read from the foreground user's terminal.
    const probe = spawnSync('python3', ['-c',
      'import os, sys; sys.exit(0 if os.tcgetpgrp(0) == os.getpgrp() else 1)'], {
      stdio: [terminal, 'ignore', 'ignore'], timeout: 5000,
    });
    if (probe.error) {
      writeSync(terminal, `Cannot start Python 3: ${probe.error.message}. Install Python 3.10 or later.\n${recovery}\n`);
      return;
    }
    if (probe.status !== 0) return;
    const cli = fileURLToPath(new URL('./miso-stack.mjs', import.meta.url));
    const result = spawnSync(process.execPath, [cli, 'install'], {
      stdio: [terminal, terminal, terminal],
    });
    if (result.error || result.status !== 0) {
      writeSync(terminal, 'MisoStack is installed, but harness setup did not finish. Run miso-stack install to retry.\n');
      if (result.error) writeSync(terminal, result.error.message + '\n');
    }
  } finally {
    closeSync(terminal);
  }
}

setup();
