---
title: Who can read reports
status: accepted
---

## Intent

Reports are sensitive, so only holders of the reports credential can read
them. That goes for the office admin too: setting up the system does not
include reading reports. The credential gives no right to change anything.

## Terms

- _reports credential_: the right to read reports, and nothing else. The
  office admin gives it and takes it back.
- _report reader_: anyone who holds the reports credential.

## Acceptance criteria

- Given the office admin without the reports credential, when they try to
  open the reports, then the system refuses.
- Given a small office, when the office admin gives themselves the reports
  credential, then they can read reports.
- Given a person, when the office admin gives them the reports credential
  or takes it back, then they can or can no longer read reports.
- Given a holder of the reports credential, when they try to change the
  office setup, then the system refuses, unless another right allows it.
- Given a person without the reports credential, when they try to open the
  reports, then the system refuses.

## Rationale

- [Report access](../rationale/report-access.md)
