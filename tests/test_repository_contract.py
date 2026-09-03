from __future__ import annotations

import json
from hashlib import sha256
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = json.loads((ROOT / "manifest.json").read_text(encoding="utf-8"))


def test_identity() -> None:
    assert MANIFEST["package"]["id"] == "growth-insider-software-engineering-ai-skills"
    assert MANIFEST["package"]["title"] == "Growth Insider Software Engineering AI Skills"
    assert MANIFEST["package"]["version"] == "1.0.0-rc.1"


def test_hub_and_playbook_counts() -> None:
    assert len(MANIFEST["hubs"]) == 10
    assert len(MANIFEST["playbooks"]) >= 16


def test_hubs_and_playbooks_have_depth_and_unique_bodies() -> None:
    hub_paths = sorted((ROOT / "references" / "hubs").glob("*.md"))
    playbook_paths = sorted((ROOT / "references" / "playbooks").glob("*.md"))

    for path in hub_paths:
        assert len(path.read_text(encoding="utf-8").splitlines()) >= 180

    hashes = []
    for path in playbook_paths:
        lines = path.read_text(encoding="utf-8").splitlines()
        assert len(lines) >= 95
        hashes.append(sha256("\n".join(lines[1:]).strip().encode("utf-8")).hexdigest())

    assert len(hashes) == len(set(hashes))


def test_engineering_scope() -> None:
    text = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    assert "marketing skill" in text
    assert "product skill" in text
    assert "technical SEO where code changes are required" in text


def test_examples_and_tests_registered() -> None:
    for path in MANIFEST["examples"] + MANIFEST["tests"]:
        assert (ROOT / path).exists()
