# API Daily Win

## Endpoints

### Get Today's Win

Endpoint: GET /api/daily-win/today

Behavior: If no daily win selected for today: return data: null (NOT 404)

Response:

{
    "data": null
}

or 

{
    "data": {
        "id": 10,
        "date": "2026-02-28",
        "task": {
            "id": 12,
            "title": "Take Out Trash",
            "domain": "CHORES",
            "effort": "TINY",
            "status": "ACTIVE",
            "definition_of_done": "Trash bins emptied and bags replaced",
            "materials_needed": "Trash Bags",
            "owner_user_id": 1
        },
        "status": "ACTIVE",
        "note": null,
        "selected_by_user_id": 1,
        "completed_at": null,
        "created_at": "2026-02-28T20:10:00",
        "updated_at": "2026-02-28T20:10:00"
    }
}

Note: Task object will be embedded. Board/Editor will need it constantly

---

## Select Today's Daily Win

Endpoint: POST /api/daily-win/select

Request:
    {
        "task_id": 12,
        "selected_by_user_id": 1
    }

Rules (server enforced)
    - If today already has an ACTIVE Daily Win -> 409 daily_win_conflict
    - If today has a resolved Daily Win (DONE) no more Daily Wins can be added
    - If today's daily win transitions (PAUSED/BLOCKED) a new Daily Win is selected
    - Task must be eligible (not DONE/ABANDONED; and generally not already ACTIVE elsewhere)

Cross-effects:
    - Create/ensure DailyWin row for today
    - Set DailyWin.status = ACTIVE
    - Set Task.status = ACTIVE

Response:
    - 201 { "data": <today daily win object> }

---

## Resolve Today's Daily Win

Endpoint: POST /api/daily-win/resolve

Request:
    {
        "resolution": "DONE",
        "resolved_by_user_id": 1
    }

Rules:
- If no Daily Win exists for today -> 409 (daily_win_conflict)
- DONE:
    - sets DailyWin.status = DONE
    - sets Task.status = DONE
    - sets DailyWin.completed_at = now

Response:
    - 200 { "data": <updated today daily win> }

---

## Transition Today's Daily Win

Endpoint: POST /api/daily-win/transition

Request:
    {
        "to_status": "PAUSED" or "BLOCKED",
        "note" : "required",
        "resolved_by_user_id": 1
    }

Rules:
    - If daily win is marked as PAUSED/BLOCKED, a new daily win must be selected.
    - PAUSED/BLOCKED:
        - note required (400 note_required)
        - sets DailyWin.status accordingly
        - sets Task.status accordingly
        - completed_at remains null
        - new daily win task selected

Response:
    - 200 { "data": <updated taday daily win> }

---

## Get Daily Win History

Endpoint: GET /api/daily-win/history?start=YYYY-MM-DD&end=YYY-MM-DD

Response:
    {
        "data": [
            {
                "date: "2026-02-27",
                "status": "DONE",
                "task": { "id": 7, "title": "Pay electric bill", "owner_user_id": 1},
                "note": null,
                "completed_at": "2026-02-27T21:11:00"
            }
        ],
        "meta": { "count": 1 }
    }

---

## Defaults

- If start/end omitted:
    - default to last 7 days