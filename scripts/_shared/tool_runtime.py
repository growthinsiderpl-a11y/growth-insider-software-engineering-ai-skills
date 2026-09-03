#!/usr/bin/env python3
"""Shared deterministic runtime for Growth Insider engineering tools."""

from __future__ import annotations

import argparse
import json
import math
import statistics
import sys
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from typing import Any


class InputError(ValueError):
    """Raised when supplied data violates an explicit contract."""


def obj(required: list[str], properties: dict[str, Any]) -> dict[str, Any]:
    return {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "type": "object",
        "required": required,
        "additionalProperties": True,
        "properties": properties,
    }


def record(required: list[str], properties: dict[str, Any]) -> dict[str, Any]:
    return {"type": "object", "required": required, "additionalProperties": True, "properties": properties}


TEXT = {"type": "string", "minLength": 1}
NON_NEGATIVE = {"type": "number", "minimum": 0}
INTEGER = {"type": "number", "minimum": 0}
BOOLEAN = {"type": "boolean"}


SPECS: dict[str, dict[str, Any]] = {
    "inventory_codebase": {
        "description": "Inventory a codebase snapshot into file, extension, and directory counts.",
        "schema": obj(
            ["entries"],
            {
                "entries": {
                    "type": "array",
                    "minItems": 1,
                    "items": record(
                        ["path", "kind", "bytes", "lines"],
                        {
                            "path": TEXT,
                            "kind": TEXT,
                            "bytes": NON_NEGATIVE,
                            "lines": NON_NEGATIVE,
                        },
                    ),
                },
            },
        ),
        "formulas": [
            "file_count = count(entries where kind == file)",
            "total_bytes = sum(bytes)",
            "extension_count[ext] = count(files by extension)",
        ],
    },
    "validate_dependency_direction": {
        "description": "Validate dependency edges against an explicit allowed layer graph.",
        "schema": obj(
            ["layers", "components", "dependencies"],
            {
                "layers": {
                    "type": "array",
                    "minItems": 1,
                    "items": record(["name", "allowed_to_depend_on"], {"name": TEXT, "allowed_to_depend_on": {"type": "array", "items": TEXT}}),
                },
                "components": {
                    "type": "array",
                    "minItems": 1,
                    "items": record(["id", "layer"], {"id": TEXT, "layer": TEXT}),
                },
                "dependencies": {
                    "type": "array",
                    "minItems": 0,
                    "items": record(["source", "target"], {"source": TEXT, "target": TEXT}),
                },
            },
        ),
        "formulas": [
            "violation = source_layer not in allowed_to_depend_on[target_layer]? no; target_layer not in allowed_to_depend_on[source_layer]? yes",
        ],
    },
    "find_maintainability_violations": {
        "description": "Report observable maintainability findings from supplied file contents and metadata.",
        "schema": obj(
            ["files"],
            {
                "files": {
                    "type": "array",
                    "minItems": 1,
                    "items": record(
                        ["path", "content"],
                        {
                            "path": TEXT,
                            "content": TEXT,
                            "max_recommended_lines": NON_NEGATIVE,
                            "max_recommended_line_length": NON_NEGATIVE,
                        },
                    ),
                }
            },
        ),
        "formulas": [
            "file_too_large when line_count > max_recommended_lines",
            "long_line when len(line) > max_recommended_line_length",
            "marker_findings for TODO, FIXME, debugger, console.log, print(",
        ],
    },
    "generate_design_tokens": {
        "description": "Generate deterministic design token outputs and CSS variables.",
        "schema": obj(
            ["theme_name", "colors", "spacing", "font_sizes", "radii"],
            {
                "theme_name": TEXT,
                "colors": record([], {}),
                "spacing": record([], {}),
                "font_sizes": record([], {}),
                "radii": record([], {}),
                "shadows": record([], {}),
            },
        ),
        "formulas": [
            "css_variable = --<group>-<token>",
            "token_count = total named leaves across groups",
        ],
    },
    "validate_release_readiness": {
        "description": "Validate explicit release evidence for a production or package release.",
        "schema": obj(
            ["release"],
            {
                "release": record(
                    [
                        "change_name",
                        "tests_passed",
                        "rollback_ready",
                        "owner",
                        "observability_ready",
                        "smoke_checks_defined",
                        "known_risks",
                    ],
                    {
                        "change_name": TEXT,
                        "tests_passed": BOOLEAN,
                        "rollback_ready": BOOLEAN,
                        "owner": TEXT,
                        "observability_ready": BOOLEAN,
                        "smoke_checks_defined": BOOLEAN,
                        "known_risks": {"type": "array", "items": TEXT},
                        "migration_plan": TEXT,
                        "feature_flag": BOOLEAN,
                        "review_window_hours": NON_NEGATIVE,
                    },
                )
            },
        ),
        "formulas": [
            "ready when required booleans are true and review window exists",
            "missing_evidence = required evidence fields that are false or absent",
        ],
    },
    "check_technical_seo_artifacts": {
        "description": "Inspect supplied HTML for offline technical SEO signals.",
        "schema": obj(
            ["html"],
            {
                "html": TEXT,
                "base_url": TEXT,
            },
        ),
        "formulas": [
            "title_present = bool(title)",
            "image_alt_coverage = images_with_alt / total_images",
            "structured_data_blocks = count(ld+json scripts)",
        ],
    },
}


def _is_number(value: Any) -> bool:
    return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(float(value))


def _validate(value: Any, schema: dict[str, Any], path: str = "$") -> list[str]:
    errors: list[str] = []
    expected = schema.get("type")
    if expected == "object":
        if not isinstance(value, dict):
            return [f"{path} must be an object"]
        for field in schema.get("required", []):
            if field not in value:
                errors.append(f"{path}.{field} is required")
        for key, subschema in schema.get("properties", {}).items():
            if key in value:
                errors.extend(_validate(value[key], subschema, f"{path}.{key}"))
    elif expected == "array":
        if not isinstance(value, list):
            return [f"{path} must be an array"]
        if len(value) < schema.get("minItems", 0):
            errors.append(f"{path} must contain at least {schema.get('minItems', 0)} items")
        item_schema = schema.get("items")
        if item_schema:
            for index, item in enumerate(value):
                errors.extend(_validate(item, item_schema, f"{path}[{index}]"))
    elif expected == "string":
        if not isinstance(value, str) or len(value) < schema.get("minLength", 0):
            return [f"{path} must be a non-empty string"]
    elif expected == "number":
        if not _is_number(value):
            return [f"{path} must be a finite number"]
        numeric = float(value)
        if "minimum" in schema and numeric < schema["minimum"]:
            errors.append(f"{path} must be >= {schema['minimum']}")
    elif expected == "boolean":
        if not isinstance(value, bool):
            return [f"{path} must be a boolean"]
    return errors


def finite(value: Any, name: str, minimum: float | None = None) -> float:
    if not _is_number(value):
        raise InputError(f"{name} must be a finite number")
    number = float(value)
    if minimum is not None and number < minimum:
        raise InputError(f"{name} must be >= {minimum}")
    return number


class SeoParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.title: str | None = None
        self._in_title = False
        self.headings: dict[str, list[str]] = {"h1": [], "h2": [], "h3": []}
        self._tag_stack: list[str] = []
        self.images = 0
        self.images_with_alt = 0
        self.canonical: str | None = None
        self.description: str | None = None
        self.robots: str | None = None
        self.lang: str | None = None
        self.internal_links = 0
        self.external_links = 0
        self.schema_blocks = 0
        self.visible_text: list[str] = []
        self.viewport_present = False
        self._skip_text = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        data = dict(attrs)
        self._tag_stack.append(tag)
        if tag == "html":
            self.lang = data.get("lang")
        if tag == "title":
            self._in_title = True
        if tag in {"script", "style", "nav", "footer"}:
            self._skip_text = True
        if tag in {"h1", "h2", "h3"}:
            self.headings[tag].append("")
        if tag == "img":
            self.images += 1
            alt = data.get("alt")
            if alt is not None and alt.strip():
                self.images_with_alt += 1
        if tag == "meta":
            name = (data.get("name") or "").lower()
            if name == "description":
                self.description = data.get("content")
            if name == "robots":
                self.robots = data.get("content")
            if name == "viewport":
                self.viewport_present = True
        if tag == "link":
            rel = (data.get("rel") or "").lower()
            if "canonical" in rel:
                self.canonical = data.get("href")
        if tag == "a":
            href = data.get("href") or ""
            if href.startswith("http://") or href.startswith("https://"):
                self.external_links += 1
            elif href and not href.startswith("#") and not href.startswith("mailto:") and not href.startswith("javascript:"):
                self.internal_links += 1
        if tag == "script" and (data.get("type") or "").lower() == "application/ld+json":
            self.schema_blocks += 1

    def handle_endtag(self, tag: str) -> None:
        if self._tag_stack:
            self._tag_stack.pop()
        if tag == "title":
            self._in_title = False
        if tag in {"script", "style", "nav", "footer"}:
            self._skip_text = False

    def handle_data(self, data: str) -> None:
        text = data.strip()
        if not text:
            return
        if self._in_title:
            self.title = (self.title or "") + text
        if self._tag_stack:
            current = self._tag_stack[-1]
            if current in {"h1", "h2", "h3"} and self.headings[current]:
                self.headings[current][-1] += text + " "
        if not self._skip_text:
            self.visible_text.append(text)


def calculate(tool_id: str, data: dict[str, Any]) -> dict[str, Any]:
    if tool_id == "inventory_codebase":
        files = [entry for entry in data["entries"] if str(entry["kind"]).lower() == "file"]
        ext_counts = Counter()
        dir_counts = Counter()
        total_bytes = 0.0
        total_lines = 0.0
        for entry in files:
            path = str(entry["path"])
            ext = Path(path).suffix.lower() or "[no_extension]"
            top_dir = path.split("/", 1)[0] if "/" in path else "."
            ext_counts[ext] += 1
            dir_counts[top_dir] += 1
            total_bytes += finite(entry["bytes"], f"{path}.bytes", 0)
            total_lines += finite(entry["lines"], f"{path}.lines", 0)
        return {
            "file_count": len(files),
            "total_bytes": total_bytes,
            "total_lines": total_lines,
            "extensions": dict(sorted(ext_counts.items())),
            "top_directories": [{"path": name, "files": count} for name, count in dir_counts.most_common(10)],
        }

    if tool_id == "validate_dependency_direction":
        allowed = {item["name"]: set(item["allowed_to_depend_on"]) for item in data["layers"]}
        component_layer = {item["id"]: item["layer"] for item in data["components"]}
        violations = []
        for dep in data["dependencies"]:
            source = dep["source"]
            target = dep["target"]
            if source not in component_layer or target not in component_layer:
                raise InputError(f"unknown component in dependency: {source} -> {target}")
            source_layer = component_layer[source]
            target_layer = component_layer[target]
            if target_layer not in allowed.get(source_layer, set()):
                violations.append(
                    {
                        "source": source,
                        "source_layer": source_layer,
                        "target": target,
                        "target_layer": target_layer,
                        "rule": f"{source_layer} may not depend on {target_layer}",
                    }
                )
        return {"valid": not violations, "violation_count": len(violations), "violations": violations}

    if tool_id == "find_maintainability_violations":
        findings = []
        by_file = []
        for item in data["files"]:
            path = item["path"]
            content = item["content"]
            lines = content.splitlines()
            max_lines = int(item.get("max_recommended_lines", 400) or 400)
            max_len = int(item.get("max_recommended_line_length", 120) or 120)
            local = []
            if len(lines) > max_lines:
                local.append({"type": "file_too_large", "detail": f"{len(lines)} lines exceeds {max_lines}"})
            long_lines = [index + 1 for index, line in enumerate(lines) if len(line) > max_len]
            if long_lines:
                local.append({"type": "long_lines", "detail": f"{len(long_lines)} lines exceed {max_len}", "lines": long_lines[:10]})
            markers = {
                "TODO": "todo_marker",
                "FIXME": "fixme_marker",
                "console.log(": "debug_logging",
                "debugger": "debugger_statement",
                "print(": "print_statement",
            }
            for needle, finding_type in markers.items():
                hit_lines = [index + 1 for index, line in enumerate(lines) if needle in line]
                if hit_lines:
                    local.append({"type": finding_type, "detail": f"found {needle}", "lines": hit_lines[:10]})
            if "except:" in content:
                local.append({"type": "bare_except", "detail": "found bare except"})
            if local:
                by_file.append({"path": path, "findings": local})
                findings.extend(local)
        return {"violation_count": len(findings), "files": by_file}

    if tool_id == "generate_design_tokens":
        groups = {
            "color": data["colors"],
            "space": data["spacing"],
            "font-size": data["font_sizes"],
            "radius": data["radii"],
            "shadow": data.get("shadows", {}),
        }
        css_lines = [":root {"]
        token_count = 0
        for group, mapping in groups.items():
            for key, value in mapping.items():
                css_lines.append(f"  --{group}-{key}: {value};")
                token_count += 1
        css_lines.append("}")
        return {"theme_name": data["theme_name"], "token_count": token_count, "css": "\n".join(css_lines), "tokens": groups}

    if tool_id == "validate_release_readiness":
        release = data["release"]
        missing = []
        checks = {
            "tests_passed": bool(release["tests_passed"]),
            "rollback_ready": bool(release["rollback_ready"]),
            "observability_ready": bool(release["observability_ready"]),
            "smoke_checks_defined": bool(release["smoke_checks_defined"]),
            "owner": bool(str(release["owner"]).strip()),
            "review_window_hours": finite(release.get("review_window_hours", 0), "review_window_hours", 0) > 0,
        }
        for key, ok in checks.items():
            if not ok:
                missing.append(key)
        ready = not missing
        return {
            "change_name": release["change_name"],
            "ready": ready,
            "missing_evidence": missing,
            "known_risks": list(release["known_risks"]),
            "feature_flag": bool(release.get("feature_flag", False)),
            "migration_plan_present": bool(str(release.get("migration_plan", "")).strip()),
        }

    if tool_id == "check_technical_seo_artifacts":
        parser = SeoParser()
        parser.feed(data["html"])
        words = sum(len(chunk.split()) for chunk in parser.visible_text)
        cleaned = {key: [value.strip() for value in values if value.strip()] for key, values in parser.headings.items()}
        findings = []
        if not parser.title:
            findings.append("missing title")
        if not parser.description:
            findings.append("missing meta description")
        if not parser.canonical:
            findings.append("missing canonical")
        if not parser.lang:
            findings.append("missing html lang")
        if not parser.viewport_present:
            findings.append("missing viewport meta")
        if not cleaned["h1"]:
            findings.append("missing h1")
        return {
            "title": parser.title,
            "meta_description": parser.description,
            "meta_robots": parser.robots,
            "canonical": parser.canonical,
            "lang": parser.lang,
            "headings": cleaned,
            "image_count": parser.images,
            "image_alt_coverage": None if parser.images == 0 else parser.images_with_alt / parser.images,
            "internal_link_count": parser.internal_links,
            "external_link_count": parser.external_links,
            "structured_data_blocks": parser.schema_blocks,
            "word_count": words,
            "findings": findings,
        }

    raise InputError(f"Unknown tool: {tool_id}")


def run_tool(tool_id: str) -> int:
    spec = SPECS[tool_id]
    parser = argparse.ArgumentParser(description=spec["description"])
    parser.add_argument("--input", type=Path, help="Path to UTF-8 JSON input")
    parser.add_argument("--json", help="Inline JSON object")
    parser.add_argument("--schema", action="store_true", help="Print JSON Schema and exit")
    args = parser.parse_args()

    if args.schema:
        print(json.dumps(spec["schema"], ensure_ascii=False, indent=2, sort_keys=True))
        return 0

    try:
        if args.input:
            payload = json.loads(args.input.read_text(encoding="utf-8"))
        elif args.json:
            payload = json.loads(args.json)
        elif not sys.stdin.isatty():
            payload = json.load(sys.stdin)
        else:
            raise InputError("provide --input, --json, or JSON on stdin")
        if not isinstance(payload, dict):
            raise InputError("input must be a JSON object")
        errors = _validate(payload, spec["schema"])
        if errors:
            raise InputError(" | ".join(errors))
        result = calculate(tool_id, payload)
        print(json.dumps({"status": "OK", "tool_id": tool_id, "formulas": spec["formulas"], "benchmarks_injected": False, "result": result}, ensure_ascii=False, indent=2, sort_keys=True))
        return 0
    except (InputError, OSError, json.JSONDecodeError, TypeError, KeyError) as exc:
        print(json.dumps({"status": "ERROR", "tool_id": tool_id, "errors": [str(exc)]}, ensure_ascii=False), file=sys.stderr)
        return 2


def entrypoint(tool_id: str) -> None:
    raise SystemExit(run_tool(tool_id))
