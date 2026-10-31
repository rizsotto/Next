---
title: Shortcuts for setting skills
status: accepted
---

## Intent

Skills are always single services, but the office admin should not have to
tick them one by one. They can give a worker a whole group at once, or copy
the skills of another worker.

## Acceptance criteria

- Given a group, when the office admin assigns it to a worker, then the
  worker gets every service inside it, at any depth, as skills.
- Given a worker, when the office admin copies skills from another worker,
  then the worker gets that worker's skills, on top of their own.
- Given a shortcut already used, when a service is later added to the group
  or to the other worker, then the worker's skills do not change.

## Rationale

- [Service groups](../rationale/service-groups.md)
