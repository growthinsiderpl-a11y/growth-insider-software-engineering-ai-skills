#!/usr/bin/env python3
"""Validate behavioral evaluation fixtures."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    payloads = [
        ROOT / "tests" / "routing-safety-cases.json",
        ROOT / "tests" / "domain-behavior-cases.json",
    ]
    errors: list[str] = []
    for path in payloads:
        data = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(data.get("cases"), list) or not data["cases"]:
            errors.append(f"{path.name}: missing cases")
        for index, case in enumerate(data.get("cases", [])):
            for field in ["id", "request", "expected_behavior"]:
                if field not in case:
                    errors.append(f"{path.name}: case {{index}} missing {{field}}")
    print(json.dumps({"status": "PASS" if not errors else "FAIL", "errors": errors}, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
