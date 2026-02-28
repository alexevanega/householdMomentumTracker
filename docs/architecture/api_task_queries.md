# API Task Queries

## GET /api/tasks

Filters (repeatable params):
    - status (repeatable)
        - example: ?status=BACKLOG&status=PAUSED
    - domain (repeatable):
        - example: ?domain=CHORES&domain=BILLS
    - effort (repeatable):
        - example: ?effort=TINY&effort=SMALL
    - owner_user_id (repeatable):
        - example: ?owner_user_id=1&owner_user_id=3

Policy: multiple values for the same filter are treated as IN (...)

So:

- statuses are OR'd within the same filter set
- different filter types are AND'd together

Example meaning:
    ?status=BACKLOG&status=PAUSED&domain=CHORES
    = (status in {BACKLOG,PAUSED}) AND (domain==CHORES)

## Default Sorting Policy

v1 default is fixed:
    - sort by: updated_at desc
    - tie-breaker: id desc (to prevent unstable ordering)

No "sort=" query param in v1

## Pagination Decision

v1 NO PAGINATION

Reason: household scale. add later

## Response Meta

"meta" : { "count": <number_returned> }

Even if filters are empty. Keeps UI predictable

## Invalid Filter Value Handling

- Invalid enum in any filter -> 400
    - error code: validation_error (or request_validation_error via pydantic parsing)
- Non-integer owner_user_id -> 400
- Unknown query param keys are ignored (for v1, will upgrade to rejected in further versions once logic is secured)