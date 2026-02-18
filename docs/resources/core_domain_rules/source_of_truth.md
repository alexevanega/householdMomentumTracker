# Source of Truth Placement

Purpose: Ensure that behavioral invariants cannot be bypassed by UI decisions.

The server is the authority
The frontend is a client

---

## Core Principle
    All state machine enforcement and Daily Win invariants must be enforced server-side.

The frontend may guide
It may validate
It may prevent obvious errors

But it does not decide

---

## What the Frontend is Allowed To Do
Frontend may:
    - Perform client-side validation for user convenience
    - Hide invalid transitions
    - Disable buttons when action is not allowed
    - Display error message clearly

Frontend may NOT:
    - Override invariant rules
    - Create multiple DailyWins
    - Transition invalid Task states
    - Bypass note requirements
    - Modify state directly in DB

---

## Where Enforcement Lives
Enforcement must occur in:
    - Domain/service layer logic
    - API endpoint handlers
    - Database-level constraints (where appropriate)

Specifically:
    - Task transition validation lives in server domain logic.
    - Daily Win invariant (one ACTIVE per day) enforced server-side
    - Note requirement enforced server-side
    - DoD enforcement enforced server-side
    - Ownership requirement enforced server-side

Database constraints support invariants but do not replace domain logic

---

## Database Guardrails (Support, Not Authority)
Database should enforce:
    - Unique DailyWin per date
    - Foreign key integrity (Task <-> DailyWin)
    - Non-null required fields

But DB should NOT:
    - Encode full business logic transitions
    = Replace the state machine logic layer

The application layer enforces behavior
The database enforces structure

---

## Anti-Bypass Rule
Even if:
    - Someone manually crafts a request
    - A future React UI has a bug
    - A dev endpoints exists

The API must reject invalid transitions and invariant violations

There must be no "UI-only rules"

---

## Sanity Checks

- Can the frontend create a second ACTIVE Daily Win? -> No

- Can invalid Task transitions succeed if UI is bypassed? -> No

- Does the database enforce uniqueness of DailyWin data? -> Yes

- Does the state machine live server-side? -> Yes

- Is the frontend considered authoritative? -> No

---