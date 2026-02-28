# API Resources

## Tasks

Purpose: Store and manage all work items in the household backlog.

Key Fields (V1):
    - ID, title, domain, effort, definition_of_done, materials_needed, owner_user_id, status

    - created_at, updated_at

    Rules that must be respected: task state machine and DoD requirement (enforced server side from phase 2)

---

## Users

    Purpose: Represent household members for ownership clarity.

    Key Fields (V1):
        - ID, name, role(optional), active

    Note: No authentication. This is just attribution

---

## Daily Win

    Purpose: Enforce and record the "one ACTIVE win per calendar day" workflow

    Key Fields (V1):
        - ID, date, task_id, status, note, selected_by_user_id, completed_at

    Notes:
        - Today is determined by server-local date
        - Daily Win is the "operational driver" that can change task status

---

## Metrics

Purpose: Provide read-only aggregates needed by the board UI.

Metrics (V1): 
    - current_streak (consecutive DONE Daily Wins)
    - Weekly (last 7 days summary)

---

## Explicit Non-Resources (v1)

These are NOT API resources in phase 3:
    - suggestions engine output (phase 6)
    - energy mode
    - notifications
    - recurring tasks
    - analytics dashboards

---