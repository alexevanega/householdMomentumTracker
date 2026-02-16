Phase 4 - Wall Board UI

**Goal:**  
Design the always-on, hard-to-ignore wall display that shows the household’s current “Daily Win” state and momentum at a glance.

**Non-goals (Phase 4):**

- No full backlog management UI (that’s Phase 5)
    
- No complex interaction patterns
    
- No authentication
    
- No deep analytics
    
- No notification system
    

---

## 4.1 — Define the Board’s Job (Behavioral Contract)

**Objective:** Make the board’s purpose explicit so it doesn’t become a clutter screen.

**Outputs**

- One-sentence mission: “Display today’s Daily Win and its state with zero effort.”
    
- What the board will _never_ show by default:
    
    - full backlog list
        
    - long scrollable content
        
    - configuration/settings
        
- What it must always show:
    
    - today’s win (or “none selected”)
        
    - current status
        
    - owner
        
    - definition of done
        
    - materials needed (if any)
        
    - momentum indicators (streak/weekly)
        

**Definition of Done**

- You can explain what the board is for in 10 seconds
    
- You can list what it intentionally hides
    

---

## 4.2 — Define the Information Hierarchy (What’s Biggest)

**Objective:** Decide what visually dominates.

**Outputs**

- “Primary block” content (largest):
    
    - TODAY’S HOUSEHOLD WIN
        
    - task title
        
- “Secondary block” content (medium):
    
    - owner
        
    - status badge
        
    - definition of done
        
- “Tertiary block” content (small):
    
    - materials needed
        
    - streak
        
    - weekly wins
        

**Definition of Done**

- A clear ranked list: primary / secondary / tertiary
    

---

## 4.3 — Define Board States (Empty vs Active vs Resolved)

**Objective:** Plan what the board shows in each situation.

**Outputs**  
Board display states:

1. **No Daily Win selected**
    
    - shows “No Daily Win selected”
        
    - shows 1–3 suggested next actions (optional, could be Phase 6)
        
    - shows CTA: “Select one at /app”
        
2. **Daily Win ACTIVE**
    
    - shows all task details prominently
        
3. **Daily Win PAUSED/BLOCKED**
    
    - shows status + note prominently
        
    - shows “Next step: resolve or pick a new win”
        
4. **Daily Win DONE**
    
    - shows “Completed” banner
        
    - shows today’s completed win + timestamp
        
    - optionally shows “Pick tomorrow’s” message (later)
        

**Definition of Done**

- Each board state has a defined layout intent and message
    

---

## 4.4 — Define Update Strategy (How It Stays Fresh)

**Objective:** Make it reliable on a wall display.

**Outputs**

- Refresh method: polling every 15–30 seconds (v1)
    
- What happens on API failure:
    
    - display “connection issue” banner
        
    - keep showing last known state
        
- Time handling:
    
    - local timezone assumption
        
    - what counts as “today” is consistent
        

**Definition of Done**

- You have a documented refresh policy and failure behavior
    

---

## 4.5 — Define Interaction Policy (Read-First vs Touch-Enabled)

**Objective:** Prevent accidental complexity.

**Outputs**  
Two allowed modes (choose one for v1 planning):

- **Display-only board**
    
    - all actions happen in web editor
        
- **Light-touch board**
    
    - only 3 actions max:
        
        - Mark Done
            
        - Mark Paused (requires note prompt)
            
        - Mark Blocked (requires note prompt)
            

**Definition of Done**

- You’ve decided whether the board is display-only or light-touch
    
- If light-touch, you have a strict list of allowed actions
    

---

## 4.6 — Define Layout Constraints for TV/Monitor Use

**Objective:** Make it readable from a distance.

**Outputs**

- Typography rules:
    
    - large title size
        
    - high contrast
        
    - minimal text density
        
- Spacing rules:
    
    - big margins
        
    - avoid multi-column clutter unless necessary
        
- Kiosk behavior:
    
    - full screen friendly
        
    - no scroll required
        
- Color semantics (conceptual):
    
    - ACTIVE = neutral/steady
        
    - BLOCKED = attention color
        
    - PAUSED = softer attention
        
    - DONE = positive
        

**Definition of Done**

- You’ve written “distance readability rules” that the UI must obey
    

---

## 4.7 — Define Board Data Inputs (Which API Calls It Uses)

**Objective:** Ensure the board is purely a consumer of Phase 3.

**Outputs**

- Board requires:
    
    - Today’s Daily Win endpoint
        
    - Metrics endpoints (streak/weekly)
        
- Optional:
    
    - “last updated” timestamp
        

**Definition of Done**

- A list of required endpoints for the board to function exists
    

---

## 4.8 — Define “Minimal Backlog Visibility” (If Any)

**Objective:** Prevent the board from becoming overwhelming.

**Outputs**  
Allowed backlog exposure options (choose one):

- Show only “Backlog count: N”
    
- Show top 1–3 “Tiny tasks” (optional; might be Phase 6)
    
- Show nothing backlog-related
    

**Definition of Done**

- Backlog exposure is explicitly chosen and limited
    

---

## 4.9 — Define Security/Privacy for Household Display

**Objective:** Avoid accidental oversharing.

**Outputs**

- Decide what task details are safe to display publicly in the home:
    
    - bills/medical tasks might be sensitive
        
- Optional rule:
    
    - “private” flag on tasks (future phase)
        
- v1 policy:
    
    - avoid sensitive text on the board or keep tasks generic
        

**Definition of Done**

- You have a simple privacy guideline for what can go on the wall
    

---

## 4.10 — Board Validation Checklist (Planning Only)

**Objective:** Define what “board done” means before building the editor.

**Outputs**  
Checklist:

- Displays correctly when no win selected
    
- Displays ACTIVE win clearly
    
- Displays BLOCKED/PAUSED note clearly
    
- Updates within refresh window
    
- Handles API downtime gracefully
    
- Readable from across the room
    
- Does not require scrolling
    
- Does not show backlog clutter
    

**Definition of Done**

- You can validate the board visually and functionally with a simple checklist
    

---

# Phase 4 Definition of Done

Phase 4 is complete when:

- Board purpose and hierarchy are locked
    
- Board states are defined
    
- Update policy is defined
    
- Interaction policy is defined
    
- Data inputs and minimal backlog exposure are defined
    
- A validation checklist exists