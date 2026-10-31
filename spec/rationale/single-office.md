# Single office

## Context

Three options were on the table: one office per install, many offices of
one business in one system, or a hosted service for many businesses. Many
offices raises questions about shared services, reports across offices
and the admin role. A hosted service adds accounts and strict walls
between businesses' data.

## Decision

The MVP runs one office per install. Many offices of one business may
come later. A hosted service for many businesses is not planned.

## Consequences

Setup, roles and reports stay simple, since they all cover one office.

Avoid choices that make the move to many offices hard. Do not spend work
preparing for it either. Revisit if a chain wants one system for its
branches.
