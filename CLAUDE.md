# Project overview

Next is a "queue management system" for businesses which operates walk-in
service.

## Where things live

Each kind of content lives in one place. Before editing a place, read its
rules.

| Content | Lives in | Rules |
|---|---|---|
| Contract: what the system must do | `spec/requirements/` | `spec/requirements/CLAUDE.md` |
| Reason: why a design was chosen, or an option rejected | `spec/rationale/` | `spec/rationale/CLAUDE.md` |
| Words, actors, the big picture | `spec/overview.md` | its intro |
| Open work: questions, bugs, to-dos | `BACKLOG.md` | its intro |
| How it works | the code and its comments | Code guidelines below |

A rule lives in one file. Other files link to it, never restate it.

## Spec first

No code without an `accepted` requirement. Agents propose requirements;
only the user accepts them.

## Code guidelines

Always-on, language-agnostic standards for all code:

- Maintain the existing code structure; extend before adding.
- Keep dependencies minimal; a new dependency needs a real justification,
  not convenience.
- No speculative features or over-engineering.

## Commit messages

- Imperative subject under ~70 characters, with a conventional-commit area
  prefix (`docs:`, `fix:`, `feat:`, `chore:`, `test:`, `refactor:`, ...),
  scoped where it sharpens the scan-line (`docs(requirements): ...`).
- Blank line, then a body explaining the *why*; the diff shows the *what*.
- Reference a requirement ID when the commit implements or changes that
  contract, a backlog item ID when it closes one, and a PR only when it
  adds context the body can't.

## Output format

- ASCII only in all files (no em dashes, smart quotes, Unicode bullets)
- Use hyphens, straight quotes, three dots, asterisks/hyphens for bullets
