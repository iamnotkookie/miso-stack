import json
import os
from pathlib import Path
import signal
import subprocess
import tempfile
import time

from miso_io import create_json, evidence, lock, now, require, text


OUTPUT_LIMIT = 128 * 1024


def read_output(stream):
    size = stream.tell()
    stream.seek(0)
    output = stream.read(OUTPUT_LIMIT).decode("utf-8", errors="replace")
    return output, size > OUTPUT_LIMIT


def record(args):
    path = Path(args.path)
    command = args.command[1:] if args.command and args.command[0] == "--" else args.command
    require(command, "Supply a command after --.")
    require(0 < args.timeout <= 3600, "Timeout must be greater than zero and at most 3600 seconds.")
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("x") as destination:
        started = time.monotonic()
        with tempfile.TemporaryFile() as stdout, tempfile.TemporaryFile() as stderr:
            try:
                process = subprocess.Popen(command, stdout=stdout, stderr=stderr, start_new_session=True)
            except OSError as error:
                status, code = "error", None
                stderr.write(str(error).encode())
            else:
                try:
                    code = process.wait(timeout=args.timeout)
                    status = "pass" if code == 0 else "fail"
                except subprocess.TimeoutExpired:
                    os.killpg(process.pid, signal.SIGKILL)
                    process.wait()
                    status, code = "timeout", None
            out, out_cut = read_output(stdout)
            err, err_cut = read_output(stderr)
        result = {"version": 1, "timestamp": now(), "cwd": str(Path.cwd()), "command": command,
                  "status": status, "exit_code": code, "duration_seconds": round(time.monotonic() - started, 4),
                  "stdout": out, "stderr": err, "output_truncated": out_cut or err_cut}
        json.dump(result, destination, indent=2)
        destination.write("\n")
    require(status == "pass", f"Command {status}. Evidence saved to {path}.")
    return {"status": status, "evidence": str(path), "exit_code": code}


def trail(args):
    path = Path(args.path)
    if args.trail_command == "show":
        require(path.stat().st_size <= 4 * 1024 * 1024, "Trail is too large. Read a bounded range with a JSONL tool.")
        return {"entries": [json.loads(line) for line in path.read_text().splitlines() if line.strip()]}
    proof = evidence(Path.cwd(), args.evidence)
    row = {"timestamp": now(), "decision": text(args.decision, "decision"), "reason": text(args.reason, "reason"),
           "result": text(args.result, "result"), "evidence_base": str(Path.cwd()), "evidence": proof}
    with lock(path):
        with path.open("a") as stream:
            stream.write(json.dumps(row) + "\n")
            stream.flush()
            os.fsync(stream.fileno())
    return {"appended": str(path), "entry": row}
