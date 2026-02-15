# System Overview - Houselhold Momemtum Tracker

## Project Purpose

The Household Momentum Tracker exists to create visible, enforceable daily momentum within a household by limiting focus to exactly one intentional, state-controlled "Daily Win" per day.

It is not a productivity app.
It is not a task manager.
It is a behavioral constraint system

---

## Core Invariant

> Exactly one Daily Win per calendar day

At any given time:
 - Only one Daily Win may be ACTIVE for a given user and date.
 - A new Daily Win cannot be selected unless the current one is resolved or valid reasoning is given for switching to a new Daily Win.
 - Resolution requires:
    - DONE
    - PAUSED (with note)
    - BLOCKED (with note)

This invariant is enforced server-side.

---

## Architectural Philososphy

### 1. Server-Side Authority

All rules, invariants, and state transitions are enforced in the backend.

The frontend (Jinja now, React later):
- cannot override rules
- cannot bypass state transitions
- cannot create inconsistent system states

The server is the single source of truth.

---

### 2. State Machine Enforcement

Tasks are not free-form checklist items.
They exist in defined states and may only transition according to explicit rules.

State transitions are:
- validated
- intentional
- reject invalid moves

This prevents task hopping and ambiguity.

---

### 3. Visibility Drives Behavior

The wall board exists to make the Daily Win impossible to ignore.

The system optimizes for:
- clarity
- constraint
- momentum

Not:
- analytics dashboards
- gamification
- infinite configuration

---

## High-Level Components

### Backend (FastAPI)
- API endpoints
- Task state machine enforcement
- Daily Win selection logic
- Metrics calculation (streak / weekly wins)
- Database persistence

### Database (SQLite)
- Users
- Tasks
- DailyWin Records
- Historical State Tracking

### Wall Board (Display Layer)
- Fullscreen status display
- Shows:
    - Today's Win
    - Status
    - Deinition of Done
    - Owner
    - Streak / Weekly Wins
- Polls backend for updates

### Web Editor (Control Layer)
- Create/Edit Tasks
- Select Daily Win
- Resolved Daily Win
- View History

---

## Scope Boundaries

This system intentionally excludes:

- Authentication Complexity
- Role-Based Permissions
- Enterprise Scaling
- Complex Analytics
- AI-driven optimization

Features are only added when driven by real household behavior needs.