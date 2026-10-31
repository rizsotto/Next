---
title: Reasons are removed at the end of the day
status: accepted
---

## Intent

A reason can say something sensitive about a customer, so it stays on a
ticket only for the office day. After that, only totals remain.

## Acceptance criteria

- Given a ticket with reasons, when the office day ends, then its reasons
  are removed, whatever state it ended in.
- Given a ticket whose reasons were removed, when anyone looks at it, then
  they cannot see which reasons it had.
- Given a ticket with priority, when the office day ends, then its exact
  priority is removed too, and it keeps only a mark that it was not normal.
- Given an office day that has ended, when a reader opens the reports,
  then they see how many tickets had each reason that day.

## Rationale

- [Personal data](../rationale/personal-data.md)
