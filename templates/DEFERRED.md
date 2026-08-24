# Deferred work log

A running record of things intentionally **punted to a later feature/phase** during implementation, so
decisions to defer are tracked rather than lost. Strategic, product-level deferrals live in
[`ROADMAP.md`](ROADMAP.md) ("Explicitly deferred"); this file holds the finer-grained,
implementation-level deferrals made inside features.

> **Every row states a target** — a feature id or phase — or is marked **Landed** or **Dropped
> (decision)**. There is no "no fixed target yet": an untargeted row is not tracked work, it is a note
> nobody will action. Decide by blast radius — small and contained, do it instead of writing the row;
> large or blocked on a decision, schedule it by adding the feature to [`ROADMAP.md`](ROADMAP.md) so
> the deferral has a home. When you pick up the target feature, clear the row in that feature's PR.

## Deferred to F`<N>`-`<n>` — `<the feature that absorbs these>`

| Item | Deferred from | Notes |
|------|---------------|-------|
| **`<Item, stated as the work>`** | F`<N>`-`<n>` · `<task>` | **Target: F`<N>`-`<n>`.** `<Why it waits, what it costs to wait, and what makes the target the right home.>` |
| ~~`<A row that has landed>`~~ | F`<N>`-`<n>` | ✅ **Done in F`<N>`-`<n>`** ([ADR-NNNN](architecture/adr/NNNN-....md)). `<What actually shipped, and where it differed from the original note.>` *Original note: `<kept verbatim — the reasoning is why the row was written>`.* |

## Deferred to Phase `<N>` — `<theme>`

| Item | Deferred from | Target |
|------|---------------|--------|
| `<item>` | `<feature>` | **Target: F`<N>`-`<n>`.** |
