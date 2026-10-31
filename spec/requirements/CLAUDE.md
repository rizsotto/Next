# Requirements directory

Rules for requirement files. The format is in [`TEMPLATE.md`](TEMPLATE.md);
copy it for a new requirement. Run `scripts/check-requirements.py` after
changing one.

## Contract only

A requirement says what the user can rely on. Keep out:

- Wire-level details: URL paths, field names, status codes, config keys,
  or schema fragments. Describe the operation and the data the user sees;
  the interface definition next to the code names the details.
- Implementation walkthroughs, algorithms, error-handling tables; those go
  in code comments.

## IDs

The filename without `.md` is the ID: `<area>-<short-name>.md`. The
`<area>` is a noun from the Actors or Glossary list in
[`../overview.md`](../overview.md), for example `ticket-`, `queue-` or
`call-`. Add the noun there first if it is missing.

Use the ID in links from other files and in `Requirements: <id>` tags on
tests.

## Terms

The glossary in [`../overview.md`](../overview.md) holds only the basic
words. A term that belongs to a detail lives under `## Terms` in the
requirement that owns it. Other files link its first use in the file, for
example `[office day](office-hours.md#terms)`, and do not define it again.

## Status

| Status | Meaning |
|---|---|
| `proposed` | Drafted or changed, waiting for the user's review |
| `accepted` | Approved by the user for implementation |
| `implemented` | Code complete; tests tagged with the ID pass |
| `rejected` | Declined by the user |

- Any change to the contract sets the status back to `proposed`.
- Before changing behaviour, read the requirement that governs it.
- A bug that breaks a requirement gets a test that reproduces it, tagged
  with the ID.
