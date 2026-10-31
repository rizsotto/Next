---
title: Office hours
status: accepted
---

## Intent

The office admin sets, for each day of the week, when the office opens,
when it stops taking new tickets, and when it closes. An office day runs
from opening to closing, so an office open past midnight needs no special
rule.

## Acceptance criteria

- Given the opening time, when it comes, then a new office day starts and
  the kiosk issues tickets.
- Given the last-ticket time, when it has passed, then the kiosk issues no
  new tickets and tells the customer so.
- Given the last-ticket time has passed, when workers press "next", then
  they keep getting the tickets still waiting.
- Given a day of the week with no hours set, when that day comes, then the
  office stays closed and the kiosk issues no tickets.

## Rationale

- [Closing](../rationale/closing.md)
