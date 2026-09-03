# Dependency Direction Review

Review whether dependencies move inward toward policy and domain intent rather than outward toward framework, UI, storage, or integration detail.

## When To Run It

- clean-architecture or layered rules are claimed but not enforced
- tests require infrastructure setup to reach business logic
- core modules import web, UI, ORM, or SDK concerns directly
- reuse is difficult because inner logic knows outer specifics
- dependency drift appears after rapid feature delivery
- refactors need a precise import-level violation inventory

## Do Not Run It When

- single-file bug fixes with no broader dependency impact
- design debates with no code to inspect
- requests that are actually about naming or formatting only
- cross-skill work like marketing analytics instrumentation strategy
- cases where the repository has no meaningful layer model yet

## Inputs

- layer list and allowed relationships
- component or module ownership map
- dependency edges from code or stated analysis
- examples of imports that feel wrong
- known framework adapters and entry points
- exceptions that are intentionally tolerated

## Procedure

1. Define the rule
   - List layers from most stable policy inward to least stable detail outward.
   - Write what each layer may depend on.
2. Collect edges
   - Gather imports or references that cross modules.
   - Normalize paths so violations are reviewable.
3. Classify components
   - Assign each component to a layer.
   - Record uncertain cases instead of forcing them.
4. Locate violations
   - Compare every edge to the allowed graph.
   - Separate direct violations from suspicious but allowed coupling.
5. Interpret causes
   - Identify why the violation exists: convenience, missing abstraction, or wrong ownership.
   - Avoid treating all violations as equally urgent.
6. Recommend repair
   - Choose the smallest structural move that restores direction.
   - Suggest ports, adapters, DTOs, or composition roots only when needed.
7. Guard the rule
   - Add validator usage or review guidance.
   - Decide what should be blocked automatically versus reviewed manually.

## Decision Tests

- Violation list names source, target, and broken rule explicitly.
- Allowed exceptions are conscious and documented.
- Repair guidance reduces coupling rather than moving it elsewhere.
- Reviewers can explain the dependency rule in repository terms.
- The chosen fix helps testability or maintainability measurably.

## Outputs

- dependency rule statement
- violation report
- repair sequence
- exception register
- automation recommendation

## Failure Modes

- using abstract diagrams with no component mapping
- marking everything as an exception
- rewriting the whole repo to satisfy a theoretical purity target
- creating adapters that merely forward detail inward
- failing to explain how the fix helps actual change flow

## Review and Follow-through

- Re-run after major feature waves or repository reorganizations.
- Use as a PR review lens for architecture-sensitive work.
- Pair with maintainability review when violations cluster in the same files.

## Evidence Reminder

Classify important statements as `FACT_USER`, `FACT_FILE`, `FACT_TOOL`, `CALCULATION`, `ASSUMPTION`, `HYPOTHESIS`, or `UNKNOWN` so the procedure stays reviewable and does not imply certainty it does not have.

## Direction Review Notes

- A small number of well-explained exceptions is healthier than a false claim of purity.
- Prefer repair options that remove knowledge from inner layers instead of inventing new wrapper layers.
- Dependency rules should be expressible in repository terms that reviewers can observe quickly.
- Record whether a violation exists because of missing abstractions or because the layer model itself is wrong.
- When the outer detail is truly stable, still ask whether the inner layer must know about it directly.
- Fixes should preserve readability for everyday contributors, not only satisfy architectural vocabulary.
- Use automation for recurring import violations, but keep nuanced repairs in human review.
- If the graph is unclear, improve component classification before judging every edge.
- Re-run after major module moves to confirm the rule still matches the real system.
