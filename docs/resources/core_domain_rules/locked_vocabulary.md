# Locked Vocabulary

## TaskStatus (v1)
- BACKLOG - The task exists, is eligible to be chosen, but is not being worked right now.

- ACTIVE - The task is the current focus item being worked (typically today's Daily Win)

- PAUSED - Work in intentionally stopped for now, and a reason/context is recorded

- BLOCKED - Work cannot continue due to an external constraint (materials, dependency, waiting on someone/something), and a reason/context is recorded

- DONE - The task's Definition of Done has been met

- ABANDONED - The task is intentionally retired and should not be suggested or selected again

### No Overlap Rule (important):
- PAUSED = voluntary stop (you chose to stop)
- BLOCKED = forced stop (you cannot proceed)

---

## DailyWinStatus (v1)
- ACTIVE - The Daily Win for that calendar day is selected and not yet resolved

- DONE - The Daily Win was completed for that day

- PAUSED - The Daily Win was intentionally stopped that day with a note explaining why

- BLOCKED - The Daily Win could not be completed that day due to a constraint, with a note explaining what it is

### DailyWinStatus deliberately does NOT include:
- BACKLOG (Daily Win isn't 'pending', it is either chosen or not)

- ABANDONED (Daily Win is a daily record; Abandonment is a task concept)

---

## Plain-English Glossary Rules (to prevent future argument)
- A task can be PAUSED even if it could be done - you're choosing not to do it right now

- A task is BLOCKED only if something outside your control prevents progress

- A task is ACTIVE only when it is the one you are currently executing as the primary focus (and in this system, that's usually the Daily Win)

---

## Definition of Done Vocabulary
- Definition of Done (DoD) - A concrete description of what must be true for this task to be considered DONE

---
