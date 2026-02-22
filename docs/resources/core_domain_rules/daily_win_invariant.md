# Daily Win Invariant

## Core Invariant

    - Exactly ONE Daily Win may be ACTIVE per calendar day

---

## Uniqueness Rule

For any given calendar date (based on server-local-date):
    - There may be one DailyWin record per date
    - If one exists:
        - It may have status ACTIVE or DONE
        - If marked PAUSED/BLOCKED with a valid note, a new Daily Win is selected.

Database-level uniqueness constraint recommended on date.

---

## Selection Rule

A Daily Win may be selected only if:
    - No Daily Win exists for that day
    - Current Daily Win is marked PAUSED/BLOCKED (with note) opening Daily Win record for selection

Selection is rejected if:
    - Today's Daily Win is ACTIVE
    - Today's Daily Win is DONE

---

## Cross-Effect Rule (Task <-> DailyWin)

When selecting a Daily Win:

    - A DailyWin record is created for today
    - The selected Task transitions to ACTIVE
    - The DailyWin must store the task_id

When resolving:

    - If DONE:
        - DailyWin -> DONE
        - Task -> DONE
        - completed at timestamp set
    - If PAUSED:
        - DailyWin -> PAUSED (note required)
        - Task -> PAUSED
    
These transitions must respect the Task State Machine

---

## Definition of Resolved

A Daily Win is considered resolved when:

    - Status is DONE
    - If PAUSED or BLOCKED -> note exists and is non-empty and DailyWin is vacated
    - If DONE -> completed_at exists

ACTIVE is the only unresolved state

---

## Sanity Checks

- Can two ACTIVE Daily Wins exists for the same day? -> No

- Can you select a new win if today's is ACTIVE? -> No

- Does resolving DONE affect the Task? -> Yes, Task becomes DONE

- Does resolving PAUSED/BLOCKED affect Task? -> Yes, Task transitions accordingly

---