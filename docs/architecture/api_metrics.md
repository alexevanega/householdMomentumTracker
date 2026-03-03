# Metrics Endpoint Planning

## Endpoints (v1)

### Current Streak

Endpoint: GET /api/metrics/streak

Definition
    - Consecutive calendar days ending today where the DailyWin is DONE

Response:
    {
        "data": {
            "current_streak": 4
        }
    }

### Weekly Wins

Endpoints: GET /api/metrics/weekly

Definiton
    - Return the last 7 calendar days including today, each day summarized by whether the days was DONE/PAUSED/BLOCKED/none

Response:
    {
        "data": [
            { "date": "2026-02-22", "status": "DONE" },
            { "date": "2026-02-23", "status": "DONE" },
            { "date": "2026-02-24", "status": "PAUSED" },
            { "date": "2026-02-25", "status": null },
            { "date": "2026-02-26", "status": "DONE" },
            { "date": "2026-02-27", "status": "BLOCKED" },
            { "date": "2026-02-28", "status": "ACTIVE" }
        ],
        "meta": { "count": 7}
    }

Note: returning ACTIVE for today is useful for the board's bottom strip; it's not a "win" but it is a truthful state

### Edge Rules

1. If there is no DailyWin row for a date: return { "status": null } for that day (weekly endpoint only).
2. Weekly always returns exactly 7 entries, ordered oldest ->  newest.
3. Streak counts only DONE days. PAUSED/BLOCKED break the streak.