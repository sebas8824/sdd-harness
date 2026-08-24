# Architecture Decision Records (ADRs)

Significant architectural decisions for `<project>`. Format: [MADR](https://adr.github.io/madr/).
Each decision lives in a numbered file `NNNN-kebab-case-title.md`.

## When to write an ADR

- A change that affects multiple services or modules (a contract, an event, a schema).
- A structural tooling change (a CI workflow, a hook, a new build module).
- A non-obvious trade-off whose "why" must outlive the "what" — which already lives in the code.
- Anything touching an architecture invariant in [`AGENTS.md`](../../../AGENTS.md).
- Any change to a path listed in [`SENSITIVE-PATHS.md`](./SENSITIVE-PATHS.md) — this one is gated.

## How

1. Copy `0000-template.md` to `NNNN-title.md` (the next free number).
2. Initial status `proposed`; promote to `accepted` after review.
3. Reference the `ADR-NNNN` id in the commit message — the local hook reads the message, not the PR body.
4. If a decision becomes obsolete, mark it `superseded by ADR-XXXX`. **Never delete one.**

## Index

> Each row's status **mirrors the `Status` field of the ADR itself**; keep both in sync when
> promoting. An ADR amended by a later feature records the amendment inline, so a reader knows the
> original text is not the whole story.

| ID | Title | Status |
|----|-------|--------|
| [0000](./0000-template.md) | Template (MADR) | — |
| [0001](./0001-....md) | `<The first decision: the repository's shape and its defining boundary>` | accepted |
