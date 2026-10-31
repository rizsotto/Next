---
title: Authentication works the same by any method
status: accepted
---

## Intent

Staff prove who they are the same way everywhere, whether by hardware such
as a badge, or by software such as a login. The rest of the system does not
depend on the method, so it can ship before any hardware does.

## Acceptance criteria

- Given a person authenticated by any method, when they use the system,
  then they have the same rights.
- Given a place where staff authenticate, the kiosk or a counter, when an
  office has no authentication hardware there, then a software method
  works.
- Given a method that fails, when someone tries to authenticate, then they
  are refused and nothing else changes.

## Rationale

- [Authentication](../rationale/authentication.md)
