# Development Skills

Coding-agent skills for building `<project>`. This folder holds **only** skills that the
[Agent Skills](https://github.com/addyosmani/agent-skills) plugin does not provide — the
project-specific ones, plus any language/stack depth and knowledge-graph navigation your work needs.
Single source of truth: a skill lives here once, never copied per tool.

> **Agent Skills supplies the SDD lifecycle.** Spec/plan/build/test/review/ship and general
> engineering craft come from the plugin (installed, not vendored — see `AGENTS.md`). The Process
> skills below do not replace that lifecycle; they define this repository's execution and review
> orchestration.

## Installing Agent Skills (one-time per machine, per agent)

`AGENTS.md` names the lifecycle; the install lives here so no session pays for it.

- **Claude Code:** in an interactive session run
  `/plugin marketplace add https://github.com/addyosmani/agent-skills.git`, then
  `/plugin install agent-skills@addy-agent-skills`. (The HTTPS URL avoids the SSH clone error.)
  Gives commands + skills + subagents + hooks.
- **OpenCode / Qwen / other agents:** `npx skills add addyosmani/agent-skills -g` (`-a <agent>` targets
  one). Gives the auto-activating skills only; the slash commands and subagents are Claude-Code-only,
  but the SDD behaviour still fires.

## Reviewer roles

`.claude/agents/*.md` is canonical. A second harness's roster (if you keep one) mirrors it, and a CI
job holds the two in agreement — see `.githooks/skills-sync-check.py`.

| Role | Selected for |
|------|--------------|
| `principal-engineer` | Changes in the primary language/framework |
| `code-reviewer` | Everything else, and the fallback when no specialist matches |
| `security-engineer` | Security, auth, tenancy, secret handling |

Selection is governed by the risk matrix in `subagent-driven-development`. **Do not invent a role**,
and do not keep roles for surface the repository does not have — a reviewer for infrastructure you
never wrote reports on nothing. Delete them; git history has them if that changes.

## Layout

```
.claude/skills/
└── <skill-name>/
    ├── SKILL.md          # required: frontmatter (name + description) + body
    └── references/       # optional: supporting docs loaded on demand
```

The `description` is the activation trigger. Name the situations, symbols, and phrases that should
pull the skill in — not just its topic.

## Discovery per tool

The content here is plain Markdown, portable to any agent. Claude Code auto-discovers
`.claude/skills/` and activates a skill by its `description`. Other agents read this index and load
the relevant `SKILL.md`.

---

## Skill index (by group)

### 1. Project-specific (a thin layer over Agent Skills)

| Skill | When to use |
|-------|-------------|
| `project-architecture` | Module boundaries, contracts, tenancy — the system invariants |
| `project-code-standards` | Writing code here — language conventions + stack-constraint checklist |
| `code-commenter` | Writing, updating or deleting any comment — budgets, one-home rule, delete-on-sight list |

### 2. Process (repo-local, complements Agent Skills)

| Skill | When to use |
|-------|-------------|
| `subagent-driven-development` | Executing an approved plan: task loop, risk-matched review, finding discipline |
| `systematic-debugging`\* | Any bug or test failure, before proposing fixes |
| `verification-before-completion`\* | Before claiming done/fixed/passing — evidence first |

### 3. Codebase navigation (knowledge graph)

Require the code-review-graph MCP server; prefer over raw grep when available. These ship with the
server's own skill pack — install rather than copy.

| Skill | When to use |
|-------|-------------|
| `explore-codebase` | Understanding structure via the knowledge graph |
| `debug-issue` | Graph-powered debugging (callers, impact tracing) |
| `refactor-safely` | Refactor planning with dependency analysis |
| `review-changes` | Structured review using change detection + impact radius |

### 4. Stack depth (add what your stack needs)

| Skill | When to use |
|-------|-------------|
| `<framework>` | `<general development in the primary framework>` |
| `<framework>-testing` | `<the test slices, and which to reach for first>` |
| `<data-layer>-patterns` | `<the pitfalls your ORM or client makes easy>` |

\* Provided by the Agent Skills plugin — listed here for discovery, not vendored.

---

## Rules

- One language across the repository, including frontmatter (see the `AGENTS.md` language policy).
- One skill = one directory. Keep `SKILL.md` focused; push detail into `references/`.
- A new skill is added to the right group table above in the same PR.
- Do **not** re-add a skill the Agent Skills plugin already provides.
