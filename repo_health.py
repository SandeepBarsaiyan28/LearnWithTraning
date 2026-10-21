#!/usr/bin/env python3
"""Run a few basic health checks on a Git repository."""

import argparse
import subprocess
from pathlib import Path


def run_git(path: Path, *args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *args],
        cwd=path,
        capture_output=True,
        text=True,
        check=False,
    )


def check_repository(path: Path) -> bool:
    root = run_git(path, "rev-parse", "--show-toplevel")
    if root.returncode != 0:
        print(f"FAIL: {path} is not inside a Git repository.")
        return False

    repository = Path(root.stdout.strip())
    print(f"Repository: {repository}")
    print("PASS: Git repository found.")

    readme = repository / "README.md"
    if readme.is_file():
        print("PASS: README.md found.")
    else:
        print("WARN: README.md is missing.")

    status = run_git(repository, "status", "--porcelain")
    if status.returncode != 0:
        print(f"FAIL: Could not read Git status: {status.stderr.strip()}")
        return False

    if status.stdout.strip():
        print("WARN: Repository has uncommitted changes.")
    else:
        print("PASS: Working tree is clean.")

    print("Health check complete.")
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description="Check basic Git repository health.")
    parser.add_argument(
        "path",
        nargs="?",
        default=".",
        help="repository path to check (defaults to the current directory)",
    )
    args = parser.parse_args()

    path = Path(args.path).expanduser().resolve()
    if not path.is_dir():
        print(f"FAIL: Directory does not exist: {path}")
        return 1

    return 0 if check_repository(path) else 1


if __name__ == "__main__":
    raise SystemExit(main())
