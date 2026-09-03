# Repository Scaffolding Workflow

Create or reshape a repository so engineers can add features through a clear, testable, maintainable structure instead of ad hoc file growth.

## When To Run It

- starting a new codebase or major module family
- inheriting a repo whose structure blocks progress
- converting one-off scripts into a maintained application
- preparing public package distribution or shared internal reuse
- need exists for examples, docs, tests, and scripts to align cleanly
- new contributors cannot easily find the correct extension points

## Do Not Run It When

- full architecture redesign when the issue is only naming
- premature monorepo decomposition
- cases where one small folder move will solve the pain
- requests that belong to product packaging rather than code delivery
- scaffolding for hypothetical features with no near-term use

## Inputs

- target runtime and framework constraints
- first end-to-end use case
- testing expectations
- release and support artifacts required
- public or internal distribution needs
- current friction points if reshaping an existing repo

## Procedure

1. Choose the first slice
   - Identify the first meaningful behavior the repo must support.
   - Refuse to scaffold beyond that without evidence.
2. Define top-level contract
   - Decide what lives at root: skill entry, manifest, docs, scripts, tests, examples.
   - Keep the root readable.
3. Map responsibilities
   - Place core logic, adapters, validation, and references deliberately.
   - Avoid utility dumping grounds.
4. Add deterministic support
   - Create scripts and tests that validate the repository contract.
   - Ensure commands work locally and predictably.
5. Document extension rules
   - Explain where future hubs, playbooks, modules, or packages belong.
   - Show examples, not only rules.
6. Review against next change
   - Simulate adding the next likely feature.
   - Adjust structure only where future friction is obvious.
7. Freeze the contract lightly
   - Add validators and contribution guidance.
   - Keep room for evolution without chaos.

## Decision Tests

- Repository root is self-explanatory.
- A second contributor can locate the next extension point quickly.
- Tests and scripts mirror the repository contract.
- The structure supports public release documentation if needed.
- No folder exists only because another package used it.

## Outputs

- repository layout rationale
- extension rules
- artifact inventory
- validation commands
- future-change simulation notes

## Failure Modes

- copying structure from an unrelated domain package
- creating many empty folders to signal ambition
- burying public-facing metadata in deep paths
- omitting docs because the structure feels obvious to the author
- using scripts that hide how the repository really works

## Review and Follow-through

- Re-evaluate after the second and third real extensions.
- Check whether docs and validators still match the live tree.
- Tighten rules only when recurring drift appears.

## Evidence Reminder

Classify important statements as `FACT_USER`, `FACT_FILE`, `FACT_TOOL`, `CALCULATION`, `ASSUMPTION`, `HYPOTHESIS`, or `UNKNOWN` so the procedure stays reviewable and does not imply certainty it does not have.

## Scaffold Notes

- Scaffolding is successful when the second contributor extends the repository correctly with less guidance.
- Root-level files should signal the package contract immediately to both humans and tools.
- Avoid directory creation that advertises ambition without live content or validation value.
- A public repository benefits from examples that demonstrate extension more than from elaborate prose alone.
- Deterministic local scripts can teach the contract better than hidden conventions.
- Validate naming and placement rules early so structural drift does not become normal.
- Keep the scaffold adaptable enough to absorb the next real module without churn.
- If the repository already works, change only the parts blocking delivery or comprehension.
- Review scaffold quality by simulating the next likely change, not by admiring the tree.
