# Accessibility Implementation Checklist

Run a code-focused accessibility implementation pass covering semantics, names, focus, keyboard support, status messaging, and resilient interaction states.

## When To Run It

- shipping or reviewing user-facing interfaces
- fixing accessibility complaints or audit findings
- building forms, dialogs, navigation, or async interactions
- refactoring components whose semantics are unclear
- page templates affect multiple routes at once
- the goal is engineering remediation rather than policy discussion

## Do Not Run It When

- claiming conformance certification from a local checklist
- using ARIA as a first move instead of semantic HTML
- content-style reviews with no code changes
- backend-only tasks
- cases where the interaction design itself is still unsettled

## Inputs

- relevant component or page code
- interaction flow description
- known problem reports or audit notes
- supported browsers and devices
- state changes or async behavior
- copy or labels if already available

## Procedure

1. Choose correct elements
   - Start with semantic structure and control types.
   - Use ARIA only to enhance, not replace, semantics.
2. Check names and labels
   - Review accessible names for controls, landmarks, and media.
   - Make label relationships explicit.
3. Validate keyboard flow
   - Tab through the interaction order conceptually or literally.
   - Confirm no trap or dead-end is created.
4. Review focus handling
   - Ensure focus moves or remains intentionally after state changes.
   - Do not let modals or async updates drop context.
5. Check status communication
   - Expose loading, validation, and error messages clearly.
   - Support more than one perception mode.
6. Close with resilience
   - Inspect disabled, empty, and failure states.
   - A flow is not accessible if only success works.

## Decision Tests

- Element choice supports the interaction.
- Labels and names are explicit.
- Keyboard users can complete the task.
- Focus behavior preserves orientation.
- State changes communicate clearly.

## Outputs

- implementation checklist result
- semantics fixes
- focus and keyboard findings
- status-message guidance
- residual unknowns for broader audit

## Failure Modes

- overusing generic divs and buttons with patched roles
- adding aria-label while the visible label remains wrong
- forgetting error states in async flows
- moving focus purely because animation changed
- equating one screen reader pass with complete accessibility confidence

## Review and Follow-through

- Pair with UI implementation review when components are still changing.
- Repeat after major interaction redesigns.
- Escalate to deeper accessibility audit when legal or high-risk stakes demand it.

## Evidence Reminder

Classify important statements as `FACT_USER`, `FACT_FILE`, `FACT_TOOL`, `CALCULATION`, `ASSUMPTION`, `HYPOTHESIS`, or `UNKNOWN` so the procedure stays reviewable and does not imply certainty it does not have.

## Accessibility Notes

- If semantics are wrong at the element level, no amount of ARIA polish will fully repair the interaction.
- Clear accessible names usually reduce general UI confusion as well as assistive-technology confusion.
- Keyboard flow should preserve the same task logic the visual layout suggests.
- Error and validation messages need timing and placement decisions, not just text.
- Focus management should support orientation rather than simply moving after every state change.
- Prefer reusable patterns for recurring controls so accessibility quality scales with the component system.
- State what still requires broader audit or manual assistive-technology verification.
- Good accessibility fixes often simplify the implementation instead of making it more exotic.
- Repeat the checklist after major flow or component rewrites.
