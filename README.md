# Growth Insider Software Engineering AI Skills

[![Release](https://img.shields.io/badge/release-v1.0.0-rc.1-175CD3)](CHANGELOG.md)
[![License: MIT](https://img.shields.io/badge/license-MIT-12B76A)](LICENSE)
[![Format: Agent Skills](https://img.shields.io/badge/format-Agent%20Skills-7A5AF8)](https://agentskills.io/specification)
[![Validation: local](https://img.shields.io/badge/validation-local%20static%20checks-F79009)](scripts/validate_repository.py)

Constraint-first software engineering skill infrastructure for teams, maintainers, consultants, and AI runtimes.

This repository turns vague requests such as "fix the architecture," "review this codebase," "is this release safe," "how should we structure the repository," or "why is the frontend hard to extend" into evidence-labeled technical analysis, bounded implementation guidance, deterministic validation, and reviewable delivery steps.

## Why This Exists

Many engineering prompts jump straight to patterns or slogans. That creates polished answers before the actual software constraint is clear.

Growth Insider uses a stricter sequence:

`Business Context -> Real Constraint -> Evidence -> Minimum Sufficient Solution -> Implementation -> Measurement -> Review`

The package does not begin with role-play. It begins with the code problem, the operational constraint, and the quality of the evidence available.

## What It Does

- covers architecture, repository delivery, maintainability, testing, release readiness, frontend implementation, accessibility, performance, technical SEO engineering, and delivery operations
- organizes knowledge into 10 substantive hubs and 17 focused playbooks
- provides 6 deterministic local tools plus repository and behavioral validators
- distinguishes facts, calculations, assumptions, hypotheses, heuristics, examples, and unknowns
- keeps external integrations out of the core release
- preserves strict routing boundaries against marketing and product ownership

## How It Works

1. Frame the software outcome, affected surfaces, constraints, and available evidence.
2. Diagnose the binding technical problem instead of optimizing everything.
3. Load the smallest relevant hub and playbook.
4. Run deterministic local tools only where they reduce ambiguity.
5. Produce a plan, review, audit, or implementation guide with validation and follow-through.

## Quick Start

1. Place the `growth-insider-software-engineering-ai-skills` folder in an Agent Skills compatible location.
2. Keep the folder name unchanged.
3. Start with a concrete engineering problem and any known constraints or repository context.
4. Let the runtime load `SKILL.md`, then only the referenced hubs, playbooks, and scripts needed for the task.

Example prompts:

- "Assess our architecture boundaries. Checkout, pricing, and fulfillment logic are split across handlers, jobs, and database triggers."
- "Design a repository scaffold for a new internal platform service with deterministic validation and public package docs."
- "Review this frontend implementation for maintainability, accessibility, and design-system readiness."
- "Tell me whether this release is production-ready. We have a migration, a feature flag, dashboards, and smoke tests."
- "Check these generated HTML files for technical SEO issues that require code changes, not content strategy."

## Decision Surface

The package is organized around engineering problems, not job-title simulation.

| Item | Value |
| --- | --- |
| Architecture and system design | boundaries, contracts, and trade-offs |
| Implementation and repository delivery | scaffolding, file layout, and slices |
| Code quality and refactoring | maintainability findings and phased cleanup |
| Testing and validation | risk-based confidence and local evaluation |
| Release and reliability | gates, rollout, rollback, and observability |
| Frontend systems | components, tokens, semantics, and state |
| Accessibility and performance | web quality remediation in code |
| Technical SEO engineering | crawlable artifacts and site architecture in code |
| Developer workflow | repository operations, CI, and contribution discipline |

## Repository Structure

```text
growth-insider-software-engineering-ai-skills/
├── SKILL.md
├── manifest.json
├── references/
│   ├── hubs/
│   └── playbooks/
├── scripts/
├── adapters/
├── examples/
├── docs/
├── tests/
└── .github/
```

## Platform Compatibility

The package follows the open [Agent Skills specification](https://agentskills.io/specification), is documented for current [OpenAI Build Skills guidance](https://learn.chatgpt.com/docs/build-skills), references current [Anthropic Agent Skills documentation](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview), and ships an OpenAI-oriented descriptor in `agents/openai.yaml`.

Compatibility claims in this release are limited to:

- `DESIGNED_FOR`: Agent Skills compatible runtimes
- `STATICALLY_VALIDATED`: repository structure, manifests, links, and schemas
- `LOCALLY_TESTED`: deterministic scripts and local tests
- `NOT MODEL TESTED`: no claim of live platform model execution

See [docs/platform-compatibility.md](docs/platform-compatibility.md).

## Personalized AI Skills for Your Business

The public package is a reusable engineering operating system. Personalized AI Skills go further by encoding a company’s actual repositories, service inventory, coding standards, dependency rules, release gates, support model, and approved delivery workflows.

Growth Insider can adapt this pattern to a specific software environment, including:

- codebase-specific routing and repository conventions
- approved architecture and review heuristics
- release and observability guardrails
- internal evaluation suites and contribution workflows
- domain-specific engineering examples and adapters

That is custom operating logic, not a generic prompt bundle.

## About Growth Insider

[Growth Insider](https://growthinsider.pl/en/) works across software and growth with a constraint-first approach. The aim is not to maximize complexity; it is to reach the minimum sufficient solution that matches the real constraint, can be implemented, can be measured, and can be reviewed.

Growth Insider is based in Wrocław, Poland. Contact: [support@growthinsider.pl](mailto:support@growthinsider.pl).

## Security and Privacy

The core package runs locally and ships no mandatory network integration. Scripts are deterministic and intended to analyze user-supplied inputs, repository files, or offline HTML artifacts.

## Trademarks and Non-Affiliation

References to OpenAI, ChatGPT, Codex, Anthropic, Claude, and Agent Skills describe interoperability targets and public documentation only. No partnership, certification, or endorsement is claimed.

## License

Released under the [MIT License](LICENSE). Copyright (c) 2026 Growth Insider
