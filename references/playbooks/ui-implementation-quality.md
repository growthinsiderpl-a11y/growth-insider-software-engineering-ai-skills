# UI Implementation Quality

Review a frontend implementation for component boundaries, state ownership, semantic markup, state coverage, and design-system fitness in code.

## When To Run It

- reviewing a new screen or component family
- state management feels scattered or prop-heavy
- design-system primitives are growing unevenly
- responsive or interaction states keep breaking in review
- the code works but future UI changes look expensive
- page-level output also affects metadata or SEO behavior

## Do Not Run It When

- branding or creative-direction critique detached from code
- product strategy discussions about the feature itself
- line-by-line CSS bike-shedding with no user impact
- audits based only on screenshots when code behavior is the issue
- cases where backend or architecture dominates the problem

## Inputs

- component code or route implementation
- state and data flow description
- design tokens or style sources
- responsive targets
- accessibility expectations
- page metadata requirements if relevant

## Procedure

1. Read the contract
   - Identify the component or page responsibility.
   - Check what inputs and outputs the API exposes.
2. Inspect state ownership
   - Locate local, shared, and async state.
   - Look for props that reveal missing boundaries.
3. Check semantic structure
   - Review element choice, headings, and interactive controls.
   - Flag where semantics and styling diverge dangerously.
4. Cover states
   - Verify loading, empty, error, disabled, and success behavior.
   - Do not accept happy-path-only implementations.
5. Review token and layout discipline
   - Check repeated style choices against a token system.
   - Look for responsive behavior under content variation.
6. Close with maintainability
   - Judge whether the next UI change will be simpler or harder.
   - Recommend focused fixes only.

## Decision Tests

- Component APIs reveal intent.
- State owners are not ambiguous.
- Semantic markup supports the interaction.
- Edge states are implemented.
- Token or layout decisions are reusable.

## Outputs

- quality findings
- component boundary notes
- state coverage matrix
- token or layout recommendations
- follow-up implementation items

## Failure Modes

- celebrating visuals while behavior states are missing
- hiding data and control flow inside large components
- using design-system primitives to disguise product-specific hacks
- ignoring metadata on SEO-sensitive pages
- treating responsiveness as purely visual resizing

## Review and Follow-through

- Run before design-system extraction if patterns seem reusable.
- Pair with accessibility review for user-facing critical flows.
- Feed stable findings into coding guidelines or reusable examples.

## Evidence Reminder

Classify important statements as `FACT_USER`, `FACT_FILE`, `FACT_TOOL`, `CALCULATION`, `ASSUMPTION`, `HYPOTHESIS`, or `UNKNOWN` so the procedure stays reviewable and does not imply certainty it does not have.

## UI Review Notes

- Treat missing empty, loading, or error states as contract defects, not polish backlog.
- Prefer component boundaries that reduce cognitive load for future changes over abstractions that only reduce line count.
- When tokens are absent, describe the repeated styling decision they should capture.
- Responsive quality includes preserving action hierarchy, not only preventing overflow.
- Semantic markup decisions should be reviewed together with styling and state ownership.
- Page-level components deserve metadata attention if they influence discoverability or sharing output.
- Keep recommendations small enough that the next engineer can act without a redesign cycle.
- Note where accessibility review should deepen the frontend follow-up.
- Re-review once major variants or themes are added to ensure the API still holds.
