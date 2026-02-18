# Resolution Rules
    - What does it mean to clear the Daily Win slot?

## Resolved vs Unresolved

**Unresolved State**
    - ACTIVE
If a daily Win is ACTIVE, the Daily Win slot for that date is locked.

---

### Resolved States
- DONE
- PAUSED (note required)
- BLOCKED (note required)

Only resolved states allow a new Daily Win to be selected.

---

## DONE Resolution Requirements
A Daily Win may transition to DONE only if:
    - The Task's Definition of Done is satisfied
    - completed_at timestamp is set
    - The Task transitions to DONE

If these conditions are not met -> reject

---

## PAUSED Resolution Requirements
A Daily Win may transition to PAUSED only if:
    - A note is provided
    - Note is non-empty after trimming whitespace
    - The Task transitions to PAUSED

Purpose of note:
    - Must explain why work stopped voluntarily

Valid Examples:
    - "Ran out of time"
    - "Energy too low to continue
    - "Switching to urgent bill"

Invalid Examples:
    - ""
    - "."

Keep enforcement minimal but real

---

## BLOCKED Resolution Requirements
A Daily Win may transition to BLOCKED only if:
    - A note is provided
    - Note is non-empty after trimming whitespace
    - The Task transitions to BLOCKED

Purpose of note:
    - Must describe the external constraint preventing progress

Valid Examples:
    - "Need to buy paint"
    - "Waiting on Elijah to confirm"
    - "Cannot access attic ladder"

---

## Slot Clearance Rule
The Daily Win slot for the day becomes eligible for new selection only when:

    - Status is DONE, PAUSED, BLOCKED
            AND
    - All required resolution conditions are satisfied

ACTIVE is the only locking state.

---

## ABANDONED Policy
For v1:
    - ABANDONED applies to Tasks only
    - DailyWin does not have an option to ABANDON
    
If a task must be abandoned midday:

    Procedure:

        1. Resolve DailyWin as PAUSED or BLOCKED (with note)
        2. Then transition Task to ABANDONED seperately

    This preserves the daily record.

---

## Sanity Questions

- Can you pick a new Daily Win if today's is PAUSED? -> Yes

- Can you pick a new Daily Win if today's is BLOCKED? -> Yes

- Can you pick a new Daily Win if today's is ACTIVE? -> No

- Can you resolve DONE without setting completed_at? -> No

- Can you pause/block without a note? -> No

- Can DailyWin ever be ABANDONED? -> No, not directly

---