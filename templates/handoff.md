# F`<N>`-`<n>` T`<n>` — `<Task title>` · Handoff

**Audience:** an implementing agent picking up T`<n>` cold.
**Branch:** `feature/NNN-<name>` (T1–T`<n-1>` landed; `<sha>` is the tip).
**Spec:** `docs/specs/YYYY-MM-DD-<topic>.md` §`<the sections that govern this task>`.
**Plan:** `tasks/<feature>/plan.md` → T`<n>`.

This document exists so T`<n>` lands the scope T1–T`<n-1>` were built for, and nothing else. Where it
and the spec disagree, **the spec wins** — tell the developer about the discrepancy rather than
picking one silently.

---

## 0. Read before writing anything

Non-negotiable, in this order:

1. `AGENTS.md` — the PR-blocking standing rules.
2. `<the conventions doc for the surface you are touching>`.
3. `<the spec sections>`.
4. The code you are changing: `<path>` in full — it is small.

Load the **`code-commenter`** skill before writing, revising, or deleting any comment.

## 1. The one-paragraph version

`<What this task changes, in prose, including what it deliberately leaves alone.>`

## 2. State of the world (verify these, do not assume)

- `<What an earlier task already did — including anything currently broken on the branch, and the
  fact that this task is what fixes it.>`
- `<What is committed and what is not: generated clients, snapshots, tokens with no consumer yet.>`

## 3. The work

Numbered, each with its acceptance evidence.

### 3.1 `<step>`

`<What to do. Then: how you will know it is right.>`

## 4. Traps

The specific mistakes this task invites — the shortcut that looks correct, the test that will pass for
the wrong reason, the field nothing reads yet.

## 5. Done when

`<The checks, the red-green proofs, the record left behind: ticked todo, ADR, struck DEFERRED rows.>`
