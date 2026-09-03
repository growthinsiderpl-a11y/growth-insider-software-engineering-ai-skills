from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from _shared.tool_runtime import SPECS, _validate, calculate  # type: ignore  # noqa: E402


def load_cases():
    return json.loads((ROOT / "tests" / "business-tool-cases.json").read_text(encoding="utf-8"))["cases"]


def test_cases_cover_every_tool() -> None:
    tool_ids = {case["tool_id"] for case in load_cases()}
    assert tool_ids == set(SPECS)


def test_each_case_matches_schema_and_runs() -> None:
    for case in load_cases():
        assert _validate(case["input"], SPECS[case["tool_id"]]["schema"]) == []
        result = calculate(case["tool_id"], case["input"])
        assert isinstance(result, dict)
        assert result


def test_each_wrapper_supports_help_schema_and_json() -> None:
    for case in load_cases():
        wrapper = ROOT / case["path"]
        help_result = subprocess.run([sys.executable, str(wrapper), "--help"], cwd=ROOT, text=True, capture_output=True, check=False)
        assert help_result.returncode == 0
        assert "--schema" in help_result.stdout

        schema_result = subprocess.run([sys.executable, str(wrapper), "--schema"], cwd=ROOT, text=True, capture_output=True, check=False)
        assert schema_result.returncode == 0
        schema = json.loads(schema_result.stdout)
        assert schema["$schema"] == "https://json-schema.org/draft/2020-12/schema"

        ok_result = subprocess.run([sys.executable, str(wrapper), "--json", json.dumps(case["input"])], cwd=ROOT, text=True, capture_output=True, check=False)
        assert ok_result.returncode == 0
        payload = json.loads(ok_result.stdout)
        assert payload["status"] == "OK"
        assert payload["tool_id"] == case["tool_id"]

        bad_result = subprocess.run([sys.executable, str(wrapper), "--json", "{}"], cwd=ROOT, text=True, capture_output=True, check=False)
        assert bad_result.returncode != 0
        payload = json.loads(bad_result.stderr)
        assert payload["status"] == "ERROR"
