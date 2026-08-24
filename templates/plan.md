# F`<N>`-`<n>` — `<Feature title>` — Plan

Spec: `docs/specs/YYYY-MM-DD-<topic>.md`.

One long-lived branch, `feature/NNN-<name>`, **one isolated commit per task**, so each slice stays
independently reviewable. Use `/build`, never `/build auto`. Every task gets one independent,
risk-matched review after its focused checks are stable; verify each finding against source before
acting. Never push without the developer's explicit confirmation.

## Architecture decisions

Settled in the spec; repeated here as **the constraints a task may not quietly relax**.

- **`<Decision>`** — `<the one-line reason it is not negotiable at task level>`.
- **`<Decision>`** — `<…>`.
- **`<The default that keeps existing behaviour unchanged on day one>`** — a task that makes an
  existing user behave differently has broken the feature.

## Standing constraints

The always-applicable rules this feature is most likely to trip over. Naming them here is cheaper than
finding them in review.

- **Comment budgets are enforced.** Load `code-commenter` before writing, revising or deleting any
  comment. Default is no comment. A change that alters no behaviour alters no comment.
- `<the type-safety rule that is build-failing here>`.
- **Never read back what was just written**; state the fixed query count in the doc comment of any
  method that assembles a page.
- Writes update the client cache from their own response; nothing re-reads.

## Tasks

### T1 — `<scope, stated as the outcome>`

**Touches:** `<paths>`
**Does:** `<the change, in three lines>`
**Focused checks:** `<the narrowest commands that prove this task>`
**Review:** `<role, per the risk matrix>`
**Done when:** `<the observable condition, including the red-green proof for each new test>`

### T2 — `<…>`

### T`<last>` — Record and gate

ADR-NNNN (+ any amendments), the architecture doc this work falsified, the roadmap tick, the
`DEFERRED.md` rows opened and closed, the regenerated contracts, and **the full clean gate run**.
