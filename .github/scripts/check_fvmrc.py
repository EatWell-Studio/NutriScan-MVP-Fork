#!/usr/bin/env python3
"""Check the .fvmrc constraints from ADR 0025.

1. The Flutter version is a plain stable release number (e.g. 3.47.5).
2. "flutter" is the first key of the JSON object.
"""

import json
import re
import sys
from pathlib import Path

STABLE_VERSION = re.compile(r"\d+\.\d+\.\d+")


def check(path: Path) -> list[str]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return [f"cannot read {path} as JSON: {exc}"]
    if not isinstance(data, dict) or not data:
        return [f"{path} must be a non-empty JSON object"]

    errors = []
    first_key = next(iter(data))
    if first_key != "flutter":
        errors.append(f'the first key must be "flutter", found "{first_key}"')
    version = data.get("flutter")
    if not isinstance(version, str) or not STABLE_VERSION.fullmatch(version):
        errors.append(f'"flutter" must be a stable release number like 3.47.5, found {version!r}')
    return errors


def main() -> int:
    path = Path(sys.argv[1] if len(sys.argv) > 1 else ".fvmrc")
    errors = check(path)
    for error in errors:
        print(f"::error file={path}::{error}")
    if errors:
        return 1
    print(f"{path} is valid (ADR 0025)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
