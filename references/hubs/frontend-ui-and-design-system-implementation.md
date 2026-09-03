# Frontend UI and Design System Implementation

Use this hub when the work is in the interface layer: component design, stateful UI implementation, design token translation, interaction quality, design-system structure, and converting visual or UX intent into maintainable frontend code.

## What This Hub Owns

- component architecture and composition
- state placement in interface flows
- design token definition and implementation mapping
- responsive layout systems and breakpoint behavior
- interaction states, feedback, and empty/error handling
- design-system primitives, variants, and extension discipline
- frontend code quality for readability and reuse
- UI implementation reviews grounded in code and behavior
- semantic markup decisions that affect accessibility and SEO output
- motion and microinteraction implementation boundaries
- frontend documentation that helps consistent delivery
- translation of visual requirements into code constraints

## What This Hub Does Not Own

- brand strategy or campaign creative direction
- pure visual moodboarding without implementation decisions
- product discovery or prioritization
- copywriting strategy beyond spotting implementation constraints
- marketing landing-page offer strategy
- native app policy interpretation outside the current code change
- organizational ownership debates without code impact
- generic web design theory untied to a concrete interface task

## Questions To Answer First

- What behavior should the UI make easy, obvious, and recoverable?
- Which state belongs local, shared, or server-sourced?
- What component boundaries reduce duplication without freezing flexibility?
- Which design tokens need to be first-class because variation is expected?
- How should the interface degrade when data, permissions, or devices vary?
- Where will accessibility semantics shape markup and interaction choices?
- What visual requirement translates into measurable code rules?
- Which interaction states are missing from the current implementation?
- How will this component evolve when the next feature arrives?
- What belongs in the design system versus the product layer?
- How do performance and animation constraints limit the implementation?
- What SEO-relevant markup must remain crawlable or server-rendered?

## Required Inputs

- UI goals and user journeys
- design files, screenshots, or written interaction notes
- current component library and token sources
- responsive targets and browser support expectations
- data-loading, error, and permission states
- accessibility requirements or known complaints
- copy or content variability expectations
- rendering model such as SSR, CSR, or hybrid routes
- performance budgets for the affected surfaces
- theme requirements including dark mode if relevant
- test approach for frontend behavior
- handoff expectations between design and engineering

## Evidence Signals

- component duplication and prop explosion
- markup that undermines semantics or keyboard flow
- token drift between code and design assets
- loading and empty states missing from implementation
- responsive breakpoints that collapse important actions
- animations causing layout thrash or unclear focus behavior
- inconsistent spacing or typography because primitives are weak
- frontend bugs caused by unclear state ownership
- SEO-sensitive pages rendered without stable metadata
- review feedback repeating the same UI implementation defects

## Working Rules

- Build stable primitives before proliferating specialized wrappers.
- Component APIs should reveal purpose, not internal layout trivia.
- Token systems are valuable only if engineers can actually apply them.
- Loading, empty, and error states are part of the component contract.
- Use semantic HTML as the default, then justify divergence.
- Responsive behavior should preserve task completion, not just avoid overflow.
- Animation should clarify state or hierarchy, not decorate uncertainty.
- Keep state near the smallest owner that can manage it coherently.
- Do not turn a design system into a dumping ground for product hacks.
- Prefer implementation patterns that survive content variation.
- If SEO-critical content depends on JavaScript, say so explicitly.
- Design polish matters when it changes usability, trust, or maintainability.

## Recommended Workflow

- Define the interface responsibility and user task.
- Map component boundaries and state ownership.
- Translate design attributes into tokens or explicit code rules.
- Implement semantic structure before visual flourish.
- Cover all primary UI states.
- Check responsive and keyboard behavior early.
- Harden metadata and crawlable output when page-level work exists.
- Review API shape for extension cost.
- Measure performance-sensitive interactions.
- Document patterns the next contributor must follow.

## Common Failure Modes

- wrapping every HTML element in a custom abstraction
- creating huge component props to avoid state decisions
- treating design tokens as static screenshots instead of systems
- building beautiful happy paths with broken edge states
- ignoring keyboard and focus flow until QA finds it
- shipping server-sensitive SEO pages as client-only shells
- letting animation hide poor information hierarchy
- mixing domain logic directly into primitive components
- adding variants with no token strategy
- equating pixel matching with implementation quality

## Expected Deliverables

- component boundary review
- token mapping or generation output
- responsive behavior notes
- state and variant matrix
- semantic markup guidance
- interaction quality findings
- SEO-sensitive page implementation notes
- design-system extension rules
- frontend test implications
- implementation follow-up list

## Hand-offs and Escalation

- to accessibility review when semantics or focus behavior matter
- to performance work when rendering or animation costs rise
- to technical SEO when metadata or routing output matters
- to maintainability review when component APIs sprawl
- to testing when behavior states need stronger coverage
- to design collaboration when tokens or patterns remain undefined
- to release readiness for risky UI migrations
- to architecture if frontend boundaries reflect broader system coupling

## Playbooks To Load Next

- `references/playbooks/ui-implementation-quality.md`
- `references/playbooks/accessibility-implementation-checklist.md`
- `references/playbooks/performance-remediation-plan.md`
- `references/playbooks/technical-seo-engineering.md`

## Deterministic Tools

- `scripts/quality/generate_design_tokens.py`
- `scripts/seo/check_technical_seo_artifacts.py`

## Review Checklist

- Component purpose is obvious from its name and API.
- UI states include loading, empty, error, and success.
- Markup preserves semantics where possible.
- Design tokens cover repeated styling decisions.
- Responsive behavior protects key actions.
- Focus management is intentional.
- Keyboard access is considered.
- Animation serves feedback or orientation.
- SEO-relevant metadata exists on page-level routes.
- Client-only dependencies are justified.
- Variant growth remains manageable.
- Product-specific hacks are isolated from primitives.
- Tests cover important state transitions.
- Styles are maintainable under future theming.
- Token generation is deterministic if automated.
- Accessibility concerns are flagged early.
- Performance-sensitive components avoid obvious waste.
- Examples teach the preferred usage pattern.
- Design-system additions have review criteria.
- The implementation remains readable under change.

## Closing Rule

Keep the answer inside engineering ownership. If the best next move is product strategy, discovery, or marketing planning, state that plainly and hand off rather than stretching this hub beyond its remit.

## Interface Field Notes

- Component APIs should help engineers predict usage without opening the implementation file every time.
- Design tokens become operational when they reduce repetitive judgment, not when they merely mirror a design file naming scheme.
- The best frontend abstractions make edge states easier to represent, not easier to ignore.
- Responsive quality is often about preserving decision-making context for the user rather than fitting every pixel perfectly.
- Primitive components should stay stable enough that product code can move faster around them.
- Metadata and semantic structure deserve attention early on page-level routes because retrofitting them later is usually more expensive.
- UI reviews should include the maintenance story for the next variant, not just the current screenshot.
- Implementation quality improves when interaction, accessibility, and styling are reviewed as one coded system.
- A healthy design system reduces friction without flattening every product need into the same component shape.
