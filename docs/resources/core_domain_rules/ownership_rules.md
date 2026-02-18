# Ownership & Responsibility Rules

Purpose: Eliminate ambiguity about who is responisble for the Daily Win

Backlog can be loose
DailyWin cannot

---

## Task Ownership (Backlog level)
- A Task may exist without an owner
- Onwer is optional in BACKLOG
- Owner may be assigned or changed while task is NOT ACTIVE

Owner is informational at backlog stage

---

## Daily Win Ownership Rule (Hard Rule)
    A Daily Win must have an owner OR be explicitly marked as Shared.

A Daily Win cannot be unassigned

This Prevents:
    - "floating responsibility"
    - "silent diffusion of accountability"

---

## Owner Determination at Selction Time

You must choose one of these policies and document it clearly

If the Task has no owner:
    - The selecting user becomes the owner automatically.

If the Task has an owner:
    - Ownership remains unchanged

Later Option:

At selction:
    - User must confirm or change owner.
    - No implicit assignment

---

## Shared Ownership Policy
If you allow Shared:
    Represent as:
        - "owner = null" + "shared=true"
                OR
        - special "Share" user

Shared means: 

    - Responsibility is joint.
    - Both parties accept accountability

No silent "unowned" tasks

---

## Ownership During ACTIVE State
While a Task is ACTIVE (as Daily Win):

    - Owner cannot be changed mid-day
    - Ownership change requires:
        - Resolve current Daily Win (PAUSED/BLOCKED/DONE)
        - Then modify ownership before next activation
This prevents mid-day responisibility drify.

---

## Ownership Effects on Resolution
- If DONE -> Owner is credited
- If PAUSED/BLOCKED -> note must reflect owner's reasoning
- Owner field is stored in DailyWin record for historical trace

DailyWin must snapshot the owner at time of selection

Even if Task owner changes later.

---

## Sanity Checks

- Can a Daily Win exist without an owner? -> No

- Can backlog tasks exist without an owner? -> Yes

- Does selecting a Daily Win guarantee ownership? -> Yes

- Can ownership cange while ACTIVE? -> No

- Is ownership preserved in history? -> Yes

---