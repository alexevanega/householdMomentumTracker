# Definition of Done Enforcment

    Purpose: Prevent vague tasks from entering the system and poisioning momentum.

    A task without a real definiton of done is not a task - it is a worry.

---

## Core Rule
    A task cannot be created without a Definition of Done
This is enforced server-side

---

## Activation Rule
    A task cannot become ACTIVE unless it has a valid Definition of Done.
This matters even if someone bypasses creation rules later (imports, dev endpoints, manual edits, etc.)

---

## Minimum Quality Rules (v1)
A Definition of Done is considered valid only if:
    - It is non-empty after trimming whitespace
    - It is not a known placeholder

### Placeholder Rejection List (v1)
Reject if DoD (case-sensitive, trimmed) equals:
    - "done"
    - "tbd"
    - "n/a"
    - "na"
    - "idk"
    - "?"

---

## What "Good Enough" looks like
DoD should describe a concrete observable outcome

Good Examples:

- "Kitchen counters wiped, sink empty, trash taken out."
- "Bill paid and confirmation number saved in notes"
- "Groceries put away and fridge is organized"
- "Tires checked: pressure set to spec and no visible damage"

Bad Examples:

- "Clean Kitchen"
- "Fix it"
- "Work on bills"
- "Organize stuff"

---

## Enforcement Timing Decision
For v1, enforce at both moments:

    1. Creation Time (cannot create without DoD)
    2. Activation Time (cannot activate without DoD)

Reason: Catches messy data no matter how it got there

---

## Error Behavior (Contract)
If DoD is missing/invalid:
    - API rejects with 400 code
    - Error message must be human-readable
        - "Definition of Done is required."
        = "Definiton of Done is too vague."

---

## Definition of Done Check 

- You cannot create a task with a blank DoD

- You cannot activate a task with blank/placeholder DoD

- The placeholder list is documented and intentionally well

- The app's error messages explain what to fix, not just "invlid".