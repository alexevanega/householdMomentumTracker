Phase 9 - Post-Deployment & Feature Hardening

**Goal:**  
Live with the app for real, identify what actually breaks or annoys the household, and make targeted improvements that increase reliability and usability—without expanding into a “productivity platform.”

This phase is where you convert “it runs” into “it sticks.”

**Non-goals (Phase 9):**

- No React retrofit (later)
    
- No major new modules unless pain forces it
    
- No feature creep driven by curiosity
    
- No complex analytics
    
- No auth unless truly needed
    

---

## 9.1 — Establish a Real Usage Feedback Loop

**Objective:** Capture what’s happening in the house without relying on memory.

**Outputs**

- A “Friction Log” note in Obsidian:
    
    - date
        
    - what went wrong / what felt annoying
        
    - severity (low/med/high)
        
    - frequency (one-off/repeats)
        
- A rule: only issues that repeat get changes
    

**Definition of Done**

- You have a place to record pain points and a rule to avoid one-off overbuilding
    

---

## 9.2 — Prioritize Fixes by Behavioral Impact

**Objective:** Choose changes that increase momentum, not features that look cool.

**Outputs**

- A simple priority rubric:
    
    1. prevents daily use (critical)
        
    2. causes confusion (high)
        
    3. causes annoyance (medium)
        
    4. aesthetic polish (low)
        
- A short “Top 5 fixes” list
    

**Definition of Done**

- You can explain why each chosen fix matters in household behavior terms
    

---

## 9.3 — Usability Hardening on the Wall Board

**Objective:** Make the board resilient and readable under real conditions.

**Outputs**  
Potential improvements (choose only what you need):

- “Last updated” timestamp
    
- Clear offline banner (“Can’t reach server”)
    
- Auto-retry behavior clarity
    
- Stronger status emphasis (Blocked/Paused note visibility)
    
- QR code to editor (if helpful)
    

**Definition of Done**

- Board failure is obvious (not silent)
    
- Board is readable at a distance in the real room lighting
    

---

## 9.4 — Editor Workflow Smoothing

**Objective:** Reduce clicks and confusion in the control panel.

**Outputs**  
Potential improvements:

- Quick-add task from Today page
    
- Better task picker (search + filters remembered)
    
- Inline validation messages (especially DoD and pause/block notes)
    
- Confirmations for destructive actions (abandon/delete if you add it)
    

**Definition of Done**

- Household can operate it without you explaining it each time
    

---

## 9.5 — “Backlog Entropy” Management (Minimal)

**Objective:** Stop the backlog from becoming a swamp.

**Outputs**  
Choose one minimal approach:

- Add “Archive/Abandon” action and hide those by default
    
- Add “Backlog review” indicator (e.g., “15 tasks older than 60 days”)
    
- Add a “Cleanup” view (later), but keep it minimal
    

**Definition of Done**

- Backlog stays navigable after 30+ days of real use
    

---

## 9.6 — Improve Blocking and Dependency Handling (If It’s Real Pain)

**Objective:** Make blocked tasks actionable rather than dead ends.

**Outputs**  
Minimal options:

- Standardize blocked note format (e.g., “Blocked by: [thing]”)
    
- Add “Needs materials” checkbox or field (still not a full inventory)
    
- Add a “Blocked tasks” filter view and a reminder section in editor
    

**Definition of Done**

- Blocked items can be reviewed and unblocked without hunting
    

---

## 9.7 — Recurring Task Strategy (Only If Needed)

**Objective:** Handle repeating household tasks without manual re-entry.

**Outputs**  
Decide:

- Do you need recurring tasks at all?
    
- If yes, choose one minimal method:
    
    - “Create next instance when marked done”
        
    - “Weekly template tasks that can be selected”
        
    - “Recurring generator” (more complex; likely later)
        

**Definition of Done**

- Recurring doesn’t create clutter or duplicates
    
- It actually reduces workload
    

---

## 9.8 — Stability & Safety Improvements

**Objective:** Improve reliability without turning into DevOps.

**Outputs**  
Possible changes:

- Better error logging
    
- Safer DB backup automation
    
- Simple “export data” feature (CSV/JSON)
    
- Database integrity check procedure
    

**Definition of Done**

- If something breaks, you can diagnose quickly
    
- Data loss risk is reduced
    

---

## 9.9 — Performance and Responsiveness Review (Household Scale)

**Objective:** Make sure it stays snappy as tasks accumulate.

**Outputs**

- Decide performance boundaries:
    
    - still fine at 200–500 tasks
        
- Identify any slow views and why (usually filtering/sorting)
    
- Decide whether to add indices (only if needed)
    

**Definition of Done**

- Board loads fast
    
- Editor lists don’t lag noticeably
    

---

## 9.10 — Define “v1 Complete” Criteria

**Objective:** Create a finish line so you don’t tinker forever.

**Outputs**  
A short list such as:

- Board is stable and always visible
    
- Daily Win workflow is used at least X days in a 2-week span
    
- Backlog stays manageable
    
- Your partner can use it without coaching
    
- You can explain the full app architecture from memory
    

**Definition of Done**

- You have a written “v1 complete” definition and you can declare victory
    

---

# Phase 9 Definition of Done

Phase 9 is complete when:

- You have real household feedback documented
    
- You’ve implemented only repeat pain fixes
    
- The board/editor are smooth enough to become habit
    
- You’ve defined and reached “v1 complete”