---
title: What each display covers
status: accepted
---

## Intent

The office admin chooses which services each display covers: all of them,
or a selected set, for example when counters are in different buildings.
Each display shows the current calls for its services.

## Acceptance criteria

- Given a display set to all services, when a ticket is called, then the
  display shows the call.
- Given two displays set to all services, when a ticket is called, then
  both show the same call.
- Given a display set to selected services, when a ticket for one of them
  is called, then the display shows the call.
- Given a display set to selected services, when a ticket for another
  service is called, then the display does not show the call.

## Rationale

- [What customers see](../rationale/customer-view.md)
