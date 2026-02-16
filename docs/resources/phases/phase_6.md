Phase 6 - Suggestions Engine

**Goal:**  
Plan a lightweight “decision friction reducer” that helps the household choose a Daily Win without turning this into a productivity app.

This phase exists for one reason:  
When people are tired, the hardest part is _picking_ the next thing.

**Non-goals (Phase 6):**

- No machine learning
    
- No complex personalization
    
- No “optimization” dashboards
    
- No nagging notifications
    
- No long ranked lists
    

---

## 6.1 — Define the Suggestions Engine’s Job (Scope Fence)

**Objective:** Keep it simple and aligned with the Momentum Board philosophy.

**Outputs**

- One-sentence mission: “Offer a short list of reasonable Daily Win candidates.”
    
- Explicit exclusions:
    
    - no points
        
    - no streak pressure
        
    - no guilt messaging
        
    - no infinite recommendations
        

**Definition of Done**

- You can explain in one sentence what suggestions are for, and what they’re not for
    

---

## 6.2 — Define Eligibility Rules (What Can Be Suggested)

**Objective:** Prevent bad candidates from showing up.

**Outputs**  
Eligibility rules for suggestions (v1):

- Task must have Definition of Done (already required)
    
- Task status must be eligible (choose set):
    
    - BACKLOG
        
    - PAUSED (optionally)
        
    - BLOCKED (usually excluded unless “blocked reason resolved” is a thing)
        
- Task should not be ABANDONED or DONE
    
- Optional: exclude tasks marked “sensitive/private” (future)
    

**Definition of Done**

- A clear list exists: eligible statuses and ineligible statuses
    

---

## 6.3 — Define Suggestion Output Size + Presentation

**Objective:** Keep choice small.

**Outputs**

- Suggest exactly **3** candidates (default)
    
- If fewer than 3 exist, show what exists + a message “Add tasks to backlog”
    
- Presentation location:
    
    - Today page (when no Daily Win selected)
        
    - Board “No win selected” state (optional)
        

**Definition of Done**

- Output size is fixed and small
    
- You’ve documented where suggestions appear
    

---

## 6.4 — Define the Selection Strategy (How Suggestions Are Picked)

**Objective:** Choose a simple, explainable approach.

**Outputs**  
Pick one approach for v1 (document it):

- **Effort-first**: prefer TINY then SMALL then MEDIUM
    
- **Domain rotation**: avoid showing 3 tasks from same domain if possible
    
- **Staleness**: prefer tasks not updated/selected recently
    
- **Owner-aware** (optional): prefer tasks owned by the person likely to do it
    

**Definition of Done**

- The v1 strategy is written as simple if/then rules, not “magic”
    

---

## 6.5 — Define “Anti-Repetition” Behavior

**Objective:** Avoid suggesting the same thing every day.

**Outputs**  
Choose one minimal method:

- exclude tasks completed in last X days
    
- exclude tasks suggested yesterday (requires storing suggestions history)
    
- random sampling from eligible tasks (with effort weighting)
    

**Definition of Done**

- A basic anti-repetition rule is documented
    

---

## 6.6 — Define “Effort” as the Core Energy Proxy

**Objective:** Support burnout reality without implementing full “energy tracking.”

**Outputs**

- Effort tiers meaning in plain language:
    
    - TINY: 5–10 minutes, minimal friction
        
    - SMALL: 10–30 minutes, some friction
        
    - MEDIUM: 30–90 minutes, requires focus
        
- Rule: suggestions default to TINY/SMALL unless user explicitly requests more
    

**Definition of Done**

- Effort categories have time/feel definitions that match household reality
    

---

## 6.7 — Optional: Define “Friction Tags” (Planning Only)

**Objective:** Capture why tasks feel heavy even when small.

**Outputs**  
A short list of optional tags (not required for v1 implementation):

- requires leaving house
    
- requires phone call
    
- requires social interaction
    
- loud/dirty
    
- time-sensitive
    

**Definition of Done**

- Tags are defined as optional metadata, not mandatory complexity
    

---

## 6.8 — Define User Controls (How Humans Override Suggestions)

**Objective:** Ensure suggestions never become “the boss.”

**Outputs**

- User can always choose any eligible task manually
    
- Suggestions are recommendations, not requirements
    
- Provide “refresh suggestions” button or link (optional)
    

**Definition of Done**

- Human override is explicitly documented
    

---

## 6.9 — Define Failure States

**Objective:** Make the system robust when backlog is empty or messy.

**Outputs**

- If no eligible tasks:
    
    - show message: “No eligible tasks. Add one in Backlog.”
        
    - optionally show quick-add box
        
- If many tasks are BLOCKED:
    
    - show message: “Most tasks are blocked—review blocked notes”
        

**Definition of Done**

- You’ve documented what to display when suggestions can’t be generated
    

---

## 6.10 — Suggestions Validation Checklist (Planning Only)

**Objective:** Define “done” for the suggestions engine.

**Outputs**  
Checklist:

- Suggestions appear when no Daily Win selected
    
- Exactly 3 candidates shown (or fewer if not enough)
    
- Suggestions never include DONE/ABANDONED
    
- Suggestions heavily favor TINY/SMALL by default
    
- Suggestions do not repeat the same exact set every day (per your chosen anti-repeat rule)
    
- Suggestions are explainable (user can understand why they were shown)
    

**Definition of Done**

- A checklist exists that prevents the engine from turning into “magic”
    

---

# Phase 6 Definition of Done

Phase 6 is complete when:

- Eligibility rules are defined
    
- Selection strategy is defined
    
- Anti-repetition behavior is defined
    
- Effort semantics are defined
    
- Output size and placement are defined
    
- Validation checklist exists