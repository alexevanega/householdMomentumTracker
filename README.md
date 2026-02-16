# Household Momentum Tracker

The Household Momentum Tracker is a household momentume system designed to enforce clarity and intentional focus by limiting each day to exactly one controlled "Daily Win".

This is not a productivity app.
It is a behavioral constraint system built around enforceable state transistions and visible daily commitment

---

## Core Invariant

> Exactly one Daily Win per calendar day.

- Only one Daily Win may be ACTIVE at a time.
- A new Daily Win cannot be selected unless the current one is resolved.
- Resolution requires:
    - DONE
    - PAUSED (with note)
    - BLOCKED (with note)

All rules are enforced server-side.

---

## Development Model

This project follows **Milestone-Based Incremental Architecture (MBIA)**.

Phases are:
- Sequential
- Gated by formal sign-off
- verified through documented acceptance checks and audit review

This project is new and in progress. README will be updated as new features are added.

To review the current phase list, access docs/resources/phase_list.md.

Each phase has an individual document. Those docs can be found in docs/resources/phases/phase_x.md (replace x with phase number).

See:
docs/governance/development_model.md

---

## Local Development

Activate the virtual environment:

# Windows
.trackerENV\Scripts\activate

# macOS / Linux
source .trackerENV/bin/activate

Run the app:

uvicorn app.main:app --reload


Health endpoint:

GET /api/health


## Project Structure
/app — application code
/docs — governance + architecture
/docs/resources — reusable templates and phase documentation
/docs/phase_signoffs — signed phase reviews

## Philosophy
- Server-side authority
- Explicit state machine enforcement
- Minimal UI complexity
- Visibility drives behavior
- No feature creep without behavioral justification

---