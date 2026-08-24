#!/usr/bin/env python3
"""Fail when a changed file matches a sensitive path and no ADR-NNNN is referenced.

The list of paths is the single source of truth in docs/architecture/adr/SENSITIVE-PATHS.md
("## Listed paths"). Shared by the local .githooks/commit-msg hook and the CI gate in
.github/workflows/config-policy.yml, so both enforce exactly the same list.

Changed files arrive on stdin (newline-separated) unless --files-from is given.
The ADR reference is searched in --message-file or --message.
"""
import argparse
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SENSITIVE_DOC = REPO_ROOT / "docs/architecture/adr/SENSITIVE-PATHS.md"
ADR_REF = re.compile(r"\bADR-\d{4}\b")


def load_patterns(doc):
    """Extract every backtick-quoted glob from the '## Listed paths' section."""
    patterns, in_section = [], False
    for line in doc.read_text(encoding="utf-8").splitlines():
        if line.startswith("## "):
            in_section = line.strip() == "## Listed paths"
            continue
        if in_section:
            patterns.extend(re.findall(r"`([^`]+)`", line))
    return patterns


def expand_braces(glob):
    """Expand a single {a,b,c} group (recursively) into concrete globs."""
    match = re.search(r"\{([^{}]*)\}", glob)
    if not match:
        return [glob]
    prefix, suffix = glob[: match.start()], glob[match.end() :]
    expanded = []
    for option in match.group(1).split(","):
        expanded.extend(expand_braces(prefix + option + suffix))
    return expanded


def glob_to_regex(glob):
    """Translate a glob to a full-match regex: ** spans '/', * stays within a segment."""
    index, out = 0, []
    while index < len(glob):
        if glob[index : index + 2] == "**":
            out.append(".*")
            index += 2
        elif glob[index] == "*":
            out.append("[^/]*")
            index += 1
        elif glob[index] == "?":
            out.append("[^/]")
            index += 1
        else:
            out.append(re.escape(glob[index]))
            index += 1
    return re.compile("^" + "".join(out) + "$")


def sensitive_matches(files, patterns):
    regexes = [glob_to_regex(g) for pattern in patterns for g in expand_braces(pattern)]
    return [f for f in files if f and any(r.match(f) for r in regexes)]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--message-file", help="file holding the text to search for ADR-NNNN")
    source.add_argument("--message", help="text to search for ADR-NNNN")
    parser.add_argument("--files-from", help="file with changed paths (default: stdin)")
    args = parser.parse_args()

    message = Path(args.message_file).read_text(encoding="utf-8") if args.message_file else args.message
    raw = Path(args.files_from).read_text(encoding="utf-8") if args.files_from else sys.stdin.read()
    files = [line.strip() for line in raw.splitlines() if line.strip()]

    hits = sensitive_matches(files, load_patterns(SENSITIVE_DOC))
    if hits and not ADR_REF.search(message):
        sys.stderr.write(
            "\nSensitive-paths policy: this change touches path(s) that require an ADR reference:\n"
            + "".join(f"  - {hit}\n" for hit in hits)
            + "\nReference an `ADR-NNNN` in the commit message (or PR body), or justify the exception.\n"
            + "See docs/architecture/adr/SENSITIVE-PATHS.md\n"
        )
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
