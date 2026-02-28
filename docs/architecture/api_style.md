## API Base Path
- All endpoints live under: /api

## Naming Conventions
- snake_case for:
    - JSON Keys
    - Query Params
    - Response Keys

## Success Response Shapes
### Single Object
    {
        "data": {}
    }

### List
    {
        "data": [],
        "meta": {
            "count": 0
        }
    }

### Error Response Shape
    {
        "error": {
            "code": "string_machine_code",
            "message": "Human Readable Message"
        }
    }

## Status Code Policy
- 200: OK: Successful GETs + succesful transitions
- 201 Created: POST creates a new resource
- 400: Bad Request: validation failures (missing fields, invalid enum, required note missing, etc.)
- 404: Not Found: resource id doesn't exist or "today has no daily win" when you require one
- 409: Conflict: rule conflicts / invariants / state machine violations
    Examples: 
        - selecting a Daily Win when one is already ACTIVE today
        - invalid task state transition
        - selecting a task that's ineligible (DONE/ABANDONED)

## Error Code Conventions
- validation_error
- not_found
- daily_win_conflict
- invalid_transition
- note_required
- definition_of_done_required