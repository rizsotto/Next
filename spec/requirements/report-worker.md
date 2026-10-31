---
title: Worker report
status: accepted
---

## Intent

A [report reader](report-credential.md#terms) can review how each office
worker performs. Offices choose whether to use this at all: it is off until
the office admin turns it on. It can be viewed by day, week or month.

## Acceptance criteria

- Given a new office, when a report reader opens the reports, then there is
  no worker report.
- Given the office admin, when they turn the report on, then report readers
  can open it.
- Given a holder of the reports credential, when they try to turn the
  report on, then the system refuses.
- Given a period, when a report reader opens the report, then for each
  worker and service they see tickets served, average service time,
  [no-shows](call-recall.md#terms) marked and
  [recalls](call-recall.md#terms).
- Given a period, when a report reader opens the report, then for each
  worker they see their time at a counter with nothing to do.
- Given the report, when a report reader reads it, then workers are only
  compared within a service, and there is no overall ranking.

## Known limitations

Plain tables only. No export to a file.

## Rationale

- [Report content](../rationale/report-content.md)
