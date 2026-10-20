# Requirements directory

Rules for requirement files. The format is in [`TEMPLATE.md`](TEMPLATE.md);
copy it for a new requirement.

## Contract only

A requirement says what the user can rely on. Keep out:

- Wire-level details: URL paths, field names, status codes, config keys,
  or schema fragments. Describe the operation and the data the user sees;
  the interface definition next to the code names the details.
- Implementation walkthroughs, algorithms, error-handling tables; those go
  in code comments.

## IDs

The filename without `.md` is the ID: `<area>-<short-name>.md`. The
`<area>` is a glossary noun from [`../overview.md`](../overview.md), for
example `ticket-`, `queue-` or `call-`. Add the noun to the glossary first
if it is missing.

Use the ID in links from other files and in `Requirements: <id>` tags on
tests.

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
