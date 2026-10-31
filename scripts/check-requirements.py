#!/usr/bin/env python3
"""Check requirement files against spec/requirements/CLAUDE.md and TEMPLATE.md.

Run from anywhere. Prints one line per problem; exits 1 if there are any.
"""

import re
import sys
from pathlib import Path

ROOT = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent
REQUIREMENTS = ROOT / "spec" / "requirements"
RATIONALE = ROOT / "spec" / "rationale"

STATUSES = {"proposed", "accepted", "implemented", "rejected"}
REQUIRED_HEADINGS = {"Intent", "Acceptance criteria"}
RULE_FILES = {"CLAUDE.md", "TEMPLATE.md"}


def ids_in(directory):
    return {p.stem: p for p in sorted(directory.glob("*.md")) if p.name not in RULE_FILES}


def template_headings():
    text = (REQUIREMENTS / "TEMPLATE.md").read_text()
    return re.findall(r"^## (.+)$", text, re.M)


def glossary_nouns():
    text = (ROOT / "spec" / "overview.md").read_text()
    terms = re.findall(r"^- _([^_]+)_", text, re.M)
    return {term.replace(" ", "-") for term in terms}


def backlog_ids():
    text = (ROOT / "BACKLOG.md").read_text()
    return set(re.findall(r"^- \*\*([a-z0-9-]+)\*\*:", text, re.M))


def check_requirement(path, headings, nouns):
    problems = []
    text = path.read_text()

    front = re.match(r"---\n(.*?)\n---\n", text, re.S)
    if not front:
        return ["missing front matter"]
    fields = dict(re.findall(r"^(\w+): *(.+)$", front.group(1), re.M))
    if "title" not in fields:
        problems.append("missing title")
    if fields.get("status") not in STATUSES:
        problems.append(f"bad status: {fields.get('status')}")

    found = re.findall(r"^## (.+)$", text, re.M)
    for heading in REQUIRED_HEADINGS - set(found):
        problems.append(f"missing heading: {heading}")
    unknown = [h for h in found if h not in headings]
    for heading in unknown:
        problems.append(f"unknown heading: {heading}")
    known = [h for h in found if h in headings]
    if known != sorted(known, key=headings.index):
        problems.append("headings out of template order")

    if not any(path.stem.startswith(noun + "-") for noun in nouns):
        problems.append("ID does not start with a glossary noun")
    return problems


def dangling_links(path):
    problems = []
    for target in re.findall(r"\]\(([^)]+)\)", path.read_text()):
        if re.match(r"[a-z]+:", target):
            continue
        target = target.split("#")[0]
        if target and not (path.parent / target).exists():
            problems.append(f"dangling link: {target}")
    return problems


def dangling_ids(path, known):
    """Backticked kebab-case words in spec files name a requirement, rationale or backlog item."""
    words = re.findall(r"`([a-z0-9]+(?:-[a-z0-9]+)+)`", path.read_text())
    return [f"dangling ID: {word}" for word in words if word not in known]


def dangling_tags(requirements):
    """Tests tag requirements with `Requirements: <id>[, <id>...]`."""
    problems = []
    skip = {".git", "spec"}
    for path in ROOT.rglob("*"):
        if not path.is_file() or path.suffix == ".md" or path == Path(__file__).resolve():
            continue
        if skip & set(path.relative_to(ROOT).parts):
            continue
        text = path.read_text(errors="ignore")
        for line in re.findall(r"Requirements: *(.+)", text):
            for tag in re.findall(r"[a-z0-9-]+", line):
                if tag not in requirements:
                    problems.append((path, f"dangling tag: {tag}"))
    return problems


def main():
    requirements = ids_in(REQUIREMENTS)
    rationale = ids_in(RATIONALE)
    known = set(requirements) | set(rationale) | backlog_ids()
    headings = template_headings()
    nouns = glossary_nouns()

    problems = []
    for path in requirements.values():
        problems += [(path, p) for p in check_requirement(path, headings, nouns)]

    for path in [*requirements.values(), *rationale.values()]:
        problems += [(path, p) for p in dangling_links(path) + dangling_ids(path, known)]
    for path in [ROOT / "BACKLOG.md", ROOT / "CLAUDE.md", ROOT / "spec" / "overview.md"]:
        problems += [(path, p) for p in dangling_links(path)]
    problems += dangling_tags(requirements)

    for path, problem in problems:
        print(f"{path.relative_to(ROOT)}: {problem}")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
