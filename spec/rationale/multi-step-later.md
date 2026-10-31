# Multi-step services later

## Context

Some services have fixed steps, for example a driver's licence: eye test,
photo, form. Different workers do each step, so each step has to be a
service, and the customer keeps one ticket throughout.

Transfer already moves a ticket from one service to the next. What it
lacks is the plan: it is a one-off choice by the worker, not a list of
steps set in advance.

## Decision

Leave multi-step services out of the MVP. Offices handle them with manual
transfer.

## Consequences

The kiosk has to offer the first step as the service, and workers have to
know the next step. A wrong transfer sends the customer to the wrong desk.

When this returns, build it on transfer: a list of services set by the
office admin, with the system doing the transfer when a serving closes.
No call rule needs to change. Revisit if offices with step-based services
find manual transfer too clumsy.
