---
title: Estimate for a ticket on the web view
status: accepted
---

## Intent

A customer enters their ticket number on the web view and gets a rough
estimate of when it will be called, from the tickets ahead of it, the
office workers serving that service and the average service time.

## Acceptance criteria

- Given a waiting ticket, when the customer enters its number, then they
  see a rough estimate, shown as an estimate and not as a promise.
- Given two tickets that differ only in priority, when each number is
  entered, then the estimates are the same.
- Given a service with no recent servings, or no office worker serving it,
  when a customer enters a number, then no estimate is shown.

## Known limitations

The estimate treats every ticket as normal, so it can be too late for a
priority ticket and too early when priority tickets arrive.

## Rationale

- [What customers see](../rationale/customer-view.md)
