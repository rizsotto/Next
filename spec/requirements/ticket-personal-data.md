---
title: No personal data on a ticket
status: accepted
---

## Intent

The system never asks a customer who they are. A ticket holds no name and
no phone number, and it does not need them.

## Acceptance criteria

- Given a customer taking a ticket, when they use the kiosk, then they are
  not asked for a name, a phone number or any other personal data.
- Given a [floor worker](priority-credential.md#terms) giving a ticket
  [reasons](priority-reason.md#terms), when they do it, then they can only
  pick from the list, with no free text.
- Given a serving, when it ends, then the ticket records the office worker
  who served it.
- Given the worker recorded on a ticket, when anyone other than a holder of
  the [reports credential](report-credential.md#terms) looks at the ticket,
  then they do not see it.

## Rationale

- [Personal data](../rationale/personal-data.md)
