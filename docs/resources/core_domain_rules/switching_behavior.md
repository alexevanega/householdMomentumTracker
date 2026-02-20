# Switching Behavior (Anti-Task-Hop Mechanism)

Purpose: Prevent impulsive task hopping by requiring intentional resolution before switching focus.

Momentum requires friction at the moment of escape

---

## Core Rule
    A new Daily Win cannot be activated while today's Daily Win is ACTIVE

No silent replacement
No implicit switching
No override flips

---

## Switching Procedure (Step-by-Step)

If a user wants to switch to different task:

### Step 1 - Resolve Current Daily Win

User must explicitly choose one:
    - PAUSED (note required)
    - BLOCKED (note required)
ACTIVE cannot be cleared without one of these

Only ONE Daily win may be completed (marked DONE) per calendar day due to uniqueness constraints. Therefore switching will not be allowed if Daily Win is marked DONE. Switching will only be allowed when task is BLOCKED or PAUSED (with note)

---

### Step 2 - Select New Daily Win

After BLOCKED/PAUSED resolution is accepted:
    - The Daily Win slot becomes available
    - A new eligible task may be selected
    - The new task transitions to ACTIVE

---

## Explicit Non-Allowed Behavior
The following are disallowed:

    - Replacing ACTIVE Daily Win without resolution
    - Transitioning ACTIVE -> BACKLOG to "soft drop the task"
    - Editing DailyWin record while ACTIVE to point to a new task (switching is allowed while PAUSED/BLOCKED)
    - Deleting ACTIVE DailyWin record

All switches must leave a historical trace

---

## Historical Trace Requirements
Each resolution must create a durable record:
    - Date
    - Task
    - Owner
    - Status
    - Note (if PAUSED/BLOCKED)
    - Timestamp

Switching is recorded, not erased.

This ensure:

- No invisbile abandonment
- No "I don't remember why we stopped"

---

## Optional Future Considerations

- Track number of switches per day
- Flag days with excessive switching
- Visual indicator if multiple switches occurred

Documented only as future possibilities

---

## Sanity Checks

- Can a new Daily Win be selected while one is ACTIVE? -> No

- Can you silently replace an ACTIVE task? -> No

- Must you choose PAUSED or BLOCKED before switching? -> Yes

- Does every switch create a historical record? -> Yes

- Can ACTIVE go directly to BACKLOG? -> No