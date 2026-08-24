---
name: project-architecture
description: <project> system architecture and boundary invariants. Use when designing or touching module boundaries, public contracts, tenancy, persistence, or anything that crosses service lines. Enforces the invariants listed in AGENTS.md.
---

# `<project>` architecture

> **Stub — fill this in.** This is the on-demand half of `AGENTS.md`: the invariants live there in one
> line each, and the reasoning, the examples, and the checklists live here. Rename the skill to your
> project (`<project>-architecture`) and update `.claude/skills/README.md`.

## The shape

```mermaid
flowchart LR
    A["<module A>"] --> B["<module B>"]
    B --> C["<store>"]
```

`<Two paragraphs: what each component owns, and the one boundary that defines the system.>`

## Invariants, with their reasoning

### 1. `<Invariant, stated as an absolute>`

**Why.** `<The failure this prevents, concretely.>`
**What violating it looks like.** `<The tempting shortcut a reviewer must recognize.>`
**The right fix instead.** `<Where the change belongs when someone reaches for the shortcut.>`

### 2. `<…>`

## Where things go

| Concern | Lives in | Never in |
|---------|----------|----------|
| `<…>` | `<…>` | `<…>` |

## Design checklist for a cross-boundary change

- [ ] `<Does it move identity or tenancy? Then where does it come from?>`
- [ ] `<Does it add a public contract? What must be regenerated in the same PR?>`
- [ ] `<Does it need an ADR? (multi-module, non-obvious trade-off, sensitive path)>`
