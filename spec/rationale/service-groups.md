# Service groups

## Context

Skills, the queue, the prefix and the average time all hang off a service.
If a group could be picked, it would need all of those too, and a ticket
for "Vehicles" raises the question of who serves it.

A customer might look for a service in more than one place. A full graph
of groups would allow every path, but it needs cycle checks and a harder
admin screen.

## Decision

Only services can be picked; groups are menus. Groups form a tree of any
depth, and a service can sit in several groups.

A shortcut for skills is a one-time action: skills stay on single services
and a worker never holds a group.

## Consequences

A customer who is not sure what they need gets no general choice. The
office can add a generic service, such as "Vehicles: not sure", with no
new rule.

A service in several groups covers the need for many paths, and a tree of
groups can have no cycles. Revisit if an office needs a whole group in two
places.

A new service in a group reaches nobody until the admin gives it out.
