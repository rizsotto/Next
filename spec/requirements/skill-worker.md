---
title: Office worker skills
status: accepted
---

## Intent

The office admin sets the skills of each office worker. A worker only ever
gets customers they can serve.

## Acceptance criteria

- Given a worker, when the office admin gives them one or more skills,
  then those are the services they can get tickets for.
- Given a ticket for a service outside a worker's skills, when the next
  ticket is picked for that worker, then that ticket is not picked.
- Given a worker who moves to a different counter, when the next ticket
  is picked for them, then their skills are the same as before.

## Rationale

- [One queue per service](../rationale/one-queue-per-service.md)
