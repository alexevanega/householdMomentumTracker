# Edge Cases

Purpose: Ensure the system behaves predictably when real life, time boundaries, or empty data states occur.

This prevents "phantom ACTIVE" states and silent corruption

---

## Midnight Rollover Policy

Core Decision:
    The system's definition of "today" is based on server-local date.

No browser-based time
No per-user timezone logic v1

---

### If Daily Win is ACTIVE at midnight
Policy:
    - Automatically transition Daily Win -> PAUSED
    - Automatically add note:
        "Auto-paused at midnight (carryover)"
    - Do NOT set completed_at
    - Task transitions to PAUSED

Reason:
    - Prevents permanent ACTIVE lock
    - Preserves historical trace
    - Allows new selection next day

No ACTIVE Daily Win may survive across calendar boundaries

---

## Late-Night Selection
If a Daily Win is selected at 11:59 PM:

    - It belongs to that calendar date
    - If the user continues working past midnight:
        - Midnight policy applies
        - It becomes PAUSED automatically

    If selection happens at 12:01 AM:
        - It belongs to the new date

    No retroactive date assignment in v1

---

## No Tasks Exist
If the backlog contains zero eligible tasks:

    - Selecting a Daily Win returns 400
    - Error message:
        - "No eligible tasks available. Add one in backlog"
    
System must NOT:

    - Auto-create placeholder tasks
    - Allow empty Daily Win
    - Crash

---

## All Tasks are DONE or ABANDONED
If not eligible statuses exist:

    - Same behavior as "No Task Exists"
    - Daily Win cannot be created

---

## Multiple DailyWin Records (Corruption Guard)
If database somehow contains more than one DailyWin for same date:

    - System must:
        - Reject activation attempts
        -Log integrity error
        - Refuse to proceed until resolved

Better to fail loudly than drift silently

---

## Missing Owner at Selection
If a Daily Win is selected and:

- Task has no owner:
    - Ownership is assigned per Ownership Rule (docs/resources/core_domain_rules/ownership_rules.md)

- If assinment fails:
    - Reject selection

No Daily Win may exist without owner

---

## Invalid State Drift
If a DailyWin exists in ACTIVE state and the Task is not ACTIVE:

- System must treat this as integrity violation
- Reject further transitions
- Log error

Task and DailyWin states must remain synchronized

---

## Server Restart During ACTIVE State
On restart:

    - No state changes occur
    - System reads DB as source of truth
    - If midnight passed while server was down:
        - Midnight rollover logic executes at next startup check

---

## Sanity Checks

- Can and ACTIVE Daily Win survive past midnight? -> No

- Is "today" defined server-side? -> Yes

- Does empty backlog break the app? -> No

- Can two DailyWins exist for the same date? -> No (hard fail)

- Are Task and DailyWin states synchronized? -> yes

---