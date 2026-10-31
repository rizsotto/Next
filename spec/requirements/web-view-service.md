---
title: Web view of a service
status: accepted
---

## Intent

A customer can follow their service on their own phone, from anywhere, so
they can step out during the wait. They open one web page for the whole
office and type their ticket number, with no app and no login. The system
never contacts them.

## Acceptance criteria

- Given a customer away from the office, when they enter their ticket
  number on the web view, then they see the same content a display shows
  for the ticket's service.
- Given a number that matches no ticket from today, when a customer enters
  it, then they are told so.
- Given an open web view, when a ticket for that service is called, then
  the call appears without the customer doing anything.
- Given the web view, when a customer opens it, then they are not asked
  for a login or for any personal data.

## Known limitations

Reaching the web view from outside the office depends on how Next is
installed, and the MVP may not cover it; see `web-view-reach` in the
backlog.

## Rationale

- [What customers see](../rationale/customer-view.md)
