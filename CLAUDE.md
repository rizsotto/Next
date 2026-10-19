# Project overview

Next is a "queue management system" for businesses which operates walk-in
service.

## Routing - read before modifying

Use the routing guide below to identify the project-specific instructions to read before making changes or running procedures.

| When you are about to... | Read first |
|---|---|
| Add, modify, or review a requirement (contract) | `spec/requirements/CLAUDE.md` |
| Record or look up a design decision, or a rejected option | `spec/rationale/CLAUDE.md` |
| Look up scope, actors, or domain terms | `spec/overview.md` |
| Pick up, add, or close a work item | `BACKLOG.md` |

Keep the roles separate. A requirement says *what*; a rationale entry
says *why*; the code says *how*. Reasoning does not belong in a
requirement body, and a contract does not belong in a rationale entry.

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
