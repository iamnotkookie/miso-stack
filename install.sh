#!/bin/sh
set -eu
MISOSTACK_ROOT=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
exec python3 "$MISOSTACK_ROOT/scripts/install.py" "$@"
