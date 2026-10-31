# Oldest first

## Context

A customer picks a service, and an office worker can do one or more
services. The worker does not know about strategies; they ask for the next
customer and the system picks one they can serve.

The main options were oldest first, or priority, where the admin ranks
services for each worker. Priority lets an office favor a key service, but
a low-ranked service can starve at busy times, and customers see later
numbers go ahead of them.

## Decision

Pick the ticket that has waited longest among those the worker can serve.

## Consequences

The rule is fair and easy to explain. It cannot favor a key service.

This is the MVP rule. Other rules may come later; revisit if offices need
to favor a service.
