# Developer Workflow and Delivery Operations

Use this hub when the code may be sound but delivery is not: local workflow, CI shape, repository validation, review loops, deterministic tooling, contribution experience, and operating practices that help engineers ship changes without avoidable friction.

## What This Hub Owns

- developer workflow design inside the repository
- CI delivery patterns and validation loops
- local scripts and guardrails that reduce repeated review defects
- documentation for contribution and support flows
- repository validation and public release hygiene
- branch, review, and merge discipline as it affects code quality
- repeatable operations around code delivery
- tooling choices that keep feedback fast and understandable
- examples that teach the expected usage or review path
- issue and PR templates supporting maintainable contribution flow
- deterministic operational scripts with no hidden network dependency
- workflow boundaries that prevent marketing or product concerns from leaking in

## What This Hub Does Not Own

- company-wide HR or people-process design
- roadmap operations unrelated to code delivery
- marketing launch workflows
- support process not tied to repository artifacts
- general productivity advice detached from engineering tasks
- vendor procurement for collaboration tools
- product-triad operating models
- sales or customer success handoff processes

## Questions To Answer First

- Where does delivery slow down today: setup, validation, review, or release?
- Which repeated defects could be caught deterministically?
- What commands must every contributor know immediately?
- Which CI checks add confidence, and which add noise?
- How can repository rules be made self-checking?
- What templates or docs prevent repetitive clarification?
- How can local and CI feedback stay aligned?
- What part of the workflow should remain manual because judgment is required?
- How can public package consumers understand compatibility and support boundaries?
- What signals prove the workflow improved after changes?
- Which delivery pain belongs to architecture or code health rather than workflow?
- How should contribution guidance stay compact but complete?

## Required Inputs

- current local and CI commands
- repeated review comments or merge blockers
- existing scripts and their failure quality
- documentation gaps in setup or contribution
- public release requirements if the repository is distributed
- support and security contact expectations
- build and test runtime constraints
- cross-platform needs for contributors
- examples of user confusion around the package
- issue types that recur in maintenance
- release cadence and validation expectations
- non-negotiable rules from the repository owner

## Evidence Signals

- contributors asking the same operational questions
- CI failures that could have been caught locally
- scripts returning vague or misleading errors
- docs that drift from the real commands
- pull requests missing essential context
- release tasks handled from memory instead of artifacts
- support requests caused by unclear boundaries
- public metadata missing compatibility or license information
- validators that check too little or too opaquely
- manual operations repeated without review value

## Working Rules

- Workflow automation should expose rules, not hide them.
- Local feedback should arrive before remote frustration.
- Repository validation must be explicit, deterministic, and inspectable.
- CI should prove readiness, not perform ceremony.
- Public package docs should answer the first operational questions quickly.
- Keep templates short enough to be used, complete enough to help.
- Do not add workflow complexity to compensate for unclear architecture.
- Favor commands that work offline and cross-platform when possible.
- Review friction is acceptable when it blocks real risk.
- Support and security paths must be easy to find.
- Contribution guidance should state both rules and reasons.
- A good workflow makes the preferred path the easier path.

## Recommended Workflow

- Map the current delivery loop from edit to merge.
- Identify avoidable friction and repeated failure classes.
- Encode clear rules in validators, templates, and docs.
- Keep local commands aligned with CI expectations.
- Reduce ambiguity in release and support metadata.
- Make contribution steps obvious in the repository root.
- Check that automation output teaches corrective action.
- Preserve judgment where domain reasoning is required.
- Review workflow changes against real contributor needs.
- Track whether delivery becomes faster and clearer.

## Common Failure Modes

- adding workflows no contributor will read or run
- turning CI into a slow duplicate of local tooling
- using opaque scoring rather than explicit findings
- creating validator messages that do not explain fixes
- burying support or security contacts
- treating public-release docs as optional polish
- automating tasks that still require human judgment
- forcing online services into core validation
- letting templates sprawl into bureaucracy
- optimizing workflow while ignoring the underlying code smell

## Expected Deliverables

- workflow diagnosis
- local and CI command contract
- repository validation expectations
- contribution and support docs
- template improvements
- public release checklist
- compatibility documentation
- explicit operational boundaries
- example usage and review guidance
- follow-up improvements for recurring pain

## Hand-offs and Escalation

- to maintainability work when workflow pain is actually code structure pain
- to testing when CI changes should mirror better validation strategy
- to release readiness when delivery operations touch deployment risk
- to architecture when boundaries are causing review churn
- to frontend or SEO when examples and docs must reflect those domains
- to product or marketing when requests drift beyond engineering scope
- to security review when workflow touches secrets or privileged actions
- to package maintainers for public release approval

## Playbooks To Load Next

- `references/playbooks/ci-delivery-workflow.md`
- `references/playbooks/release-validation.md`
- `references/playbooks/production-readiness-gate.md`
- `references/playbooks/repository-scaffolding-workflow.md`

## Deterministic Tools

- `scripts/validate_repository.py`
- `scripts/validate_behavioral_evals.py`

## Review Checklist

- Core commands are documented.
- Validators produce actionable errors.
- Local and CI loops are aligned.
- Templates help reviewers and reporters quickly.
- Support and security routes are visible.
- Compatibility claims are bounded and honest.
- Release checklist references actual commands.
- No hidden network dependency exists in core validation.
- Contribution guidance is concise.
- Examples reflect intended usage.
- Workflow changes solve repeated problems.
- Automation stops before judgment is replaced.
- Docs match the repository reality.
- Public metadata is complete.
- Cross-skill boundaries are explicit.
- Maintainers can validate the package offline.
- Operational artifacts are versioned with the code.
- The repository is easier to adopt after the changes.
- The workflow remains professional and understandable.
- Delivery operations reinforce engineering quality.

## Closing Rule

Keep the answer inside engineering ownership. If the best next move is product strategy, discovery, or marketing planning, state that plainly and hand off rather than stretching this hub beyond its remit.

## Workflow Field Notes

- Good developer workflow design makes the correct local path shorter than the incorrect one.
- Validators should communicate repository expectations in the language of actionable fixes rather than institutional scolding.
- Public package operations matter because outside consumers do not share the maintainers' context or habits.
- Templates only help when they capture decisions contributors repeatedly forget to provide.
- CI should mirror the repository contract closely enough that local preparation remains honest and useful.
- Delivery operations improve when repeated friction is turned into explicit, inspectable repository rules.
- Support and security files are part of engineering trust, not just administrative garnish.
- Offline-first validation keeps the package portable and lowers maintenance surprises.
- A mature workflow keeps judgment with humans while making routine checks fast and dependable.
