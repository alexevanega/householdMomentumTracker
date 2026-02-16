Phase 5 - Web Editor UI

**Goal:**  
Plan the web interface that lets the household actually run the system: create tasks, choose today’s Daily Win, resolve it, and review history—without touching the database or code.

**Non-goals (Phase 5):**

- No complex UX polish or animations
    
- No authentication/roles (v1)
    
- No mobile-perfect UI (nice later)
    
- No suggestion engine logic (Phase 6)
    
- No notifications
    

---

## 5.1 — Define the Web Editor’s Job (Scope Fence)

**Objective:** Prevent the editor from becoming “a whole productivity app.”

**Outputs**

- One-sentence mission: “Make it easy to run the Daily Win workflow and maintain the backlog.”
    
- Explicit exclusions:
    
    - no calendar system
        
    - no deep project planning
        
    - no extensive analytics
        
    - no multi-step wizards
        

**Definition of Done**

- A tight list of what the editor does and does not do
    

---

## 5.2 — Define the Minimum Navigation Structure

**Objective:** Keep navigation simple and predictable.

**Outputs**

- Primary sections (v1):
    
    1. **Today**
        
    2. **Backlog**
        
    3. **History**
        
- Optional:
    
    - **Users** (can be hidden or “dev-only” in v1)
        

**Definition of Done**

- You can name the 3 core pages and what each contains in one line
    

---

## 5.3 — Today Page: Required Capabilities

**Objective:** Make “the daily workflow” operable.

**Outputs**  
Today page must support:

- View current Daily Win (or none)
    
- Select a task as today’s win (from filtered backlog)
    
- Resolve today’s win:
    
    - Done
        
    - Paused (note required)
        
    - Blocked (note required)
        
- Show the “definition of done” prominently (so resolution is obvious)
    

**Definition of Done**

- You can complete a day’s full lifecycle from this page alone
    

---

## 5.4 — Today Page: Selection Flow Design

**Objective:** Make selection fast and not overwhelming.

**Outputs**  
Selection UI decisions:

- How the task picker works:
    
    - search by title
        
    - filter by domain/effort/owner
        
    - show only eligible statuses (e.g., BACKLOG/PAUSED/BLOCKED; you define)
        
- What info appears in the picker list:
    
    - title
        
    - effort
        
    - domain
        
    - owner (if any)
        
    - short DoD preview
        

**Definition of Done**

- Written selection flow: “choose filters → pick task → confirm selection”
    

---

## 5.5 — Today Page: Resolution Note Capture

**Objective:** Make “Paused/Blocked” meaningful, not a junk drawer.

**Outputs**

- Note entry rule:
    
    - required for PAUSED/BLOCKED
        
- Note UI decision:
    
    - inline text box or modal
        
- Minimum note quality rule (planning only):
    
    - must be non-empty
        
    - optionally require at least X characters
        

**Definition of Done**

- A clear “how notes are captured” rule exists
    

---

## 5.6 — Backlog Page: Task List Capabilities

**Objective:** Make task maintenance manageable.

**Outputs**  
Backlog page supports:

- List tasks
    
- Filters:
    
    - status
        
    - domain
        
    - effort
        
    - owner
        
- Sorting (simple default):
    
    - most recently updated first (or created first)
        
- Quick visibility fields shown per task:
    
    - title
        
    - status
        
    - owner
        
    - domain
        
    - effort
        

**Definition of Done**

- Backlog can be navigated without scroll fatigue (filters reduce overload)
    

---

## 5.7 — Backlog Page: Add Task Flow

**Objective:** Reduce friction for capturing tasks.

**Outputs**  
Create task form includes:

- title (required)
    
- definition of done (required)
    
- domain (required, with default)
    
- effort (required, with default)
    
- owner (optional)
    
- materials needed (optional)
    

**Definition of Done**

- The minimum form fields are defined and match Phase 2 rules
    

---

## 5.8 — Backlog Page: Edit Task Flow

**Objective:** Allow correction without creating chaos.

**Outputs**  
Editable fields in v1:

- title
    
- definition of done
    
- domain
    
- effort
    
- owner
    
- materials
    
- status transitions must NOT be freeform editing (must use transition actions)
    

**Definition of Done**

- Clear distinction exists between “edit fields” and “change state”
    

---

## 5.9 — Backlog Page: State Transition Controls

**Objective:** Ensure state machine rules are respected through UI.

**Outputs**

- Transition actions presented as buttons/dropdown:
    
    - Move to BACKLOG (if allowed)
        
    - Pause/Block/Done (if allowed)
        
    - Abandon (optional)
        
- UI should only _offer_ valid transitions (but server still enforces)
    

**Definition of Done**

- Transition UI is planned as an explicit action, not a free text status edit
    

---

## 5.10 — History Page: Purpose and Minimal Features

**Objective:** Give “proof of progress” without creating analytics bloat.

**Outputs**  
History page shows:

- list of Daily Wins by date
    
- status for each day (DONE/PAUSED/BLOCKED)
    
- task title + owner
    
- note (if paused/blocked)
    
- completed timestamp (if done)
    

Optional:

- filters by date range
    
- “last 7 days” default view
    

**Definition of Done**

- You can answer: “What did we get done this week?” quickly
    

---

## 5.11 — Users Handling Policy (v1)

**Objective:** Decide how users are managed without building auth.

**Outputs**  
Choose one:

- Hardcoded 3 users in DB seeded once
    
- Simple “Users” page to add/edit users (still no auth)
    
- Dev-only seed endpoint used for users
    

**Definition of Done**

- You have a plan for user creation that doesn’t require authentication complexity
    

---

## 5.12 — Form Validation and Error Presentation (Planning Only)

**Objective:** Make it usable without confusion.

**Outputs**  
Define how the UI will handle:

- missing required fields
    
- state machine violations
    
- attempting to select a Daily Win when one is already ACTIVE
    
- missing pause/block note
    

**Definition of Done**

- A rule exists: errors must be shown in plain language near the action
    

---

## 5.13 — Web Editor Validation Checklist (Planning Only)

**Objective:** Define “editor done” clearly.

**Outputs**  
Checklist:

- Create task works
    
- Edit task works
    
- Filter backlog works
    
- Select daily win works
    
- Resolve daily win works (done/paused/blocked + note rules)
    
- History shows correct records
    
- UI does not require hidden knowledge to operate
    

**Definition of Done**

- A checklist exists that a non-technical family member could follow
    

---

# Phase 5 Definition of Done

Phase 5 is complete when:

- The editor’s scope is fenced
    
- Pages are defined (Today, Backlog, History)
    
- Each page’s minimum features are defined
    
- Task capture/edit/transition flows are defined
    
- Error-handling expectations are defined
    
- Validation checklist exists