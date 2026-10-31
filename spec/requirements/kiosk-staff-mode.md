---
title: Staff mode on the kiosk
status: accepted
---

## Intent

The kiosk is a customer device, but staff can raise it to do more, as on a
point of sale terminal. A floor worker
[authenticates](staff-authentication.md#terms) to unlock staff mode.
Customers never get staff mode by accident.

## Terms

- _staff mode_: a state of the kiosk that a floor worker unlocks by
  authenticating, to do what customers cannot.

## Acceptance criteria

- Given a kiosk in customer mode, when a floor worker authenticates, then
  the kiosk goes into staff mode.
- Given a kiosk in customer mode, when someone without the [priority
  credential](priority-credential.md#terms) authenticates, then the kiosk
  stays in customer mode.
- Given a kiosk in staff mode, when the ticket is created, then the kiosk
  goes back to customer mode.
- Given a kiosk in staff mode, when nobody uses it for a short time, then
  the kiosk goes back to customer mode.

## Rationale

- [Ticket priority](../rationale/ticket-priority.md)
