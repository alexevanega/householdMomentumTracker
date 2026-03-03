# Cross Resource Effects

## Selection Effects

When: POST /api/daily-win/select

Preconditions: 
    - Reject if today has a DailyWin with status = ACTIVE -> 409 daily_win_conflict
    - Reject if today has DailyWin with status = DONE -> 409 daily_win_conflict
    - Allow if today has no DailyWin

Effects:
    - Ensure a DailyWin row exists for today
    - Set daily_win.task_id = <task_id>
    - Set daily_win.status = ACTIVE
    - Set daily_win.note = null 
    - Set daily_win.selected_by_user_id = <selected_by_user_id>
    - Set daily_win.completed_at = null
    - Set the Task's status = ACTIVE

Postconditions:
    - GET /api/daily-win/today returns the DailyWin with embedded Task in ACTIVE state

## Resolve DONE Effects (Day Closes)

When: POST /api/daily-win/resolve with "resolution": "DONE"

Preconditions:
    - Reject if no DailyWin exists today -> 409 daily_win_conflict
    - Reject if today's DailyWin is not ACTIVE -> 409 daily_win_conflict

Effects:
    - Set daily_win.status = DONE
    - Set daily_win.completed_at = now()
    - associated Task status = DONE

Postconditions: 
    - The day is closed: any further call to /api/daily-win/select returns 409 for that data

## Transition PAUSED/BLOCKED Effects (Slot Vacated)

When: POST /api/daily-win/transition with "to_status": "PAUSED" | "BLOCKED"

Preconditions:
    - Reject if no DailyWin exists today -> 409 daily_win_conflict
    - Reject if note missing/blank -> 400 note_required
    - Reject if today's DailyWin is already DONE -> 409 daily_win_conflict

Effects: 
    - Set daily_win.status = PAUSED or BLOCKED
    - Set daily_win.note = <note>
    - Set daily_win.completed_at = null
    - Set associated Task status = PAUSED or BLOCKED

Postconditions:
    - A new Daily Win selection is allowed (via subsequent /api/daily-win/select call)

## Task Transition Constraints Relative to Daily Win

Even though tasks have their own /api/tasks/{id}/transition the Daily Win workflow has priority.

- If a task is today’s Daily Win, task status changes that affect it must happen via Daily Win endpoints, not the task transition endpoint.

## Data Integrity Invariants (must always be true)

1. If daily_win.status = DONE then daily_win.completed_at is not null

2. If daily_win.status in {PAUSED, BLOCKED} then daily_win.note is note null/blank

3. If daily_win.status = ACTIVE then associated task.status = ACTIVE

4. If daily_win.status = DONE then associated task.status = DONE

5. If daily_win.status in {PAUSED, BLOCKED} then associated task.status matches it

## Definition of Done

If POST /api/tasks/{task_id}/transition is called and that task is the task for today's Daily Win:

If to_status = DONE
    - Update Task -> DONE
    - Update today's DailyWin -> DONE
    - Set DailyWin.completed_at = now
    - The day is closed

If to_status = PAUSED or BLOCKED
    - Require note (400 note_required)
    - Update Task -> PAUSED/BLOCKED
    - Update today's Daily Win -> same status
    - Set DailyWin.note = note
    - completed_at remains null
    - Slot is vacated (selection allowed)

Any other to_status (BACKLOG, ABANDONED, etc.)

- Reject (409 invalid_transition)