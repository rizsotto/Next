# One queue per service

## Context

A queue could have been something the office admin sets up: a named line
that holds one or more services, with workers linked to it.

Workers are matched to tickets by skill, and the next ticket is the oldest
one they can serve. Under that rule, a configured queue has no effect on
who gets called. Worse, a line that mixes services would not stay first
in, first out, since a worker skips tickets outside their skills. It could
only group tickets on the display.

## Decision

There is no queue setup. Each service has its own queue: the tickets
waiting for it.

## Consequences

Admins have one less concept. Nothing needs to pick a queue for a new
ticket, and to handle more load the admin gives the service to more
workers.

The display cannot show lines that the admin defines. Revisit if offices
need that, or if a later calling rule needs a group of services to work
on.
