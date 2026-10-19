# Requirements directory

This directory captures functional and non-functional requirements for the system.
Requirements are the source of truth for what the system should do.
Tests (integration and unit) verify that implemented requirements work correctly.

Requirements are **contract-only**: they describe what the user can expect, not
where the bits live and not why the design was chosen.
The *why* belongs in [`../rationale/`](../rationale/); the *how* belongs in the
code and its comments.

### Things that do NOT belong here

- Wire-level details: URL paths, field names, status codes, config keys, or
  schema fragments. Describe the operation and the data the user sees; the
  interface definition next to the code names the details. Its format is a
  design decision, recorded in [`../rationale/`](../rationale/).
- Step-by-step implementation guides, algorithm walkthroughs, error-handling
  tables; those go in code comments next to the implementation.
- Design rationale, trade-offs, or rejected alternatives - those go in
  [`../rationale/`](../rationale/); link them from a `## Rationale` section.
- Bug reports or to-dos; those belong in the issue tracker.

## File naming

```
<area>-<short-name>.md
```

The filename (without extension) is the requirement's unique identifier. Use it
for cross-references in other requirement files and as the value tests cite in
their `Requirements:` tag (see below).

## Structure

Every requirement file must follow this structure:

```markdown
---
title: user management
status: implemented
---

### Intent

What the user expects to happen, written from the user's perspective.

### Acceptance criteria

Given-When-Then scenarios that define the details of the functionality.
These are the canonical scenarios; tests implement them.

### Non-functional constraints

Performance, platform support, backwards compatibility, etc.
Only include if relevant.

### Known limitations

Gaps in the contract that are accepted rather than planned for fixing;
link the tracking issue when one exists.
Omit the section when there are none.

### Rationale

A list of links to the rationale entries under [`../rationale/`](../rationale/)
that motivated this requirement (one short label per link, no prose).
A `rejected` requirement gives its reason here in one line.
Omit the section when there is nothing to link.
```

## Status lifecycle

| Status | Meaning |
|---|---|
| `proposed` | Drafted, waiting for the user's review |
| `accepted` | Approved by the user for implementation |
| `implemented` | Code complete, tests passing |
| `rejected` | Declined by the user (one-line reason in Rationale) |

Only the user moves a requirement out of `proposed`. Agents may create and
edit requirements, but never set `accepted` or `rejected` themselves.

## How agents should use this

1. **Before implementing a feature**: check if a requirement exists. If not,
   create one with status `proposed` and await approval before coding.
2. **Before modifying behavior**: find the requirement that governs it. Read
   acceptance criteria to understand what must not break.
3. **When the contract changes**: edit the requirement first, set its status
   back to `proposed`, and await approval before changing code or tests.
   Git history keeps the previous version.
4. **After implementing**: set status to `implemented` and add a
   `Requirements: <id>` tag to the test(s) that protect the requirement.
5. **When fixing a bug**: check if the bug violates an existing requirement. If
   so, add a test that reproduces the bug and tag it with the requirement ID.
