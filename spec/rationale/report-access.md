# Report access

## Context

Reports can name people, directly or not. Hiding names does not solve this:
in a small office, or one with few customers, readers can guess who is who
from the numbers. So reports stay sensitive however they are built.

The person who reads reports is often not the person who sets up the
office, and neither should need the other's rights.

## Decision

Treat reports as sensitive data and control who can read them. Reading
takes a read-only reports credential, which the office admin gives out.
Setting up the system does not include reading reports, so the admin needs
the credential too, by default.

## Consequences

A small office has one extra step: the admin gives themselves the
credential. Access control is the real protection, so what a report may
contain is still a choice to make with care.
