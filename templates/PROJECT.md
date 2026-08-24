# Project configuration

The stable context an agent needs that the code does not state: what this product is, who it is for,
what it is built on, and who does what. Loaded on demand — `AGENTS.md` links here.

Keep it short and keep it current. Anything that changes per feature belongs in a spec, not here.

## Vision

`<What this product is, in three sentences. Who uses it. What it replaces. What "good" looks like a
year out.>`

## Non-goals

`<What this product deliberately is not. A non-goal prevents more work than a goal creates.>`

## Stack

| Layer | Choice | Notes |
|-------|--------|-------|
| Language / runtime | `<…>` | `<version, and why it is pinned>` |
| Framework | `<…>` | |
| Persistence | `<…>` | |
| Frontend | `<…>` | |
| Build | `<…>` | `<the exact clean gate command>` |
| CI | `<…>` | |

**Stack constraints:** `<the versions and choices a change may not silently break, and the reason>`.

## Environments

| Environment | How it runs | Data |
|-------------|-------------|------|
| Local | `<command>` | `<…>` |
| CI | `<…>` | `<…>` |

## Roles

| Role | Who | Decides |
|------|-----|---------|
| Product owner | `<…>` | scope, priority, deferrals |
| Maintainer | `<…>` | architecture, merges |
| Agents | see `.claude/agents/` | nothing — they review and implement, humans decide |

## Glossary

Domain terms an agent will otherwise guess at. Two lines each, maximum.

| Term | Means |
|------|-------|
| `<term>` | `<definition, in the product's terms>` |
