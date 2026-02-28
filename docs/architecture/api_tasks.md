# API Tasks

## List Tasks
    Endpoint: GET /api/tasks

    Query Params:
        - status (repeatable: e.g. GET /api/tasks?status=BACKLOG&status=PAUSED)
        - domain
        - effort
        - owner_user_id

    Response:

        {
            "data": [
                {
                    "id": 1,
                    "title": "Take Out Trash",
                    "domain": "CHORES",
                    "effort": "TINY",
                    "status": "BACKLOG",
                    "defintion_of_done": "Trash bins emptied and bags replaced",
                    "materials_needed: "Trash Bags",
                    "owner_user_id": 1,
                    "created_at": "2026-02-28T20:10:00",
                    "updated_at": "2026-02-28T20:10:00"
                }
            ],
            "meta": {"count": 1}
        }

    Notes: Default sort: updated_at desc

## Get Task By ID

    Endpoint: GET /api/tasks/{task_id}

    Response:
        {"data": { ...task, fields... } }

    Errors:
        404 not_found if missing

## Create Task

    Endpoint: POST /api/tasks

    Request Body:
        {
            "title": "string",
            "domain": "CHORES",
            "effort": "TINY",
            "definition_of_done": "string",
            "materials_needed": "string (optional)",
            "owner_user_id": 1
        }

    Response: 201 { "data": {...task...} }

    Validation:
        - title required
        - domain required (enum)
        - effort required (enum)
        - definition_of_done required (non-empty)

    Errors:
        400 validation_error or request_validation_error

## Update Task (fields only - NOT STATE)

    Endpoint: PUT /api/tasks/{task_id}

    Request Body: Same fields as create, but all optional. Only provided fields update

    Response: 200 { "data": {...updated task...} }

    Errors: 
        - 404 if missing
        - 400 if invalid enum / empty DoD, etc.

## Transition Task Status (the ONLY way status changes)

    Endpoint: POST /api/tasks/{task_id}/transition

    Request Body:
        {
            "to_status": "PAUSED",
            "note": "required when pausing/blocking"
        }

    Response: 200 { "data": { ...task... } }

    Rules:
        - Enforce Phase 2 state machine (invalid transitions => 409 invalid_transition)
        - if to_status is PAUSED or BLOCKED, note required (400 note_required)
        - if trying to set ACTIVE directly and your rules disallow it (likely), reject with 409 invalid_transition
        - Daily Win selection should be the normal path to ACTIVE


