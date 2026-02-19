# Task State Machine

| From      | Allowed To                         | Notes                                                                            |
| --------- | ---------------------------------- | -------------------------------------------------------------------------------- |
| BACKLOG   | ACTIVE, PAUSED, BLOCKED, ABANDONED | Allow PAUSED/BLOCKED if you want “pre-marking context” (optional but practical). |
| ACTIVE    | DONE, PAUSED, BLOCKED              | PAUSED/BLOCKED require note.                                                     |
| PAUSED    | BACKLOG, ACTIVE, ABANDONED         | “Backlog” means eligible again.                                                  |
| BLOCKED   | BACKLOG, ACTIVE, ABANDONED         | “Backlog” means constraint cleared / ready to retry.                             |
| DONE      | *(none)*                           | Terminal.                                                                        |
| ABANDONED | *(none)*                           | Terminal.                                                                        |

---

## Why Allow BACKLOG -> PAUSED/BLOCKED
Sometimes you know a task is blocked before you ever start it ("Need to buy caulk first"). This prevents you from activating it just to block it.

---

## Transitions That Require A Note
A note is required when the destination is:
= PAUSED
- BLOCKED
This applies regardless of source state.

Minimum note quality (v1):
- non-empty after trimming whitespace

---

## Explicity Disallowed Transitions:
- Terminal State Rules
    - BACKLOG -> DONE
    - ABANDONED -> anything

- No 'teleporting' to DONE
    - BACKLOG -> DONE
    - PAUSED -> DONE
    - BLOCKED -> DONE

- No 'reviving' finished work
    - DONE -> ABANDONED/ACTIVE/PAUSED/BLOCKED/ABANDONED
    - ABANDONED -> BACKLOG/ACTIVE/PAUSE/BLOCKED/DONE
    (If task has been abandoned, the only way to reintroduce is to recreate the task)

- No returning to BACKLOG once ACTIVE
    - ACTIVE -> BACKLOG
    (from ACTIVE, you must choose either PAUSED/BLOCKED/DONE)

---

## Plain-English Transition Intent
- BACKLOG -> ACTIVE: We are starting work now

- ACTIVE -> DONE: DoD satisfied; Task Complete

- ACTIVE -> PAUSED: We chose to stop; we will resume later

- ACTIVE -> BLOCKED: We cannot proceed; waiting on something.

- PAUSED/BLOCKED -> BACKLOG: It's eligible again but not being worked now;

- PAUSED/BLOCKED -> ACTIVE: We are resuming work now.

- PAUSED/BLOCKED/BACKLOG -> ABANDONED: We are retiring this task permanently

---

## Definition of Done Check
A) Completeness

Every TaskStatus has an explicit list of allowed “next” statuses.

Terminal states (DONE, ABANDONED) are explicitly terminal.

B) No overlaps / no ambiguity

PAUSED vs BLOCKED distinction is written in one sentence each.

“Backlog” meaning is defined (eligible again, not being worked).

C) Disallowed transitions are explicit

Invalid transitions are listed (not implied).

“Teleporting to DONE” is explicitly forbidden.

D) Note requirements are explicit

Any transition into PAUSED requires a note.

Any transition into BLOCKED requires a note.

Minimum note quality rule is stated (non-empty after trimming).

E) Quick sanity questions (answerable from the doc)

Can a PAUSED task go straight to DONE? No.

Can an ACTIVE task go to BACKLOG? No (by design).

Can a BACKLOG task be marked BLOCKED before it’s started? Yes (if you keep that transition).

Can DONE ever be re-opened? No.

Can ABANDONED ever be revived? No.