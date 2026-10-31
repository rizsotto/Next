---
title: Service groups on the kiosk
status: accepted
---

## Intent

The office admin arranges services into groups, so customers find them
easily at the kiosk. Groups are only menus. A customer always ends up on a
service, and only a service gets a ticket.

## Terms

- _group_: a menu of services and other groups at the kiosk, so customers
  find a service easily.

## Acceptance criteria

- Given a group, when a customer selects it at the kiosk, then they see
  what is inside it and no ticket is created.
- Given a service, when a customer selects it at the kiosk, then they get
  a ticket for it.
- Given a group, when the office admin puts another group inside it, then
  the groups nest, to any depth.
- Given a group, when the office admin puts it in a second group, then it
  moves there, so that it has one parent.
- Given a service, when the office admin puts it in several groups, then
  customers can reach it through each of them, and it stays one service.

## Rationale

- [Service groups](../rationale/service-groups.md)
