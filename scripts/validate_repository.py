#!/usr/bin/env python3
"""Validate the Growth Insider Software Engineering AI Skills repository."""

from __future__ import annotations

import json
import re
import sys
from hashlib import sha256
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_ID = "growth-insider-software-engineering-ai-skills"
EXPECTED_TITLE = "Growth Insider Software Engineering AI Skills"
EXPECTED_VERSION = "1.0.0-rc.1"
FORBIDDEN_STRINGS = ["Alireza Rezvani", "wondelai", "Act as a developer", "Act as a CTO"]
REQUIRED_HUBS = ['software-architecture-and-system-design.md', 'application-implementation-and-repository-delivery.md', 'code-quality-refactoring-and-maintainability.md', 'testing-validation-and-quality-engineering.md', 'release-reliability-and-production-readiness.md', 'frontend-ui-and-design-system-implementation.md', 'accessibility-performance-and-web-quality.md', 'technical-seo-and-site-architecture.md', 'technical-requirements-and-codebase-analysis.md', 'developer-workflow-and-delivery-operations.md']
REQUIRED_PLAYBOOKS = ['architecture-boundary-assessment.md', 'dependency-direction-review.md', 'system-design-decision-process.md', 'repository-scaffolding-workflow.md', 'code-maintainability-review.md', 'refactor-plan.md', 'test-strategy-design.md', 'production-readiness-gate.md', 'release-validation.md', 'observability-baseline.md', 'ui-implementation-quality.md', 'accessibility-implementation-checklist.md', 'performance-remediation-plan.md', 'technical-seo-engineering.md', 'secure-coding-review.md', 'api-service-design.md', 'ci-delivery-workflow.md']
REQUIRED_TOOLS = [
    "scripts/architecture/inventory_codebase.py",
    "scripts/architecture/validate_dependency_direction.py",
    "scripts/quality/find_maintainability_violations.py",
    "scripts/quality/generate_design_tokens.py",
    "scripts/release/validate_release_readiness.py",
    "scripts/seo/check_technical_seo_artifacts.py",
    "scripts/_shared/tool_runtime.py",
    "scripts/validate_repository.py",
    "scripts/validate_behavioral_evals.py",
]
MIN_HUB_LINES = 180
MIN_PLAYBOOK_LINES = 95


class Results:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def require(self, condition: bool, message: str) -> None:
        if not condition:
            self.errors.append(message)


def non_empty_lines(text: str) -> list[str]:
    return [line.strip() for line in text.splitlines() if line.strip()]


def repeated_line_overlap(a: str, b: str) -> int:
    lines_a = set(non_empty_lines(a))
    lines_b = set(non_empty_lines(b))
    generic = {"## When To Run It", "## Do Not Run It When", "## Inputs", "## Procedure", "## Decision Tests", "## Outputs", "## Failure Modes", "## Review and Follow-through", "## Evidence Reminder"}
    return len({line for line in lines_a & lines_b if line not in generic})


def main() -> int:
    results = Results()
    manifest = json.loads((ROOT / "manifest.json").read_text(encoding="utf-8"))
    package = manifest["package"]
    results.require(package["id"] == EXPECTED_ID, "package id mismatch")
    results.require(package["title"] == EXPECTED_TITLE, "package title mismatch")
    results.require(package["version"] == EXPECTED_VERSION, "package version mismatch")
    results.require(ROOT.name == EXPECTED_ID, "folder name mismatch")
    results.require((ROOT / "SKILL.md").is_file(), "missing SKILL.md")
    results.require((ROOT / "README.md").is_file(), "missing README.md")
    results.require((ROOT / "LICENSE").is_file(), "missing LICENSE")

    hub_files = sorted(path.name for path in (ROOT / "references" / "hubs").glob("*.md"))
    playbook_files = sorted(path.name for path in (ROOT / "references" / "playbooks").glob("*.md"))
    tool_files = sorted(str(path.relative_to(ROOT)).replace("\\", "/") for path in (ROOT / "scripts").rglob("*.py"))
    results.require(hub_files == sorted(REQUIRED_HUBS), "hub inventory mismatch")
    results.require(playbook_files == sorted(REQUIRED_PLAYBOOKS), "playbook inventory mismatch")
    results.require(set(tool_files) == set(REQUIRED_TOOLS), "tool inventory mismatch")

    hub_hashes = {}
    for path in (ROOT / "references" / "hubs").glob("*.md"):
        text = path.read_text(encoding="utf-8")
        line_count = len(text.splitlines())
        results.require(line_count >= MIN_HUB_LINES, f"hub too shallow: {path.name} ({line_count} lines)")
        body_hash = sha256("\n".join(text.splitlines()[1:]).strip().encode("utf-8")).hexdigest()
        hub_hashes.setdefault(body_hash, []).append(path.name)
    for names in hub_hashes.values():
        results.require(len(names) == 1, f"duplicate hub bodies: {', '.join(sorted(names))}")

    playbook_texts = {}
    playbook_body_hashes = {}
    for path in (ROOT / "references" / "playbooks").glob("*.md"):
        text = path.read_text(encoding="utf-8")
        lines = text.splitlines()
        line_count = len(lines)
        results.require(line_count >= MIN_PLAYBOOK_LINES, f"playbook too shallow: {path.name} ({line_count} lines)")
        body = "\n".join(lines[1:]).strip()
        playbook_texts[path.name] = body
        body_hash = sha256(body.encode("utf-8")).hexdigest()
        playbook_body_hashes.setdefault(body_hash, []).append(path.name)
    for names in playbook_body_hashes.values():
        results.require(len(names) == 1, f"duplicate playbook bodies: {', '.join(sorted(names))}")
    playbook_names = sorted(playbook_texts)
    for index, left in enumerate(playbook_names):
        for right in playbook_names[index + 1 :]:
            overlap = repeated_line_overlap(playbook_texts[left], playbook_texts[right])
            results.require(overlap < 28, f"playbooks too templated: {left} vs {right} ({overlap} repeated non-empty lines)")

    skill_text = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    results.require("Business Context -> Real Constraint -> Evidence -> Minimum Sufficient Solution -> Implementation -> Measurement -> Review" in skill_text, "missing philosophy sequence")
    results.require("Do not use this skill when" in skill_text, "missing negative boundaries")
    results.require("technical SEO where code changes are required" in skill_text, "missing technical SEO scope line")

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    results.require("Personalized AI Skills for Your Business" in readme, "README missing Personalized AI Skills section")
    results.require("About Growth Insider" in readme, "README missing About Growth Insider section")
    results.require(not readme.startswith(" "), "README must not begin with leading spaces")
    results.require(readme.lstrip().startswith("# "), "README must begin with an H1 heading")
    indented_public = [
        index + 1
        for index, line in enumerate(readme.splitlines())
        if line.startswith("    ") and line.strip() and not line.lstrip().startswith("|")
    ]
    # Allow intentional fenced code only; ordinary public paragraphs/headings/lists must not be indented 4+ spaces.
    in_fence = False
    bad_indent_lines: list[int] = []
    for index, line in enumerate(readme.splitlines(), start=1):
        if line.strip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        if line.startswith("    ") and line.strip() and not line.lstrip().startswith("|"):
            bad_indent_lines.append(index)
    results.require(not bad_indent_lines, f"README public content indented like a code block at lines: {bad_indent_lines[:8]}")
    results.require("NOT MODEL TESTED" in (ROOT / "docs" / "platform-compatibility.md").read_text(encoding="utf-8"), "platform compatibility missing model test boundary")

    csv_path = ROOT / "docs" / "capability-parity-matrix.csv"
    row_count = sum(1 for line in csv_path.read_text(encoding="utf-8-sig").splitlines()[1:] if line.strip())
    results.require(row_count == 346, f"expected 346 parity rows, found {row_count}")

    scan_text = []
    for path in ROOT.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in {".md", ".py", ".json", ".yaml", ".yml", ".cff", ".txt"}:
            continue
        rel = path.relative_to(ROOT).as_posix()
        if rel.startswith("tests/") or rel == "scripts/validate_repository.py":
            continue
        scan_text.append(path.read_text(encoding="utf-8", errors="replace"))
    all_text = "\n".join(scan_text)
    for token in FORBIDDEN_STRINGS:
        results.require(token not in all_text, f"forbidden legacy token present: {token}")

    for path in ROOT.rglob("*.json"):
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            results.errors.append(f"invalid json {path.relative_to(ROOT).as_posix()}: {exc}")
    for path in ROOT.rglob("*.py"):
        try:
            compile(path.read_text(encoding="utf-8"), str(path), "exec")
        except SyntaxError as exc:
            results.errors.append(f"python syntax error {path.relative_to(ROOT).as_posix()}: {exc}")

    print(json.dumps({"status": "PASS" if not results.errors else "FAIL", "errors": results.errors, "warnings": results.warnings}, indent=2))
    return 0 if not results.errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
