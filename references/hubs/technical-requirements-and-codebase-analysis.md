# Technical Requirements and Codebase Analysis

Use this hub when the first job is understanding the codebase and translating ambiguous requests into technical requirements: repository inventory, affected surfaces, constraints, implementation implications, and the evidence needed before writing or changing code.

## What This Hub Owns

- technical requirement extraction from code and stated intent
- codebase inventory and impact surface mapping
- constraint identification for runtime, data, and interfaces
- translation of vague asks into implementation-ready statements
- gap analysis between current behavior and requested behavior
- cross-module traceability for the affected path
- technical unknown management before large changes
- example and artifact collection for grounded implementation
- requirements handoff into architecture, implementation, or testing work
- scope clarification through code evidence rather than speculation
- initial repository analysis for inherited or legacy systems
- problem framing that keeps marketing and product work out of engineering scope

## What This Hub Does Not Own

- market requirement discovery
- roadmap priority decisions
- business-case creation not tied to implementation
- campaign briefs or messaging
- feature desirability debates without technical consequence
- organizational planning
- copy editing of external-facing content
- generic brainstorming detached from repository evidence

## Questions To Answer First

- What exact behavior or artifact must change?
- Which repository paths are in play, and which are not?
- What current behavior is proven from code versus assumed by the requester?
- Where is the source of truth for the affected rule today?
- What adjacent systems can break if this changes?
- Which interfaces or data contracts will feel the change first?
- What is blocked by missing evidence from the codebase?
- What requirements are actually implementation constraints in disguise?
- Which parts of the ask belong to marketing or product instead?
- How can the request be decomposed into reviewable technical slices?
- What acceptance evidence is realistic for this repository?
- What ambiguity should be preserved as an explicit unknown?

## Required Inputs

- user request or ticket text
- repository paths or modules suspected to be relevant
- runtime entry points and integration boundaries
- available docs, examples, or sample outputs
- known environment, language, or framework constraints
- current bugs, incidents, or complaints tied to the request
- existing tests or missing coverage around the area
- deployment or release sensitivity of the affected path
- ownership cues from the repository structure
- historical context if the code is legacy or recently migrated
- requested deliverable type such as design, code, or audit
- hard boundaries the user already provided

## Evidence Signals

- file tree and language distribution
- imports or dependencies indicating coupling
- tests showing intended behavior
- docs contradicting or confirming current implementation
- configuration values that shape the execution path
- generated artifacts revealing output rules
- churn hotspots suggesting risk of accidental regressions
- naming mismatches between code and request language
- missing seams where a change will be hard to isolate
- places where the ask reaches beyond engineering ownership

## Working Rules

- Describe what the code must do, not who the model should pretend to be.
- Keep requirements falsifiable and implementation-relevant.
- Start with repository evidence before proposing structure.
- State unknowns early to prevent invented certainty.
- Do not convert marketing or product ambiguity into engineering busywork.
- Prefer one precise requirement over a vague manifesto.
- Map requirements to code surfaces explicitly.
- Separate current state, target state, and migration path.
- A codebase inventory is useful when it drives a decision.
- Use deterministic analysis tools when they clarify scope.
- Avoid broad rewrites as a substitute for requirement clarity.
- When ownership crosses skill boundaries, say so plainly.

## Recommended Workflow

- Restate the request in technical outcome terms.
- Inventory the codebase surface involved.
- Collect facts from files, tests, and generated outputs.
- Separate mandatory constraints from convenient ideas.
- Write implementation-facing requirements.
- Identify unknowns and evidence gaps.
- Route the work to the right hub or playbook.
- Define acceptance evidence for the next phase.
- Bound scope to what the repository can actually support.
- Keep ownership boundaries visible throughout.

## Common Failure Modes

- turning vague asks into larger vague plans
- assuming a codebase pattern from one folder name
- writing requirements that cannot be validated
- inventing constraints because the repository is unfamiliar
- missing the one file that actually controls behavior
- collapsing product ambiguity into engineering architecture work
- treating existing docs as true when code disagrees
- producing a long analysis with no implementation consequence
- skipping acceptance evidence until after coding begins
- failing to retire out-of-scope requests clearly

## Expected Deliverables

- technical requirement statement
- affected-surface inventory
- current-versus-target behavior notes
- explicit constraints list
- ownership boundary statement
- unknowns and follow-up evidence needs
- recommended hub or playbook route
- acceptance evidence outline
- repository impact summary
- implementation sequencing hints

## Hand-offs and Escalation

- to architecture when boundary or topology decisions are needed
- to implementation planning when scope is ready to build
- to testing when validation strategy must be designed early
- to release readiness when risk is already visible
- to frontend or SEO work when output surfaces dominate
- to maintainability review when the request exposes code health debt
- to product or marketing when the ask is misrouted
- to security review when the requirement touches sensitive flows

## Playbooks To Load Next

- `references/playbooks/architecture-boundary-assessment.md`
- `references/playbooks/system-design-decision-process.md`
- `references/playbooks/repository-scaffolding-workflow.md`
- `references/playbooks/test-strategy-design.md`

## Deterministic Tools

- `scripts/architecture/inventory_codebase.py`
- `scripts/quality/find_maintainability_violations.py`

## Review Checklist

- Technical outcome is clearly stated.
- Repository evidence supports the analysis.
- Affected paths are named explicitly.
- Constraints are actionable.
- Unknowns are documented.
- Acceptance evidence is realistic.
- Routing boundary is clear.
- Non-goals prevent scope drift.
- The analysis can lead to implementation.
- The analysis avoids role-play framing.
- Current behavior and target behavior are separated.
- Integration impacts are visible.
- Legacy assumptions are challenged by code facts.
- Risk is proportionate to the requested change.
- Tool outputs remain deterministic and inspectable.
- Cross-skill retirements are explicit.
- No external research is required for core understanding.
- The result helps the next engineer act quickly.
- The repository stays the center of gravity.
- The package keeps engineering ownership narrow and clean.

## Closing Rule

Keep the answer inside engineering ownership. If the best next move is product strategy, discovery, or marketing planning, state that plainly and hand off rather than stretching this hub beyond its remit.

## Analysis Field Notes

- Technical requirement framing is most useful when it tells engineers what must be true after the change, not merely what was requested in natural language.
- Repository analysis should stay proportional; the goal is to identify the evidence needed for action, not to narrate the whole codebase for its own sake.
- Impact analysis becomes more valuable when it names both touched surfaces and intentionally untouched surfaces.
- Vague requests often contain hidden acceptance criteria that appear only after code paths are traced explicitly.
- A good analysis distinguishes repository facts from remembered team folklore or assumptions carried from other systems.
- Clarifying ownership early prevents engineering work from absorbing product or marketing ambiguity by default.
- Codebase inventory tools help most when their output leads directly to routing or scope decisions.
- The first technical summary should reduce confusion enough that the next phase can stay narrow.
- Analysis quality is visible when later implementation work needs fewer corrective reinterpretations.
