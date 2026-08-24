# Session Start Prompt

Reusable warm-start for any coding-agent session on **`<project>`**. This is **ignored local
continuity, not durable policy**: update it as work moves; put enduring rules in `AGENTS.md`, an ADR,
or a tracked skill.

## How to use

1. Open the agent in `<repo path>`.
2. Read this file, then `tasks/<feature>/plan.md` and `tasks/<feature>/todo.md`.
3. Start with the prompt at the bottom of this file.

## If you are not the primary harness

`AGENTS.md` is canonical and every agent reads it — a harness-specific file is only a pointer to it.
Two things are harness-specific and should be substituted rather than skipped:

- **Lifecycle commands** (`/spec`, `/plan`, `/build`, `/review`) come from the Agent Skills plugin.
  Install the same behaviour with `npx skills add addyosmani/agent-skills -g`, or follow the
  discipline by hand: spec → plan → build with a human review between tasks. **Never vibecode a whole
  slice in one pass.**
- **`.claude/agents/`** holds the reviewer role definitions, written as portable role prompts on
  purpose — read them as prompts and run the review yourself if your harness has no subagents.
- The **knowledge-graph MCP tools** may not be available to you. Check; if they are missing, say so
  rather than silently falling back to file scanning for everything.

---

## Where the work stands

**Branch: `feature/NNN-<name>`.** `<Pushed or not.>` Do not push without explicit confirmation.

`<Which feature is in progress, which spec is approved, where the plan and todo live.>`

### Done and committed

- **T`<n>` — `<title>`** (`<sha>`). `<What landed, and the one non-obvious property a reviewer must
  not undo. Name the test that pins it.>`

### `<Current task>` — in progress / next

`<What is left, and which decisions are already settled so they are not re-opened.>`

## Carry forward — the failures this feature keeps repeating

- **A green suite is not evidence.** `<The tests found passing for the wrong reason, counted.>` Prove
  a new test bites — remove the behaviour it names, watch it fail, restore it.
- `<The rule that has now been missed N times in this repository.>`

## Still open, not blocking

- `<Question, and who decides it.>`

---

## Start prompt

> `<The literal prompt to paste. Name the task, the plan file, the settled context not to re-derive,
> and the two standing constraints most likely to be broken. End with: do not push.>`
