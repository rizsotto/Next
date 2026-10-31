---
title: Flow report
status: accepted
---

## Intent

A [report reader](report-credential.md#terms) can see how the office ran
and where it got stuck, so they can improve the flow. The report names no
worker. It can be viewed by day, week or month.

## Acceptance criteria

- Given a period, when a report reader opens the report, then for each
  service they see tickets taken, average and longest wait time, and
  average service time.
- Given a period, when a report reader opens the report, then they see
  tickets taken and average wait time by hour of the day.
- Given a period, when a report reader opens the report, then for each
  service they see the wait time next to how many workers have that skill.
- Given a period, when a report reader opens the report, then they see how
  many tickets ended as [no-show](call-recall.md#terms) and as [not
  served](office-end-of-day.md#terms).
- Given a period, when a report reader opens the report, then they see how
  many transfers went from each service to each other service.
- Given a period, when a report reader opens the report, then they see the
  total per [reason](priority-reason.md#terms), the share of priority
  tickets, and the average wait time of
  [normal](priority-sum-of-weights.md#terms) and of priority tickets.
- Given the report, when a report reader reads it, then no office worker is
  named in it.

## Known limitations

Plain tables only. No export to a file.

## Rationale

- [Report content](../rationale/report-content.md)
