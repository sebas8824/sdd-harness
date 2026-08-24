# `<project>` Roadmap

> Phased roadmap. Each phase decomposes into SDD features (`/spec → /plan → /build → /test → /review
> → /ship`). **A phase does not start until the previous one meets its green criteria.**
>
> **This file is authoritative for phase and feature numbering.** When the roadmap is re-sequenced,
> add a mapping table below rather than rewriting older specs and ADRs — those are point-in-time
> records and are never edited to match a later numbering.

<!--
### Re-sequenced YYYY-MM-DD — <why>

| Prior | Now | |
|-------|-----|-|
| old F3-1 (…) | **superseded** | replaced by … |
| old F3-2…F3-7 | **Phase 4** (F4-1…F4-6) | … |

Why: <the product reason, in two sentences>.
-->

---

## Phase 0 — `<Foundation>`

**Green = `<the observable condition that lets Phase 1 start>`.**

- [ ] F0-1: `<feature>`
- [ ] F0-2: `<feature>`
- [ ] F0-3: `<CI: build + tests + lint>`
- [ ] F0-4: `<CONTRIBUTING: the MANDATORY/SIGNAL gate split, branching, PRs>`

## Phase 1 — `<…>`

**Green = `<…>`.**

- [ ] F1-1: `<feature>`

## Phase 2 — `<…>`

**Green = `<…>`.**

- [ ] F2-1: `<feature>`

---

## Explicitly deferred

Product-level, strategic deferrals — the "not this year" decisions. Implementation-level punts live in
[`DEFERRED.md`](DEFERRED.md), grouped by the feature that will absorb them.

| Item | Why it waits | Earliest phase |
|------|--------------|----------------|
| `<capability>` | `<the reason, not just "later">` | Phase `<N>` |
