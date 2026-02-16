Phase 7 - Reliability & Housekeeping

**Goal:**  
Ensure the system behaves predictably over time, survives edge cases, and doesn’t silently rot.

This phase is about operational stability, not features.

**Non-goals (Phase 7):**

- No new productivity features
    
- No UI redesign
    
- No analytics expansion
    
- No scaling for thousands of users
    
- No premature optimization
    

---

## 7.1 — Define Day Boundary Behavior

**Objective:** Decide what happens at midnight.

Questions to answer:

- If Daily Win is still ACTIVE at 12:00 AM, what happens?
    
    - Auto-carry forward?
        
    - Auto-pause with note “Carried over”?
        
    - Freeze as yesterday’s unresolved?
        
- What if a Daily Win is selected after midnight for the previous day?
    
- Is “today” always based on server time?
    

**Definition of Done**

- You have a single documented policy for midnight rollover
    
- There is no ambiguity about what “today” means
    

---

## 7.2 — Data Integrity Guardrails

**Objective:** Prevent silent corruption over months of use.

Define:

- Tasks cannot exist without valid status
    
- DailyWin must always reference an existing Task
    
- Completed DailyWin must have `completed_at`
    
- Paused/Blocked DailyWin must have note
    

Decide:

- DB-level constraint vs application-level enforcement
    

**Definition of Done**

- You can list 5 invariants that must always be true in the database
    

---

## 7.3 — Backlog Entropy Control

**Objective:** Prevent backlog from becoming a graveyard.

Decide:

- Will ABANDONED tasks exist?
    
- Should tasks auto-surface if untouched for X days?
    
- Should there be a “Backlog Review” indicator?
    

Keep v1 simple.

**Definition of Done**

- You’ve chosen a backlog decay philosophy (ignore, prune, or review)
    

---

## 7.4 — Blocked Task Resolution Loop

**Objective:** Ensure BLOCKED tasks don’t stay invisible forever.

Define:

- Are blocked tasks included in suggestions? (likely no)
    
- Is there a visual indicator on Backlog page for blocked tasks?
    
- Does the board ever surface blocked notes?
    

**Definition of Done**

- Blocked tasks have a clear lifecycle and visibility plan
    

---

## 7.5 — Data Backup Strategy (Minimal but Real)

**Objective:** Protect against data loss.

Decide:

- Is the SQLite file backed up?
    
    - Manual copy weekly?
        
    - Scheduled task?
        
- Where is it stored?
    
- What is the recovery process?
    

Keep it simple.

**Definition of Done**

- You can restore the DB file from backup in one documented step
    

---

## 7.6 — Startup & Recovery Behavior

**Objective:** Define what happens when the app restarts.

Define:

- Does it auto-create DB if missing?
    
- What happens if DB is corrupted?
    
- What happens if no users exist?
    
- What happens if no tasks exist?
    

**Definition of Done**

- You’ve documented expected startup behavior for 3 failure cases
    

---

## 7.7 — Dev vs Production Mode Separation

**Objective:** Prevent dev shortcuts from leaking into real usage.

Define:

- Are `/api/dev/*` routes disabled in production?
    
- Is debug logging different?
    
- Is auto-seeding disabled outside local dev?
    

**Definition of Done**

- You have a rule: “Production mode must not expose dev endpoints.”
    

---

## 7.8 — Logging Policy

**Objective:** Make debugging possible without noise.

Define:

- Log level defaults (INFO in production)
    
- What events should log?
    
    - DailyWin selection
        
    - Resolution
        
    - Invalid transition attempts
        
- Avoid logging sensitive content
    

**Definition of Done**

- You have a minimal logging policy written
    

---

## 7.9 — Performance Boundaries (For Household Scale)

**Objective:** Prevent overengineering.

Define:

- Expected scale: < 500 tasks total
    
- Expected users: 3–5
    
- Expected daily usage: minimal concurrent traffic
    

Decision:

- No caching layer
    
- No async DB complexity required
    

**Definition of Done**

- You’ve documented expected scale and confirmed architecture is sufficient
    

---

## 7.10 — Reliability Validation Checklist

**Objective:** Define “stable enough to live with.”

Checklist:

- App survives restart without losing state
    
- Midnight rollover behaves as defined
    
- Corrupt transitions are rejected
    
- Suggestions don’t crash when backlog is empty
    
- Board handles API downtime gracefully
    
- DB file backup exists
    
- No dev endpoints visible in production mode
    

**Definition of Done**

- You can run through checklist without patching logic mid-test
    

---

# Phase 7 Definition of Done

Phase 7 is complete when:

- Day boundary behavior is defined
    
- Integrity invariants are documented
    
- Backup plan exists
    
- Dev/production separation exists
    
- Logging policy exists
    
- Stability checklist exists
    

At this point, you have something you could mount on a wall and rely on.