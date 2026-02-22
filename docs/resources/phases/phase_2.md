Phase 2 - Core Business Logic

**Goal:**  
Define and enforce the household rules that make this system different from a to-do app.

**Non-goals (Phase 2):**

- No UI work (board/app pages come later)
    
- No “nice to have” metrics/suggestions
    
- No deployment concerns
    
- No auth/permissions
    

---

## 2.1 — Lock the Vocabulary of State

**Objective:** Ensure everyone (and the system) uses the same language.

**Outputs**

- Final list of task states (TaskStatus)
    
- Final list of daily win states (DailyWinStatus)
    
- Clear definitions for each state in plain English
    

**Definition of Done**

- Each status has a one-sentence meaning
    
- No overlapping meanings (“Paused” vs “Blocked” is unambiguous)
    

---

## 2.2 — Define the Task State Machine

**Objective:** Create the allowed transitions so “task hopping” becomes visible and controlled.

**Outputs**

- A transition table (from → to) for TaskStatus
    
- Rules for transitions that require a note/reason
    

**Definition of Done**

- You can point at any state and say what states it can move to next
    
- Invalid transitions are explicitly listed as disallowed (not left implied)
    

---

## 2.3 — Define the Daily Win Invariant

**Objective:** Specify the rule that creates momentum.

**Outputs**

- Rule: Exactly one Daily Win can be ACTIVE per calendar day
    
- Rule: A Daily Win cannot be replaced unless resolved
    

**Definition of Done**

- You have written the invariant in a single sentence
    
- You have a clear “what counts as resolved” definition
    

---

## 2.4 — Define “Resolution” Rules

**Objective:** Decide what it means to “clear” the Daily Win slot.

**Outputs**

- Resolved states: DONE
    
- Unresolved state: ACTIVE
    

**Definition of Done**

- You can answer: “Can we pick a new Daily Win if the current is PAUSED?” (Yes, because resolved-with-context)
    
- Notes requirement is documented (what counts as an acceptable note)
    

---

## 2.5 — Define “Definition of Done” Enforcement

**Objective:** Kill vague tasks at the source.

**Outputs**

- Rule: A task cannot be created/activated without a Definition of Done
    
- Optional: Minimum quality rule (e.g., not blank, not “done”)
    

**Definition of Done**

- You can decide whether Definition of Done is required at creation only, or also required before activation (recommendation for later; planning only here)
    

---

## 2.6 — Define Ownership + Responsibility Rules

**Objective:** Remove ambiguity (“I thought you were doing it”).

**Outputs**

- Rule: Daily Win must have an owner (or explicitly Shared)
    
- Rule: Tasks can exist unassigned in backlog, but Daily Win cannot be unassigned
    

**Definition of Done**

- Ownership rules are written clearly enough that a stranger could follow them
    

---

## 2.7 — Define “Switching” Behavior (Anti-Task-Hop Mechanism)

**Objective:** Make task switching intentional instead of impulsive.

**Outputs**

- Rule: You cannot activate a new Daily Win while today’s is ACTIVE
    
- If switching is allowed by resolving current, require explicit choice: PAUSED or BLOCKED with note, or DONE
    
- Optional: Track switch count per day (planning only; likely Phase 5+)
    

**Definition of Done**

- You have a written “switch procedure” step-by-step in plain language
    

---

## 2.8 — Define Failure/Edge Cases

**Objective:** Prevent the system from breaking when real life happens.

**Outputs**

- What happens at midnight if Daily Win is still ACTIVE?
    
    - Option: auto-carry forward
        
    - Option: auto-pause with note “carried over”
        
    - Option: leave as yesterday’s unresolved (usually bad)
        
- What happens if someone selects a Daily Win late at night?
    
- What happens if DB has no tasks?
    

**Definition of Done**

- You’ve chosen an approach for each edge case and documented it
    

---

## 2.9 — Define the “Source of Truth” Placement

**Objective:** Ensure rules live in the right place so React later can’t bypass them.

**Outputs**

- Rule: State enforcement happens server-side (not in UI)
    
- UI is only a client of the rules
    

**Definition of Done**

- Written as a principle: “Frontend can’t override invariants.”
    

---

## 2.10 — Create the Phase 2 Test Matrix (Planning Only)

**Objective:** Define what must be provably true before moving on.

**Outputs**  
A checklist of scenarios the system must handle, such as:

- Create task with missing Definition of Done → reject
    
- Activate Daily Win when one is already ACTIVE → reject
    
- Pause Daily Win without note → reject
    
- Block Daily Win with note → accept, allow new selection
    
- Mark Daily Win done → sets completion state cleanly
    

**Definition of Done**

- You have at least 10 scenario checks written
    
- Each scenario is phrased as “Given / When / Then”
    

---

# Phase 2 Definition of Done

You are done with Phase 2 when:

- core_domain_rules exists as a directory under docs/resources

- core_domain rules contains a task_state_machine.md file

- core_domain_rules contains a locked_vocabulary.md file
    
- core_domain_rules contains a daily_win_invariant.md file
    
- core_domain_rules contains a resolution_rules.md file
    
- core_domain_rules contains a edge_cases.md file

- docs/resources/test_matrices exists as a directory
    
- docs/resources/test_matrices contains a phase_2_test_matrix.md file
    
- Ownership + Definition of Done rules are explicit
    

No UI, no DB details beyond what’s needed to describe rules—just the behavioral contract.