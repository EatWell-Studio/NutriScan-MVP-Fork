#!/usr/bin/env python3
"""Check commit messages in a range against CONTRIBUTING §3 (ADR 0023).

Usage: check_commits.py <base-sha> <head-sha>
"""

import re
import subprocess
import sys

SUBJECT = re.compile(r"(app|api|schema|docs|ci|chore): \S")
MAX_SUBJECT = 72
TASK_ID = r"[A-Z][A-Z0-9]*-(?:\d+|R)"
REFS = re.compile(rf"Refs: {TASK_ID}(?:, {TASK_ID})*")
# Tool attribution is not allowed in commit messages (CONTRIBUTING §3).
ATTRIBUTION = [
    re.compile(r"(?i)^co-authored-by:.*(claude|anthropic)"),
    re.compile(r"(?i)generated with .*claude"),
]


def commits(base: str, head: str) -> list[tuple[str, str]]:
    out = subprocess.run(
        ["git", "log", "--format=%H%x00%B%x1e", f"{base}..{head}"],
        check=True, capture_output=True, text=True,
    ).stdout
    result = []
    for record in out.split("\x1e"):
        record = record.strip("\n")
        if record:
            sha, message = record.split("\x00", 1)
            result.append((sha, message.strip()))
    return result


def check(message: str) -> list[str]:
    lines = message.splitlines()
    subject = lines[0] if lines else ""
    errors = []
    if not SUBJECT.match(subject):
        errors.append("subject must start with app:, api:, schema:, docs:, ci: or chore: followed by a space")
    if len(subject) > MAX_SUBJECT:
        errors.append(f"subject is {len(subject)} characters; the limit is {MAX_SUBJECT}")
    if subject.endswith("."):
        errors.append("subject must not end with a period")
    if not any(REFS.fullmatch(line.strip()) for line in lines[1:]):
        errors.append("body needs a line like 'Refs: P1-3' or 'Refs: C-1, C-2'")
    if any(p.search(line) for p in ATTRIBUTION for line in lines):
        errors.append("remove tool attribution lines")
    return errors


def main() -> int:
    if len(sys.argv) != 3:
        print(__doc__)
        return 2
    failed = 0
    for sha, message in commits(sys.argv[1], sys.argv[2]):
        subject = message.splitlines()[0] if message else ""
        errors = check(message)
        if errors:
            failed += 1
            for error in errors:
                print(f"::error::{sha[:7]} \"{subject}\": {error}")
        else:
            print(f"ok   {sha[:7]} {subject}")
    if failed:
        print(f"{failed} commit(s) do not follow CONTRIBUTING §3")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
