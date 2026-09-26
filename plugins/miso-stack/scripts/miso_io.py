import contextlib
from datetime import datetime, timezone
import fcntl
import hashlib
import json
import os
from pathlib import Path
import tempfile


MAX_JSON_BYTES = 4 * 1024 * 1024


def now():
    return datetime.now(timezone.utc).isoformat()


def require(condition, message):
    if not condition:
        raise ValueError(message)


def text(value, field):
    require(isinstance(value, str) and bool(value.strip()), f"{field} must be nonempty text.")
    require(len(value) <= 10000, f"{field} exceeds 10000 characters.")
    return value


def read_json(path):
    path = Path(path)
    require(path.stat().st_size <= MAX_JSON_BYTES, f"JSON file is too large: {path}")
    return json.loads(path.read_text())


def create_json(path, data):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("x") as stream:
        json.dump(data, stream, indent=2)
        stream.write("\n")


def replace_json(path, data):
    path = Path(path)
    require(not path.is_symlink(), "Refusing to replace a symlink. Use the actual plan file.")
    descriptor, name = tempfile.mkstemp(prefix=".miso-", dir=path.parent)
    try:
        with os.fdopen(descriptor, "w") as stream:
            json.dump(data, stream, indent=2)
            stream.write("\n")
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(name, path)
    finally:
        if os.path.exists(name):
            os.unlink(name)


@contextlib.contextmanager
def lock(path):
    path = Path(path)
    require(not path.is_symlink(), "Refusing a symlink as mutable state.")
    path.parent.mkdir(parents=True, exist_ok=True)
    flags = os.O_CREAT | os.O_RDWR | getattr(os, "O_NOFOLLOW", 0)
    descriptor = os.open(str(path) + ".lock", flags, 0o600)
    with os.fdopen(descriptor, "w") as stream:
        fcntl.flock(stream, fcntl.LOCK_EX)
        try:
            yield
        finally:
            fcntl.flock(stream, fcntl.LOCK_UN)


def evidence(base, name):
    text(name, "evidence path")
    relative = Path(name)
    require(not relative.is_absolute(), "Evidence must use a relative path beneath the state file's directory.")
    resolved = (Path(base) / relative).resolve()
    require(resolved.is_relative_to(Path(base).resolve()), "Evidence escapes the state directory.")
    require(resolved.is_file(), f"Evidence file is missing: {name}")
    require(resolved.stat().st_size > 0, f"Evidence is empty: {name}")
    digest = hashlib.sha256()
    with resolved.open("rb") as stream:
        for chunk in iter(lambda: stream.read(65536), b""):
            digest.update(chunk)
    return {"path": name, "sha256": digest.hexdigest()}
