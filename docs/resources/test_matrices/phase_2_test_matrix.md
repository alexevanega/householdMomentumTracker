# Phase 2 Test Matrix

Purpose: These scenarios define what must be true for the Phase 2 rules to be considered complete and internally consistent. They are not executable tests yet; They are behavioral examples that can later be automated.

---

## Task Creation + Definition of Done Enforcement

### Scenario A1 - Reject task creation with missing DoD

Given a create-task request with definition_of_done missing or blank
When the task is created
Then the system rejects the request
And no task record is created

### Scenario A2 - Reject task creation with placeholder DoD

Given a create-task request where definition_of_done is a known placeholder (e.g. "done","tbd")
When the task is created
Then the system rejects the request

### Scenario A3 - Reject activation of a task missing DoD

Given an existing task with an empty/invalid definition_of_done (created via dev/import/manual corruption)
When attempting to transition it to ACTIVE
Then the system rejects the transition

---

## Task State Machine - Valid Transitions

### Scenario B1 - BACKLOG -> ACTIVE allowed

Given a task in BACKLOG
When transitioning to ACTIVE
Then the transition succeeds

### Scenario B2 - ACTIVE -> DONE allowed

Given a task in ACTIVE
When transitioning to DONE
Then the transition suceeds
And the task is terminal

### Scenario B3 - ACTIVE -> PAUSED allowed with note

Given a task in ACTIVE
When transitioning to PAUSED with a non-empty note
Then the transition succeeds

### Scenario B4 - ACTIVE -> BLOCKED allowed with note

Given a task in ACTIVE
When transitioning to BLOCKED with a non-empty note
Then the transition succeeds

### Scenario B5 - PAUSED -> ACTIVE allowed

Given a task in PAUSED
When transitioning to ACTIVE
Then the transition succeeds

### Scenario B6 - BLOCKED -> BACKLOG allowed

Given a task in BLOCKED
When transitioning to BACKLOG
Then the transition succeeds

### Scenario B7 - BACKLOG -> BLOCKED allowed (if enabled by table)

Given a task in BACKLOG
When transitioning to BLOCKED with a non-empty note
Then the transition succeeds

---

## Task State Machine - Invalid/Disallowed Transitions

### Scenario C1 - Reject BACKLOG -> DONE

Given a task in BACKLOG
When attempting to transition to DONE
Then the system rejects the transition

### Scenario C2 - Reject PAUSED -> DONE

Given a task in PAUSED
When attempting to transition to DONE
Then the system rejects the transition

### Scenario C3 - Reject BLOCKED -> DONE

Given a task in BLOCKED
When attempting to transition to DONE
Then the system rejects the transition

### Scenario C4 - Reject ACTIVE -> BACKLOG 

Given a task in ACTIVE
When attempting to transition to BACKLOG
Then the system rejects the transition

### Scenario C5 - DONE is terminal

Given a task in DONE
When attempting any transition to another state
Then the system rejects the transition

### Scenario C6 - ABANDONED is terminal

Given a task in ABANDONED
When attempting any transition to another state
Then the system rejects the transition

---

## Note Requirements (Task Transition)

### Scenario D1 - Reject PAUSED without note

Given a task in ACTIVE
When transitioning to PAUSED with no note or blank note
Then the system rejects the transition

### Scenario D2 - Reject BLOCKED without note

Given a task in ACTIVE
When transitioning to BLOCKED with no note or blank note
Then the system rejects the transition

---

## Daily Win Invariant - Selection

### Scenario E1 - Select Daily Win when none exists today

Given there is no Daily Win record for today
And there exists an eligible task
When selecting a task as today's Daily Win
Then a Daily Win record is created with status ACTIVE
And the selected task becomes ACTIVE

### Scenario E2 - Reject selecting a new Daily Win when today is ACTIVE

Given today's Daily Win exists and is ACTIVE
When attempting to select another Daily Win for today
Then the system rejects the selection

### Scenario E3 - Reject selecting a new Daily Win after DONE

Given today's Daily Win exists and is DONE
When selecting another Daily Win for today
Then the system rejects the selction

---

## Daily Win Resolution Rules

### Scenario F1 - Resolve Daily Win as DONE

Given today's Daily Win is ACTIVE
When resolving it as DONE
Then today's Daily Win becomes DONE
And completed_at is set
And the linked task becomes DONE

### Scenario F2 - Reject DONE resolution without completed_at

Given today's Daily Win is ACTIVE
When resolving it as DONE without setting completed_at
Then the system rejects the resolution

### Scenario F3 - Resolve Daily Win as PAUSED with note

Given today's Daily Win is ACTIVE
When resolving it as PAUSED with a non-empty note
Then today's Daily Win becomes PAUSED
And the linked task becomes PAUSED

### Scenario F4 - Reject PAUSED resolution without note

Given today's Daily Win is ACTIVE
When resolving it as PAUSED with no note or blank note
Then the system rejects the resolution

### Scenario F5 - Resolve Daily Win as BLOCKED with note

Given today's Daily Win is ACTIVE
When resolving it as BLOCKED with a non-empty note
Then today's Daily Win becomes BLOCKED
And the linked task becomes BLOCKED

### Scenario F6 - Reject BLOCKED resolution without note

Given today's Daily Win is ACTIVE
When resolving it as BLOCKED with note note or blank note
Then the system rejects the resolution

---

## Ownership Rules

### Scenario G1 - Daily Win must have owner or Shared

Given a selection attempt for today's Daily Win
When the selection occurs
Then the resulting Daily Win has an owner or is explicitly shared

### Scenario G2 - Auto-assign owner

Given a task with no owner
And a user selects it as Daily Win
When selection occurs
Then the task owner becomes the selecting user
And the Daily Win owner is the selecting user

### Scenario G3 - Reject ownership change while ACTIVE

Given a task is ACTIVE as today's Daily Win
When attempting to change its owner
Then the system rejects the change

---

## Switching Behavior

### Scenario H1 - Reject switching Daily Win ACTIVE

Given today's Daily Win is ACTIVE
When attempting to select a different task as today's Daily Win
Then the system rejects the attempt

### Scenario H2 - Require explicit resolution before switching

Given today's Daily Win is ACTIVE
When user wants a different task
Then user must resolve current as PAUSED/BLOCKED
And current Daily Win will be vacated
And only after resolution may a new selection occur

---

## Edge Cases

### Scenario I1 - Midnight rollover auto-pause

Given today's Daily Win is ACTIVE at 23:59
When the system crosses into the next calendar day
Then yesterday's Daily Win becomes PAUSED
And an auto-note is recorded
And the linked task becomes PAUSED

## Scenario I2 - Define "today" using server-local date

Given the server time is used for date boundaries
When clients in different timezones interact
Then "today" is consistent according to server-local date

### Scenario I3 - No eligible tasks exist

Given there are no eligible tasks
When attempting to select a Daily Win
Then the system rejects with a clear message

### Scenario I4 - Corruption Guard: multipke DailyWins for same date

Given the database contains more than one DailyWin record for the same date
When any Daily Win is attempted
Then the system fails loudly and logs integrity error
 
---