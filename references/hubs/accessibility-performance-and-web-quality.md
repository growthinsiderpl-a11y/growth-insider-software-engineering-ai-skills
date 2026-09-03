# Accessibility, Performance, and Web Quality

Use this hub when the quality bar is defined by the lived web experience: semantic accessibility, interaction clarity, rendering efficiency, asset discipline, web vitals pressure, and the code changes required to make a site or app faster and more usable.

## What This Hub Owns

- accessibility implementation decisions in code
- keyboard, focus, and semantic interaction quality
- performance bottleneck diagnosis tied to rendering behavior
- asset loading strategy and component efficiency
- web-quality decisions affecting responsiveness and usability
- front-end remediation planning with measurable outcomes
- progressive enhancement and graceful degradation
- page structure and metadata quality that affect the browser experience
- code-level recommendations for Core Web Vitals pressure
- engineering review of interaction friction or rendering waste
- quality trade-offs between aesthetics, complexity, and speed
- verification plans for user-facing web performance changes

## What This Hub Does Not Own

- brand storytelling or marketing conversion strategy
- search strategy that does not involve code changes
- product prioritization except to note trade-offs
- visual design taste absent implementation impact
- vendor benchmarking claims without local evidence
- pure analytics interpretation with no remediation path
- infrastructure spend decisions alone
- general consulting on inclusion policies outside the codebase

## Questions To Answer First

- What user task is degraded today: perceiving, navigating, or completing?
- Which accessibility issue is factual from markup or behavior?
- What part of the render path is slow, and why?
- Is the bottleneck network, execution, layout, or media?
- Which code change gives the most user benefit first?
- What failure state appears on low bandwidth, low power, or keyboard-only use?
- Which assets or components are loaded before they are needed?
- How do state changes communicate to assistive technology?
- What performance regression risk comes from this remediation?
- Which quality improvements can be validated locally and repeatably?
- Where does progressive enhancement matter for resilience?
- What remains unknown without live telemetry or browser profiling?

## Required Inputs

- affected pages or component paths
- screenshots, recordings, or repro steps if available
- markup and interaction implementation details
- current performance symptoms or targets
- asset inventory and rendering strategy
- browser and device support expectations
- accessibility bug reports or audit findings
- JavaScript execution hotspots if known
- server-rendering or caching model
- critical user flows tied to the affected area
- availability of local profiling or synthetic measurements
- release constraints for remediation sequencing

## Evidence Signals

- missing landmarks, labels, or headings
- focus loss during state transitions
- tab order that conflicts with visual or logical flow
- large assets or blocking scripts
- layout thrash or repeated re-render patterns
- hydration-heavy pages with little above-the-fold value
- buttons or links with ambiguous accessible names
- unannounced async updates or error states
- page metadata or lang attributes missing
- remediations that cannot be proven because measurement is absent

## Working Rules

- Accessibility is part of correctness for user-facing software.
- Measure the browser problem before prescribing generic speed advice.
- Prefer semantic defaults over ARIA patchwork.
- Do not trade away keyboard clarity for animation style.
- Optimize the critical path before polishing the long tail.
- Lazy loading is useful only when user tasks remain coherent.
- Progressive enhancement is a resilience strategy, not nostalgia.
- Fix the render trigger, not only the symptom metric.
- State changes should be perceivable to more than one modality.
- Performance advice must mention what is still unknown.
- A fast but confusing page is not high quality.
- Remediation should target user outcomes, not only score dashboards.

## Recommended Workflow

- Identify the user experience defect in observable terms.
- Inspect markup, behavior, and asset paths involved.
- Separate accessibility findings from performance findings while noting overlap.
- Choose the smallest code change that meaningfully improves the path.
- Define what local validation can prove.
- Implement semantics or rendering fixes first.
- Re-check state changes, focus behavior, and loading experience.
- Document residual unknowns that require live verification.
- Sequence broader remediation if deeper causes remain.
- Review whether the code is now easier to keep high quality.

## Common Failure Modes

- treating Lighthouse-style advice as universal truth
- adding ARIA to compensate for wrong elements
- optimizing metrics while preserving a confusing workflow
- lazy-loading content that users need immediately
- announcing too much state noise to assistive technology
- hiding slow architecture with skeleton theatrics only
- shipping performance fixes that create caching bugs
- reducing motion without preserving orientation cues
- focusing on one browser while ignoring required support
- claiming accessibility compliance from a partial local review

## Expected Deliverables

- accessibility findings and remediation steps
- performance bottleneck hypothesis and evidence
- prioritized code-level improvements
- state and focus behavior checklist
- asset and rendering recommendations
- verification plan for local and live follow-up
- residual-risk notes
- handoff cues for frontend and release teams
- technical SEO overlap notes when relevant
- quality maintenance guidance after the fix

## Hand-offs and Escalation

- to frontend implementation for component-level fixes
- to technical SEO when web quality affects crawlable pages
- to release readiness if the remediation changes critical paths
- to testing when regression checks should be added
- to observability work if live verification is needed
- to design collaboration when layout or hierarchy causes the issue
- to architecture when poor rendering follows broader system shape
- to product only if the task itself is ambiguous

## Playbooks To Load Next

- `references/playbooks/accessibility-implementation-checklist.md`
- `references/playbooks/performance-remediation-plan.md`
- `references/playbooks/ui-implementation-quality.md`
- `references/playbooks/technical-seo-engineering.md`

## Deterministic Tools

- `scripts/seo/check_technical_seo_artifacts.py`
- `scripts/quality/find_maintainability_violations.py`

## Review Checklist

- Landmarks and headings support navigation.
- Interactive controls have clear names.
- Focus is preserved or intentionally redirected.
- Keyboard operation is possible for key tasks.
- Async updates communicate clearly.
- Critical content is not delayed without reason.
- Large assets are justified or optimized.
- Render work is proportional to user value.
- Performance claims reference observable evidence.
- Unknowns are not hidden by faux certainty.
- Remediations improve maintainability where possible.
- Lang, title, and metadata basics are covered.
- Animation does not obscure usability.
- Error and empty states stay accessible.
- Progressive enhancement is considered for fragile paths.
- Validation steps are repeatable.
- SEO overlap is captured if page output changes.
- The user experience is simpler after the change.
- Reviewers can understand the quality trade-offs made.
- Web quality work remains tied to code, not scores alone.

## Closing Rule

Keep the answer inside engineering ownership. If the best next move is product strategy, discovery, or marketing planning, state that plainly and hand off rather than stretching this hub beyond its remit.

## Web Quality Field Notes

- Accessibility and performance often meet at the same implementation seam: clear structure, predictable state, and disciplined rendering.
- Web quality reviews should prioritize the real user task first, then the metrics that approximate that experience.
- Performance work becomes more durable when it removes unnecessary work instead of merely delaying it.
- Semantic HTML usually improves both accessibility and resilience before any specialized tooling enters the picture.
- Fast pages still fail users if focus, error communication, or reading order are poorly implemented.
- Engineering recommendations should separate what is observable offline from what still requires live browser or field evidence.
- The best remediations lower future maintenance cost as well as present user friction.
- Quality guidance should help teams avoid regressions, not only fix the current page once.
- Browser experience is part of the product surface and should be treated as such in code reviews.
