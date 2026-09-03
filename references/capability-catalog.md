# Capability Catalog

This repository is organized as a compact public package:

- one routing entry in `SKILL.md`
- 10 engineering hubs in `references/hubs/`
- 17 focused playbooks in `references/playbooks/`
- deterministic local scripts in `scripts/`
- examples, adapters, tests, and public-release docs

## Hubs

- `references/hubs/software-architecture-and-system-design.md`: Use this hub when the hard part is shaping the system: boundaries, flows, capacity, failure isolation, dependency rules, and the trade-offs that determine whether implementation will stay coherent under change.
- `references/hubs/application-implementation-and-repository-delivery.md`: Use this hub when the challenge is turning intent into a working repository: scaffolding, conventions, file layout, implementation slices, migration-safe delivery, and maintaining a codebase others can continue to extend.
- `references/hubs/code-quality-refactoring-and-maintainability.md`: Use this hub when code already works, but the cost of change is rising: unclear names, deep functions, hidden coupling, unstable seams, noisy dependencies, and refactors that need to improve the code without breaking delivery momentum.
- `references/hubs/testing-validation-and-quality-engineering.md`: Use this hub when confidence is the bottleneck: test strategy, behavioral coverage, characterization before refactor, risk-based validation, evidence for release gates, and keeping quality engineering tied to real failure modes instead of ritual coverage growth.
- `references/hubs/release-reliability-and-production-readiness.md`: Use this hub when shipping safely is the core problem: release gates, rollout strategy, rollback posture, observability minimums, reliability trade-offs, dependency failure handling, and determining whether the change can be trusted in production.
- `references/hubs/frontend-ui-and-design-system-implementation.md`: Use this hub when the work is in the interface layer: component design, stateful UI implementation, design token translation, interaction quality, design-system structure, and converting visual or UX intent into maintainable frontend code.
- `references/hubs/accessibility-performance-and-web-quality.md`: Use this hub when the quality bar is defined by the lived web experience: semantic accessibility, interaction clarity, rendering efficiency, asset discipline, web vitals pressure, and the code changes required to make a site or app faster and more usable.
- `references/hubs/technical-seo-and-site-architecture.md`: Use this hub only when search visibility depends on engineering work: crawlable markup, metadata generation, routing, canonicalization, sitemap and robots artifacts, internal linking structures, and site architecture decisions that must be changed in code.
- `references/hubs/technical-requirements-and-codebase-analysis.md`: Use this hub when the first job is understanding the codebase and translating ambiguous requests into technical requirements: repository inventory, affected surfaces, constraints, implementation implications, and the evidence needed before writing or changing code.
- `references/hubs/developer-workflow-and-delivery-operations.md`: Use this hub when the code may be sound but delivery is not: local workflow, CI shape, repository validation, review loops, deterministic tooling, contribution experience, and operating practices that help engineers ship changes without avoidable friction.

## Playbooks

- `references/playbooks/architecture-boundary-assessment.md`: Assess whether the current or proposed system boundaries match responsibility, failure isolation, and change flow.
- `references/playbooks/dependency-direction-review.md`: Review whether dependencies move inward toward policy and domain intent rather than outward toward framework, UI, storage, or integration detail.
- `references/playbooks/system-design-decision-process.md`: Make a bounded architecture or system-design choice using explicit constraints, few serious options, operational trade-offs, and measurable follow-through.
- `references/playbooks/repository-scaffolding-workflow.md`: Create or reshape a repository so engineers can add features through a clear, testable, maintainable structure instead of ad hoc file growth.
- `references/playbooks/code-maintainability-review.md`: Review code for maintainability using explicit, observable traits that affect change cost rather than opinion or composite debt scores.
- `references/playbooks/refactor-plan.md`: Turn maintainability or architecture findings into a risk-aware refactor sequence that improves the code without disguising behavior changes or destabilizing release flow.
- `references/playbooks/test-strategy-design.md`: Design a risk-based validation approach that selects the cheapest faithful test layers for the behavior, failure modes, and rollout profile involved.
- `references/playbooks/production-readiness-gate.md`: Run an explicit readiness gate before shipping a meaningful change by requiring concrete evidence on rollout, rollback, observability, testing, operations, and unresolved risk.
- `references/playbooks/release-validation.md`: Validate the release path itself: preflight checks, smoke sequence, artifact correctness, rollout readiness, and the first signals that confirm the change is behaving in the wild.
- `references/playbooks/observability-baseline.md`: Define the minimum logs, metrics, traces, health indicators, and review windows required so a new or changed software path can be understood in production.
- `references/playbooks/ui-implementation-quality.md`: Review a frontend implementation for component boundaries, state ownership, semantic markup, state coverage, and design-system fitness in code.
- `references/playbooks/accessibility-implementation-checklist.md`: Run a code-focused accessibility implementation pass covering semantics, names, focus, keyboard support, status messaging, and resilient interaction states.
- `references/playbooks/performance-remediation-plan.md`: Plan a code-level remediation of user-facing performance issues by linking symptoms to bottlenecks, selecting the highest-payoff fixes, and defining measurable verification.
- `references/playbooks/technical-seo-engineering.md`: Investigate and remediate code-owned SEO issues by validating generated artifacts, tracing them back to templates or routing logic, and planning safe changes with explicit marketing handoff boundaries.
- `references/playbooks/secure-coding-review.md`: Review software changes for code-level security weaknesses, trust-boundary confusion, risky defaults, and missing validation without pretending to replace a dedicated security program.
- `references/playbooks/api-service-design.md`: Design or review an API or service contract so responsibilities, payloads, errors, idempotency, and evolution paths are coherent for both implementers and consumers.
- `references/playbooks/ci-delivery-workflow.md`: Shape a continuous-integration and delivery workflow that catches meaningful defects quickly, aligns with local development, and supports reliable releases without needless ceremony.

## Tooling

- `scripts/architecture/inventory_codebase.py`
- `scripts/architecture/validate_dependency_direction.py`
- `scripts/quality/find_maintainability_violations.py`
- `scripts/quality/generate_design_tokens.py`
- `scripts/release/validate_release_readiness.py`
- `scripts/seo/check_technical_seo_artifacts.py`
- `scripts/validate_repository.py`
- `scripts/validate_behavioral_evals.py`

## Philosophy

`Business Context -> Real Constraint -> Evidence -> Minimum Sufficient Solution -> Implementation -> Measurement -> Review`
