# Report access

## Context

Reports can name people, directly or not. Hiding names does not solve this:
in a small office, or one with few customers, readers can guess who is who
from the numbers. So reports stay sensitive however they are built.

The person who reads reports is often not the person who sets up the
office, and neither should need the other's rights.

## Decision

Treat reports as sensitive data and control who can read them. The office
admin can always read them, and can give others a read-only reports
credential.

## Consequences

A small office has nothing to set up, since the admin is the manager. Access
control is the real protection, so what a report may contain is still a
choice to make with care.
