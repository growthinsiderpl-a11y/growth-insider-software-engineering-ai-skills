---
name: growth-insider-software-engineering-ai-skills
description: Structured software engineering operating skill for architecture, implementation, repository delivery, maintainability, testing, reliability, frontend systems, secure coding, developer workflows, and technical SEO where code changes are required. Use when the user needs a design, implementation plan, review, validation approach, or deterministic engineering support tied to code and operational constraints. Do not use for product strategy, prioritization, discovery, or marketing planning.
license: MIT
metadata:
  title: Growth Insider Software Engineering AI Skills
  product: Growth Insider Software Engineering AI Skills
  product_id: growth-insider-software-engineering-ai-skills
  version: 1.0.0-rc.1
  author: Growth Insider
  maintainer: Growth Insider
  publisher: Growth Insider
  organization: Growth Insider
  website: https://growthinsider.pl/en/
  contact: support@growthinsider.pl
  location: Wrocław, Poland
  copyright: Copyright (c) 2026 Growth Insider
  status: release-candidate
  architecture: compact-skill-hubs-playbooks-tools
  compatibility: Designed for Agent Skills compatible runtimes that can read markdown, optionally run local scripts, and preserve user control over code changes, testing, and release actions.
---

# Growth Insider Software Engineering AI Skills

Turn engineering requests into evidence-grounded designs, implementation plans, code-quality decisions, release-safe workflows, and reviewable outputs.

This package does not simulate a role such as "a developer" or "a CTO." It starts from the software problem, the real technical constraint, the quality of the code evidence, and the minimum sufficient engineering move.

## Use this skill when

- the user needs software architecture, system design, or dependency-boundary reasoning
- the request is implementation planning, repository construction, API or service design, or frontend code structure
- code quality, refactoring, testing, release safety, observability, or secure coding is the core problem
- deterministic local checks can clarify maintainability, dependency rules, release evidence, design tokens, or technical SEO artifacts
- the task is technical SEO only because the fix requires code, templates, routing, metadata generation, or site-architecture changes

## Do not use this skill when

- the request is primarily product strategy, discovery, JTBD, prioritization, or roadmap governance
- the request is marketing strategy, offers, retention marketing, lead magnets, launch communications, or press activity
- the user wants generic brainstorming with no repository, implementation, or operational consequence
- the main work is legal, tax, regulatory, or formal security assurance beyond issue spotting and safe escalation

## Operating philosophy

Always follow this sequence:

`Business Context -> Real Constraint -> Evidence -> Minimum Sufficient Solution -> Implementation -> Measurement -> Review`

Prefer the smallest engineering move that resolves the real constraint and can be validated.

## Evidence rules

Classify material claims as:

- `FACT_USER`
- `FACT_FILE`
- `FACT_TOOL`
- `FACT_EXTERNAL`
- `CALCULATION`
- `ASSUMPTION`
- `HYPOTHESIS`
- `UNKNOWN`

Additional labels may be used when relevant: `EXAMPLE`, `HEURISTIC`, `BENCHMARK`, `POLICY`.

Read `references/evidence-and-uncertainty.md` when the request has architectural risk, release sensitivity, security implications, or unresolved unknowns.

## Workflow

### 1. Frame the engineering problem

State the target behavior, affected surfaces, operational constraints, evidence available, and what technical decision or code change the user needs.

### 2. Diagnose the real constraint

Determine whether the bottleneck is primarily:

- architecture and system boundaries
- repository and implementation structure
- maintainability and refactoring pressure
- test strategy or validation confidence
- release safety, reliability, or observability
- frontend implementation quality
- accessibility, performance, or web quality
- technical SEO requiring code changes
- developer workflow and delivery operations

### 3. Route

Load only the relevant hub from `references/hubs/`, then a focused playbook from `references/playbooks/`, then a deterministic script from `scripts/` only if it answers a concrete engineering question.

### 4. Decide the method

Prefer the minimum sufficient method:

- direct recommendation for a bounded implementation question
- one hub plus one playbook for most specialist work
- multiple hubs only when architecture, testing, release, and frontend concerns materially interact

### 5. Produce the artifact

Valid outputs include:

- architecture assessment
- repository scaffold plan
- maintainability review
- refactor sequence
- test strategy
- release gate
- observability baseline
- UI implementation review
- accessibility or performance remediation plan
- technical SEO engineering diagnosis

### 6. Measure and review

Every non-trivial answer should include expected signals, validation steps, stop conditions or release cautions when relevant, and what would falsify the recommendation.

## Boundary routing

Use this repository for architecture, code, tests, delivery, reliability, and engineering-owned technical SEO.

Escalate to other skill families when the center of gravity shifts:

- market, channel, messaging, offer, or growth planning -> marketing skill
- product strategy, discovery, prioritization, or behavioral product design -> product skill

See `docs/cross-skill-routing-boundaries.md`.

## Tool discipline

Registered scripts return deterministic JSON, publish their schema via `--schema`, and never depend on the network. Use them when structure validation or explicit calculations reduce ambiguity, not as a replacement for engineering judgment.

- Codebase inventory: `scripts/architecture/inventory_codebase.py`
- Dependency rules: `scripts/architecture/validate_dependency_direction.py`
- Maintainability findings: `scripts/quality/find_maintainability_violations.py`
- Design tokens: `scripts/quality/generate_design_tokens.py`
- Release evidence gate: `scripts/release/validate_release_readiness.py`
- Offline technical SEO artifacts: `scripts/seo/check_technical_seo_artifacts.py`

## Safety and misuse warnings

- Do not fabricate architecture constraints, test evidence, or production readiness.
- Do not present maintainability heuristics as an objective debt score.
- Do not claim secure or production-ready status from a partial review.
- Do not imply search-ranking outcomes from offline technical SEO checks.
- Do not present out-of-scope product or marketing work as if this package owns it.

## Progressive disclosure

Load in this order:

1. `references/capability-catalog.md`
2. relevant hub in `references/hubs/`
3. matching playbook in `references/playbooks/`
4. deterministic tool schema if validation is needed
5. example request or adapter only if the runtime or format requires it

Machine-readable inventory lives in `manifest.json`.
