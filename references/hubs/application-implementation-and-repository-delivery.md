# Application Implementation and Repository Delivery

Use this hub when the challenge is turning intent into a working repository: scaffolding, conventions, file layout, implementation slices, migration-safe delivery, and maintaining a codebase others can continue to extend.

## What This Hub Owns

- repository structure and source-set organization
- implementation sequencing from thin slice to complete path
- configuration boundaries and environment separation
- framework placement without locking core logic to framework detail
- cross-cutting concerns such as validation, logging, and error mapping
- developer ergonomics when adding new endpoints, screens, or jobs
- migration-aware feature delivery and rollback positioning
- artifact layout for examples, docs, tests, and scripts
- module naming that reflects work ownership rather than personal taste
- dependency minimization during initial scaffolding
- deterministic local tooling required for implementation confidence
- repository delivery choices that preserve future maintainability

## What This Hub Does Not Own

- product roadmapping or feature prioritization
- campaign launches or audience segmentation
- organizational process unrelated to code delivery
- pure hosting procurement decisions without code consequences
- research synthesis that does not alter implementation
- support playbooks unless code changes are part of the answer
- business model strategy
- discovery interviews and JTBD output

## Questions To Answer First

- What is the first end-to-end slice that proves the repository is shaped correctly?
- Which conventions must be visible in the file tree rather than tribal memory?
- What needs a stable module seam now, and what can remain local?
- Which implementation path minimizes destructive refactors later?
- What scripts or templates make the happy path the default?
- How will a new engineer discover where to add the next behavior?
- What belongs in code versus generated configuration versus docs?
- Which build or runtime choices complicate local setup unnecessarily?
- How much scaffolding is enough before shipping the first useful slice?
- What release dependencies require feature flags or migration staging?
- Which interfaces should be test-first because they are brittle?
- What directory decisions will slow delivery if left vague?

## Required Inputs

- target runtime and language constraints
- expected deployment model and build pipeline shape
- team familiarity with current framework and repository conventions
- existing monorepo or single-repo policies
- required documentation or compliance artifacts
- testing strategy expectations from the team
- integration points that affect scaffolding choices
- environment variable and secret handling requirements
- release frequency and rollback expectations
- operational ownership after merge
- code generation tools already accepted or forbidden
- historical repository pain points to avoid repeating

## Evidence Signals

- existing repository layout and churn hotspots
- build times or setup failures visible in team feedback
- duplication patterns created by current structure
- missing conventions that force code review rework
- integration sequences that cross too many folders
- scripts required to complete common development tasks
- migration order dependencies between modules
- places where tests are hard to place or run
- release notes showing repeated implementation regressions
- documentation gaps that block onboarding

## Working Rules

- Build one thin vertical slice before scaling the pattern.
- Keep generation and scaffolding transparent, reviewable, and optional.
- Hide framework details behind code that the team can actually own.
- Prefer boring folder names over clever repository jokes.
- Move shared code only after two real call sites demand it.
- Keep configuration discoverable and environment-safe.
- Make extension points obvious to a future maintainer.
- Document new repository conventions near the code they govern.
- Do not let test layout drift from production layout without reason.
- Use scripts to reduce toil, not to conceal complexity.
- Treat setup friction as a delivery defect.
- A scaffold is successful when the second feature is faster, not the first demo prettier.

## Recommended Workflow

- Clarify the smallest production-relevant use case.
- Design the repository skeleton around that use case.
- Map folders to responsibilities and runtime boundaries.
- Create implementation conventions for inputs, outputs, and errors.
- Add scripts that validate structure before scale increases.
- Deliver the first vertical slice with tests and docs.
- Review extension cost with one hypothetical next feature.
- Adjust layout only where evidence shows confusion.
- Record the repository contract in README and examples.
- Keep later tooling additive rather than mandatory.

## Common Failure Modes

- scaffolding every possible layer before the first behavior exists
- copying architecture patterns that the team cannot maintain
- storing business logic in framework lifecycle files
- using barrels or wildcard exports that erase ownership
- letting config sprawl without local validation
- burying migrations inside unrelated features
- treating naming conventions as optional style
- producing repos that require oral tradition to navigate
- adding tools that cannot run offline or deterministically
- optimizing package boundaries before reviewing actual change flow

## Expected Deliverables

- repository layout rationale
- scaffold workflow with extension guidance
- implementation slice plan
- local validation script references
- module ownership cues and naming rules
- configuration handling notes
- testing placement rules
- migration and release considerations
- developer workflow checkpoints
- example prompt or usage scenario

## Hand-offs and Escalation

- to code quality review once the first slice lands
- to testing strategy once seams are defined
- to release work when configuration or rollout risk grows
- to frontend or API design when implementation surfaces clarify
- to platform owners when build or deployment constraints dominate
- to architecture review if repository structure exposes new coupling
- to product only if missing requirements block implementation
- to security review when secrets or privileged integrations appear

## Playbooks To Load Next

- `references/playbooks/repository-scaffolding-workflow.md`
- `references/playbooks/api-service-design.md`
- `references/playbooks/ci-delivery-workflow.md`
- `references/playbooks/refactor-plan.md`

## Deterministic Tools

- `scripts/architecture/inventory_codebase.py`
- `scripts/validate_repository.py`

## Review Checklist

- Repository root tells a newcomer where to start.
- Core logic is not trapped inside framework glue.
- Configuration sources are named and validated.
- Common commands are documented and reproducible.
- First slice covers a real request path or user path.
- Module names describe responsibility, not implementation detail.
- Shared utilities are not premature dumping grounds.
- Scripts fail clearly when contracts are broken.
- Docs match the actual file tree.
- Testing folders mirror production intent.
- Scaffold decisions include non-goals and future constraints.
- Release-relevant files are easy to locate.
- Rollback or migration needs are visible.
- No mandatory external service is hidden in setup.
- Examples show how to extend the repository correctly.
- Developers can validate behavior before pushing.
- The repository supports reviewable, incremental delivery.
- Default path is maintainable under ongoing feature pressure.
- Conventions are strict enough to reduce rework.
- The package remains professional and public-release ready.

## Closing Rule

Keep the answer inside engineering ownership. If the best next move is product strategy, discovery, or marketing planning, state that plainly and hand off rather than stretching this hub beyond its remit.

## Delivery Field Notes

- Repository structure should make the next feature cheaper, not simply make the current scaffold look complete.
- Setup commands that differ from CI without reason usually indicate missing repository contracts rather than contributor error.
- Public package roots deserve the same clarity as application roots because consumers also navigate by filenames first.
- Scaffolding should protect naming, testing, and validation habits before it tries to encode every future architectural nuance.
- A thin vertical slice is often a better structural proof than a long conventions document with no working path.
- Build scripts are part of the developer experience surface and should be reviewed as such.
- The most valuable repository examples tend to show extension patterns, not idealized greenfield snapshots.
- If contributors keep adding code in the wrong place, the structure is giving the wrong clue somewhere.
- Delivery guidance should explain both where code belongs and how engineers know they are done.
