#!/usr/bin/env python3
"""Fail when a project-owned skill, or the reviewer roster, differs between agent trees.

Some harnesses read their instructions from their own directory. Where the same rule must exist
in two trees, one is canonical and the other is a mirror — and nothing tells you when they drift.
A drifted copy means two agents enforce two versions of the same rule, silently. That is the
failure this gate exists to prevent; it has been observed in the wild as a bad find-and-replace in
one tree only, and as a reviewer roster that sat ungoverned in the mirror for eleven days.

Only the skills this repository *authors* are compared. Vendored third-party skills legitimately
differ per harness (they name the agent reading them), and holding those byte-identical would fail
for the wrong reason.

Configure the four constants below. If you keep no mirror tree, delete this gate and its CI job
rather than pointing it at nothing.

Run with no arguments to check the working tree:

    python3 .githooks/skills-sync-check.py
"""
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

# --- configure -------------------------------------------------------------------------------
CANONICAL_TREE = REPO_ROOT / ".claude/skills"
MIRROR_TREE = REPO_ROOT / ".agents/skills"
CANONICAL_ROSTER = REPO_ROOT / ".claude/agents"      # *.md
MIRROR_ROSTER = REPO_ROOT / ".agents/agents"         # any extension; set to None if you keep one roster

# Skills authored by this repository. Everything else under the trees is vendored.
PROJECT_OWNED = (
    "project-architecture",
    "project-code-standards",
    "subagent-driven-development",
)

# Every reviewer role, in every tree, must carry these sections and the clauses that give them force.
# A heading alone is not the contract: shipping the heading to the mirror while the governing rules
# stay behind reads as "synchronized" to a heading-only check.
REQUIRED_CLAUSES = {
    "## Repository Contract": "the Repository Contract section",
    "## Workflow Contract": "the Workflow Contract section",
    "Read `AGENTS.md` before your first tool call": "the instruction to read AGENTS.md first",
    "risk matrix in `AGENTS.md`": "the risk-matrix selection rule",
    "source evidence": "the evidence requirement for findings",
    "cross-cutting": "the cross-cutting scan rule",
}

# Text that must appear in no role prompt: a step querying a tool this repository does not have, and
# dispatch to a role that is not in the roster. Add each one the day it bites.
FORBIDDEN = {
    "Query context manager": "instructs the agent to query a 'context manager' that does not exist here",
}
# --- end configure ---------------------------------------------------------------------------


def compare(skill):
    """Returns a list of human-readable problems for one skill directory."""
    canonical_dir = CANONICAL_TREE / skill
    mirror_dir = MIRROR_TREE / skill
    if not canonical_dir.is_dir():
        return [f"{skill}: missing from the canonical tree ({CANONICAL_TREE.relative_to(REPO_ROOT)})"]
    if not mirror_dir.is_dir():
        return [f"{skill}: missing from the mirror ({MIRROR_TREE.relative_to(REPO_ROOT)}) — copy it from the canonical tree"]

    canonical_files = {p.relative_to(canonical_dir): p for p in canonical_dir.rglob("*") if p.is_file()}
    mirror_files = {p.relative_to(mirror_dir): p for p in mirror_dir.rglob("*") if p.is_file()}

    problems = []
    for relative in sorted(canonical_files.keys() - mirror_files.keys()):
        problems.append(f"{skill}/{relative}: in the canonical tree, absent from the mirror")
    for relative in sorted(mirror_files.keys() - canonical_files.keys()):
        problems.append(f"{skill}/{relative}: in the mirror, absent from the canonical tree")
    for relative in sorted(canonical_files.keys() & mirror_files.keys()):
        if canonical_files[relative].read_bytes() != mirror_files[relative].read_bytes():
            problems.append(f"{skill}/{relative}: differs between the two trees")
    return problems


def compare_rosters():
    """Returns problems with the reviewer rosters.

    The trees may hold the same roles in different formats, so they cannot be compared byte-for-byte
    the way skills are. What must not diverge is the *set* of roles and the presence of the governing
    contract clauses: a role configured for one harness only, or governed in one harness only, means
    two agents follow two review policies with nothing reporting it.
    """
    if not CANONICAL_ROSTER.is_dir():
        return [f"reviewer roster: expected {CANONICAL_ROSTER.relative_to(REPO_ROOT)} to exist"]

    canonical_roles = {p.stem: p for p in CANONICAL_ROSTER.glob("*.md")}
    problems = [problem for path in canonical_roles.values() for problem in check_prompt(path)]

    if MIRROR_ROSTER is None or not MIRROR_ROSTER.is_dir():
        return problems

    mirror_roles = {p.stem: p for p in MIRROR_ROSTER.iterdir() if p.is_file()}
    for role in sorted(canonical_roles.keys() - mirror_roles.keys()):
        problems.append(f"role {role}: defined in the canonical roster, absent from the mirror")
    for role in sorted(mirror_roles.keys() - canonical_roles.keys()):
        problems.append(f"role {role}: defined in the mirror, absent from the canonical roster")
    problems += [problem for path in mirror_roles.values() for problem in check_prompt(path)]
    return problems


def check_prompt(path):
    """Returns problems with one role prompt: missing required clauses, or forbidden text."""
    content = path.read_text(encoding="utf-8")
    name = path.relative_to(REPO_ROOT)
    problems = [
        f"{name}: missing {description} ({clause!r})"
        for clause, description in REQUIRED_CLAUSES.items()
        if clause not in content
    ]
    problems += [f"{name}: {reason} ({text!r})" for text, reason in FORBIDDEN.items() if text in content]
    return problems


def main():
    skill_problems = [problem for skill in PROJECT_OWNED for problem in compare(skill)] if MIRROR_TREE.is_dir() else []
    roster_problems = compare_rosters()
    if not skill_problems and not roster_problems:
        if MIRROR_TREE.is_dir():
            print(f"skills in sync: {', '.join(PROJECT_OWNED)}")
        print("reviewer roster carries the required contract clauses")
        return 0

    if skill_problems:
        print("Project-owned skills are out of sync between the agent trees:\n", file=sys.stderr)
        for problem in skill_problems:
            print(f"  - {problem}", file=sys.stderr)
        print(
            f"\n{CANONICAL_TREE.relative_to(REPO_ROOT)} is canonical. Resync with:\n"
            f"  cp -R {CANONICAL_TREE.relative_to(REPO_ROOT)}/<name>/. {MIRROR_TREE.relative_to(REPO_ROOT)}/<name>/",
            file=sys.stderr,
        )
    if roster_problems:
        print("\nReviewer roster problems:\n", file=sys.stderr)
        for problem in roster_problems:
            print(f"  - {problem}", file=sys.stderr)
        print(
            "\nRosters are not byte-compared — the role set, the required contract clauses, and the\n"
            "absence of phantom tools and non-roster role names are. Format and prose may differ.",
            file=sys.stderr,
        )
    return 1


if __name__ == "__main__":
    sys.exit(main())
