---
name: code-commenter
description: Rules for writing, updating or deleting a code comment in any language — Java, TypeScript, SQL, YAML, shell. Use whenever the intent is to add a comment or Javadoc, revise an existing one, or decide whether one should exist at all. Enforces word budgets, the one-home rule (cite the ADR, do not re-argue it), and the principle that a change altering no behaviour alters no comment.
---

# Code Commenter

Comments are the only part of a codebase nothing verifies. They cost tokens on every read,
they rot silently, and a wrong one is worse than none. Default to **no comment**; make each
one earn its place.

## The test, before you type

Name the reader's question the comment answers. Then find the answer elsewhere:

- **In the signature or the code?** Delete it.
- **In an ADR or a spec?** Cite the id — `(ADR-0015)`, `@spec docs/specs/…` — never re-argue it.
- **Nowhere, and a maintainer would get it wrong without it?** Write it, once, at one site.

If you cannot state the question in a sentence, there is no comment to write.

## Budgets

Hard limits, checkable at a glance. Over budget means cut, not reformat.

| Comment | Budget |
|---|---|
| Class / type header | **< 100 words** — the intent, only if the name and shape do not already give it |
| Method / function | **< 50 words** — and only on genuinely complex ones |
| Inline, inside a body | one or two lines, only in a high-complexity method |

**A comment block never exceeds the code it describes.** A 25-line Javadoc over an 8-line
interface is the failure this skill exists to prevent.

## Where comments belong, and where they do not

- **Service and domain classes** carry the explanation: the invariant, the ordering
  constraint, the reason a cheaper approach was rejected.
- **DTOs, records, entities, config holders, plain mappers** carry none. A type that holds
  no logic has no *why*. Field-by-field Javadoc restating the field name is pure cost.
- **Inline comments are not line annotations.** Never narrate a single statement. If a body
  needs a running commentary, the method wants splitting, not documenting.
- **Tests**: name the behaviour in the test method name. A comment is warranted only to say
  what a passing assertion would otherwise let a reader assume wrongly.

## Editing an existing comment

**A change that alters no behaviour alters no comment.** Moving a line, renaming a local,
reformatting, extracting a helper — none of these are reasons to touch the prose. Rewriting
a comment you did not have to rewrite is a diff a reviewer must read for nothing.

Update a comment only when the behaviour it describes changed, and then **delete more than
you add**: a comment that has survived three edits is usually three explanations layered on
one another.

Delete on sight:
- Prose restating what the next line does.
- A rationale that has been promoted to an ADR or spec since it was written — replace with
  the id.
- Commented-out code. Git has it.
- A `TODO` with no target. Either fix it, or record it where deferrals are tracked.

## The one comment that always earns its place

A **deliberate, local violation of a rule the repository states elsewhere**. Without a
sentence at the site, the next reviewer "fixes" it back into the defect. One sentence naming
the rule and why this site is the exception — not a paragraph defending it.

## Language notes

- **Java**: Javadoc for the type's intent and for public contract surprises. No `@param` /
  `@return` that only re-says the parameter name. `@spec` on code implementing a spec.
- **TypeScript/React**: no JSDoc on typed props — the type is the documentation. Comment a
  non-obvious effect ordering, a cache-merge rule, or a deliberate non-refetch.
- **SQL migrations**: the header carries the *why now* — what the column is for, what it
  costs, what a reader would otherwise assume. The DDL says the what.
- **All languages**: one language across the repository, per the `AGENTS.md` language policy.

## See also

`AGENTS.md` (Response & Editing Style), `project-code-standards`.
