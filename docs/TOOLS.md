# Tools

The harness is a set of documents plus a small number of tools that make those documents cheap to
maintain and cheap to read. Nothing here is mandatory — each entry says what it buys you and what
breaks without it.

```mermaid
flowchart LR
    agent["Coding agent<br/>(Claude Code · Codex · OpenCode · Qwen · Gemini CLI)"]
    skills["Agent Skills<br/>SDD lifecycle + craft"]
    graph["code-review-graph<br/>MCP knowledge graph"]
    rtk["rtk<br/>CLI output compressor"]
    mcp["Other MCP servers<br/>docs · design · workspace"]
    gates["Git hooks + CI gates"]

    agent --> skills
    agent --> graph
    agent --> mcp
    agent -.commands rewritten by.-> rtk
    agent --> gates
```

---

## 1. Agent Skills — the SDD lifecycle

**[addyosmani/agent-skills](https://github.com/addyosmani/agent-skills)** (MIT). This is the
foundation the harness sits on, and it is adopted as an **installed dependency, never vendored** into
the project repository — vendoring forks it and freezes the fork.

It supplies the lifecycle commands `/spec → /plan → /build → /test → /review → /ship`, plus general
engineering craft skills that auto-activate by context. The harness adds what is *repository-specific*
around them: the instruction contract, the documentation model, the review orchestration, the gates.

**Install (one-time per machine, per agent):**

```bash
# Claude Code — inside an interactive session (HTTPS avoids the SSH clone error)
/plugin marketplace add https://github.com/addyosmani/agent-skills.git
/plugin install agent-skills@addy-agent-skills

# OpenCode / Qwen / other agents (-a <agent> targets one)
npx skills add addyosmani/agent-skills -g
```

The slash commands and subagents are Claude-Code-only; the auto-activating skills work everywhere.
An agent without them follows the same discipline by hand: spec → plan → build, with a human review
between tasks. **Never `/build auto`.**

## 2. code-review-graph — the codebase knowledge graph

A persistent, incremental knowledge graph of the repository, served over MCP. It parses the codebase
with Tree-sitter, builds a structural graph of nodes and edges, and answers navigation questions
without the agent reading whole files.

**What it replaces:** a fan-out of Grep/Glob/Read calls that costs thousands of tokens and still
misses a caller. On a mid-size repo the graph holds thousands of nodes and tens of thousands of edges
across every language in the tree.

**The tools worth knowing:**

| Tool | Answers |
|------|---------|
| `semantic_search_nodes` | "Where is the thing that does X?" |
| `query_graph` | callers, callees, imports_of, tests_for |
| `get_impact_radius` | "What breaks if I change this?" |
| `detect_changes` + `get_review_context` | the changed surface and its neighbourhood, for review |
| `get_architecture_overview`, `list_flows`, `get_flow` | structure and end-to-end flows |
| `get_minimal_context` | the smallest context that answers a question |

**Wire it up** — `.mcp.json` at the repository root (see [`../.mcp.example.json`](../.mcp.example.json)):

```json
{
  "mcpServers": {
    "code-review-graph": {
      "command": "uvx",
      "args": ["--with", "sentence-transformers", "code-review-graph@<version>", "serve"],
      "cwd": "/absolute/path/to/your/repo",
      "type": "stdio"
    }
  }
}
```

Keep the graph fresh with two hooks — a `SessionStart` full update and a `PostToolUse` incremental
update after every edit. Both are in [`../.claude/settings.example.json`](../.claude/settings.example.json).
The four navigation skills (`explore-codebase`, `debug-issue`, `refactor-safely`, `review-changes`)
are how an agent is taught to reach for it.

**Without it:** everything still works, the agent just reads more files. Say so in `AGENTS.md` rather
than leaving a rule that references tools nobody has.

## 3. rtk — the CLI output compressor

**rtk (Rust Token Killer)** is a token-optimizing proxy in front of everyday development commands. A
shell hook rewrites `git status` into `rtk git status` transparently, and the agent sees a compressed
form of the output instead of the raw dump — typically a 60–90% saving on routine development
operations, which is most of what an agent runs all day.

```bash
rtk --version          # verify the install
rtk gain               # token-savings analytics
rtk gain --history     # per-command savings history
rtk discover           # analyze session history for missed opportunities
rtk proxy <cmd>        # run a command raw, unfiltered (debugging)
```

Rewriting is transparent, so nothing in the harness depends on it. It changes what a session *costs*,
not what it can do. (Watch for the name collision with an unrelated `rtk` — if `rtk gain` reports
"command not found", you have the wrong binary.)

## 4. Other MCP servers

Add servers for what your project actually touches. Common, genuinely useful ones:

- **Documentation lookup** (e.g. Context7) — current library/framework docs, so an agent stops
  answering from a stale training cutoff. Prefer it over web search for API syntax and configuration.
- **Design tooling** (e.g. Figma) — design-to-code and code-to-design for UI work.
- **Workspace / knowledge** (e.g. Notion, Drive) — where the product context lives outside the repo.
- **IDE diagnostics** — compiler and linter state without shelling out.

Rule of thumb: an MCP server earns its slot if it answers a question the agent would otherwise answer
badly, or expensively, from files.

## 5. Reviewer subagents

Independent review roles, defined once in `.claude/agents/` as portable role prompts and read by any
harness that supports subagents (and by hand where none does). This harness ships three:
`code-reviewer`, `principal-engineer`, `security-engineer`. Selection is governed by the risk matrix
in the `subagent-driven-development` skill. See [`WORKFLOW.md`](WORKFLOW.md).

## 6. Hooks and gates

Two categories, and the distinction matters:

- **Context hooks** shape what the agent knows — a `SessionStart` graph refresh, a `UserPromptSubmit`
  reminder to query the graph before grepping, a `PostToolUse` incremental index.
- **Policy gates** fail the work — a `commit-msg` hook requiring an ADR reference for a
  sensitive-path change, a CI job holding cross-harness skill copies byte-identical.

Both live in this repository: [`../.claude/settings.example.json`](../.claude/settings.example.json),
[`../.githooks/`](../.githooks/), [`../.github/workflows/config-policy.yml`](../.github/workflows/config-policy.yml).

## 7. Project-local skills

Everything the plugin does not provide, authored in `.claude/skills/` — one directory per skill, a
`SKILL.md` with frontmatter, optional `references/` loaded on demand. Plain Markdown, portable to any
agent. See [`../.claude/skills/README.md`](../.claude/skills/README.md).
