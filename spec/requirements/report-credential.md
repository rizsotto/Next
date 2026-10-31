---
title: Who can read reports
status: accepted
---

## Intent

Reports are sensitive, so only the office admin and holders of the reports
credential can read them. The credential lets a manager read reports with
no right to change anything.

## Acceptance criteria

- Given the office admin, when they open the reports, then they can read
  them, with no credential needed.
- Given a person, when the office admin gives them the reports credential
  or takes it back, then they can or can no longer read reports.
- Given a holder of the reports credential, when they try to change the
  office setup, then the system refuses, unless another right allows it.
- Given a person without the reports credential, when they try to open the
  reports, then the system refuses.

## Rationale

- [Report access](../rationale/report-access.md)
