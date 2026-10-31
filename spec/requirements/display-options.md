---
title: Optional display content
status: accepted
---

## Intent

The office admin chooses what displays show besides the calls. Each option
is set for the whole office.

## Acceptance criteria

- Given the average time option is on, when a display shows a service,
  then it shows the average service time of recent servings, with the
  latest ones counting more.
- Given a service, when the office admin sets how many recent servings
  count for it, then its average uses that many. A new service starts
  with a default.
- Given the average time option is on and a service has no recent
  servings, when a display shows it, then no average is shown.
- Given the waiting count option is on, when a display shows a service,
  then it shows how many tickets with normal priority are waiting.
- Given the QR code option is on, when a display is on, then it shows one
  QR code that opens the web view.
- Given an option is off, when a display is on, then that content is not
  shown.

## Rationale

- [What customers see](../rationale/customer-view.md)
