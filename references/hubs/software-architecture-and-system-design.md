# Software Architecture and System Design

Use this hub when the hard part is shaping the system: boundaries, flows, capacity, failure isolation, dependency rules, and the trade-offs that determine whether implementation will stay coherent under change.

## What This Hub Owns

- service boundaries, module seams, and dependency direction
- state ownership, data flow, and request lifecycles
- domain models, use-case orchestration, and contract placement
- read versus write path design and latency budgets
- eventing, queues, idempotency, and asynchronous recovery
- scaling paths for storage, compute, and critical integrations
- consistency boundaries and explicit failure behavior
- architecture decision records and trade-off justification
- system decomposition before roadmap decomposition
- interface stability between core logic and outer adapters
- design constraints for operability and maintainability
- technical SEO engineering only when architecture affects crawlable output

## What This Hub Does Not Own

- product prioritization or feature selection
- market positioning or messaging decisions
- general brainstorming without architectural pressure
- visual design direction that does not affect system shape
- organization design beyond the delivery implications
- customer discovery or JTBD framing
- launch marketing or pricing strategy
- analytics storytelling without implementation consequences

## Questions To Answer First

- What user-visible outcome fails if the architecture stays unchanged?
- Which constraint is binding first: latency, throughput, coupling, or correctness?
- What boundaries must remain stable for the next two to three releases?
- Which assumptions are facts from code, and which are inferred from diagrams or tickets?
- Where do data ownership conflicts already appear in the current system?
- What failure mode is acceptable, and what failure mode is not acceptable?
- Which parts need transactional guarantees versus eventual reconciliation?
- What is the simplest deployable unit that can absorb this responsibility?
- Which integration dictates the worst-case operational behavior?
- How will this decision affect testability and release blast radius?
- What observability must exist before the architecture is considered viable?
- What future change is being bought with current complexity?

## Required Inputs

- repository map or code inventory with entry points
- runtime topology if services, jobs, queues, or workers exist
- key domain concepts and invariants
- current request or event sequence for the hot path
- data stores, ownership boundaries, and consistency requirements
- external dependencies and their timeout or quota constraints
- expected traffic shape, latency objectives, and peak events
- security and privacy constraints that affect shape
- release model, rollback options, and migration limitations
- known incidents, defects, or scaling pressure from production
- existing ADRs or design notes if available
- unknowns that must stay unknown until implementation spikes

## Evidence Signals

- fact patterns visible from code structure
- runtime behavior from incident history or logs
- measured latency or throughput numbers from the team
- schema constraints and persistence semantics
- integration contract docs or client SDK limits
- deployment topology and failure domains
- migration cost and irreversibility indicators
- test seams proving or disproving boundary claims
- observability gaps that make the design unverifiable
- explicit unknowns recorded before proposing abstractions

## Working Rules

- Keep business rules inward and framework choices outward.
- Name boundaries after responsibilities, not infrastructure fashion.
- Prefer one decisive ownership model over duplicated convenience caches.
- Refuse shared mutable state unless the concurrency model is explicit.
- Define what must happen once, what may retry, and what may duplicate.
- Treat compensating logic as part of the design, not a postscript.
- Reduce cross-boundary chat before adding caching or more services.
- Separate user-facing latency requirements from background freshness goals.
- Make unhappy-path sequencing as concrete as the happy path.
- Avoid architecture that cannot be proven by tests or telemetry.
- Use queues to absorb variability, not to hide undefined ownership.
- If a boundary exists only in slides, it does not exist yet.

## Recommended Workflow

- State the decision in one sentence with the business consequence.
- Draw the current flow from entry to persistence to side effects.
- Mark ownership, coordination, and irreversible operations.
- List constraints that are factual versus assumed.
- Generate two or three minimum-sufficient options only.
- Stress each option against scale, change, and failure.
- Pick the option with the clearest operating model.
- Define contracts, migrations, and review checkpoints.
- Translate the architecture into implementation slices.
- Specify measurement that would falsify the decision.

## Common Failure Modes

- introducing services to escape code review discipline
- using abstractions before invariants are known
- confusing package names with real dependency control
- treating eventual consistency as permission for ambiguity
- splitting reads and writes without a stale-data story
- assuming the database can absorb all coordination complexity
- designing for global scale when the real constraint is release reliability
- optimizing queues without defining idempotency keys
- adding retries without timeout budgets or operator signals
- creating a public contract before proving the internal model

## Expected Deliverables

- boundary map with ownership and dependency direction
- request or event lifecycle narrative
- trade-off table with reasons options were rejected
- migration plan with rollback position
- risk register tied to concrete failure modes
- implementation sequencing with review gates
- telemetry requirements for the chosen design
- test strategy implications for the architecture
- open questions kept visible rather than buried
- ADR-ready summary for repository documentation

## Hand-offs and Escalation

- to implementation once contracts and slices are stable
- to quality engineering once seams and risks are explicit
- to release engineering when migrations or rollout controls appear
- to observability work when new signals are required
- to frontend implementation if UI architecture changes state ownership
- to technical SEO when routing or rendering affects crawlable output
- to product only when unresolved scope questions block design
- to security review when trust boundaries move

## Playbooks To Load Next

- `references/playbooks/architecture-boundary-assessment.md`
- `references/playbooks/dependency-direction-review.md`
- `references/playbooks/system-design-decision-process.md`
- `references/playbooks/api-service-design.md`

## Deterministic Tools

- `scripts/architecture/inventory_codebase.py`
- `scripts/architecture/validate_dependency_direction.py`

## Review Checklist

- Every boundary has one clear owner.
- Dependency direction is explicit and testable.
- State mutation points are enumerated.
- External calls have timeout and retry posture.
- Consistency model is named, not implied.
- Failure handling is described before implementation starts.
- Rollback position exists for risky migrations.
- Measurement plan proves the architecture in production.
- Non-goals are documented to prevent scope drift.
- No option is chosen only because it feels modern.
- The simplest option that meets constraints is preferred.
- Key interfaces are small enough to test cheaply.
- Cache ownership and invalidation are documented.
- Batch, queue, and API contracts are differentiated.
- Security boundaries are visible on the diagram.
- Operators can tell success from silent failure.
- Incidents that motivated the change are referenced.
- Future extension points are justified, not ornamental.
- Domain language is consistent across the proposal.
- The design can survive staff turnover and partial knowledge.

## Closing Rule

Keep the answer inside engineering ownership. If the best next move is product strategy, discovery, or marketing planning, state that plainly and hand off rather than stretching this hub beyond its remit.

## Engineering Field Notes

- Boundary reviews should name the unit that can be deployed, the unit that can fail, and the unit that must be reasoned about by one engineer in one sitting.
- A storage boundary is not necessarily a domain boundary; shared tables sometimes hide two different responsibilities that should still be modeled separately.
- If an integration cannot tolerate retries, the architecture should make that constraint visible at the application edge instead of leaking it through random helper code.
- A queue is useful when it isolates variable work, but harmful when it becomes a place where undefined ownership and undefined error recovery go to hide.
- Capacity planning belongs in the design conversation only when the expected shape of traffic or jobs can change the component split or persistence choice.
- Designs that are easy to diagram but hard to instrument usually need another pass before implementation starts.
- The right boundary often reduces the number of concepts a maintainer must hold at once, even if it adds one deliberate adapter.
- Architecture prose should be short enough that the next reviewer can disagree with it precisely.
- A good system-design answer keeps at least one rejected option visible so future teams understand which trade-off was chosen on purpose.
