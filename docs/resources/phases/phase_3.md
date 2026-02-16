Phase 3 - API Surface & Operational Workflows

**Goal:**  
Define the API your app will expose so **any frontend** (Jinja now, React later, wall board, mobile, etc.) can operate the system without re-implementing rules.

**Non-goals (Phase 3):**

- No UI pages (Phase 4/5)
    
- No suggestion engine (Phase 6)
    
- No deployment/hardening (later)
    
- No auth/roles (v1)
    

---

## 3.1 — Define API Principles and Conventions

**Objective:** Keep the API predictable and easy to build against.

**Outputs**

- Base path: `/api`
    
- Response format conventions (consistent keys, error structures)
    
- Status codes expectations (200/201, 400, 404, 409)
    
- Naming conventions (snake_case vs camelCase; choose one)
    

**Definition of Done**

- You have a short “API style” note: naming, error shapes, and success shapes
    

---

## 3.2 — Define Core Resources

**Objective:** Identify the nouns the API exposes.

**Outputs**

- Resources:
    
    - Tasks
        
    - Users (minimal in v1)
        
    - Daily Win (today + history)
        
    - Metrics (streak, weekly)
        
- Clear statement of what is NOT a resource (e.g., “Energy mode” not v1)
    

**Definition of Done**

- You can list each resource and what it’s responsible for in one sentence
    

---

## 3.3 — Task Endpoints Planning

**Objective:** Define the minimal endpoints needed to manage tasks.

**Outputs**

- List tasks (with filters)
    
- Create task
    
- Update task
    
- Get task by id
    
- Transition task status (state machine entry point)
    

**Definition of Done**

- You can operate the entire backlog without touching the DB directly
    
- Task transitions are routed through one explicit “transition” concept
    

---

## 3.4 — Task Filtering and Query Plan

**Objective:** Plan how the app will retrieve the right tasks without UI hacks.

**Outputs**

- Supported filters for v1:
    
    - status
        
    - domain
        
    - effort
        
    - owner
        
- Sorting rules (default sort; keep simple)
    
- Pagination decision (v1 can omit if small household scale)
    

**Definition of Done**

- You have a written list of filters and a default sorting policy
    

---

## 3.5 — Daily Win Endpoints Planning

**Objective:** Define how the “one win per day” workflow is controlled.

**Outputs**

- Get today’s daily win
    
- Select today’s daily win
    
- Resolve today’s daily win as:
    
    - done
        
    - paused (note required)
        
    - blocked (note required)
        
- Get history of daily wins (date range)
    

**Definition of Done**

- You can complete a full day’s lifecycle entirely via API calls
    

---

## 3.6 — Cross-Resource Behavior Requirements

**Objective:** Make explicit how tasks and daily wins affect each other.

**Outputs**

- Selecting a daily win affects:
    
    - DailyWin record for today
        
    - Task status (likely becomes ACTIVE)
        
- Completing a daily win affects:
    
    - DailyWin status DONE
        
    - Task status DONE
        
- Pausing/blocking affects:
    
    - DailyWin status + note
        
    - Task status PAUSED/BLOCKED (or remain ACTIVE—decide and document)
        

**Definition of Done**

- All cross-effects are written as “When X happens, Y must also happen”
    

---

## 3.7 — Metrics Endpoints Planning

**Objective:** Support the wall board with minimal, meaningful numbers.

**Outputs**

- Current streak: consecutive days with DONE daily win
    
- Weekly wins: count/list for last 7 days
    
- Optional: paused/blocked today indicator (not a metric, just state)
    

**Definition of Done**

- You can render the board’s bottom section (streak + weekly) using API alone
    

---

## 3.8 — Dev/Debug Endpoints Policy

**Objective:** Decide how you’ll inspect and seed the app during development.

**Outputs**

- Whether dev endpoints exist (`/api/dev/...`) or not
    
- What is allowed:
    
    - seed sample data
        
    - reset DB (dangerous; usually local only)
        
    - dump current state summary
        

**Definition of Done**

- You have a documented rule: dev endpoints allowed only in local mode
    

---

## 3.9 — Error Cases and Conflict Handling

**Objective:** Ensure the API communicates “why not” clearly.

**Outputs**

- Define key conflict scenarios and how API responds:
    
    - selecting a daily win when one already ACTIVE
        
    - invalid transition (state machine violation)
        
    - missing required note
        
    - missing required definition of done
        
- Decide whether conflicts are 400 vs 409 (pick one policy)
    

**Definition of Done**

- You have a list of at least 10 error cases and expected response behavior
    

---

## 3.10 — API Test Plan (Planning Only)

**Objective:** Define what must be true before moving to UI work.

**Outputs**  
A scenario checklist such as:

- Create task → list shows it
    
- Update task → list reflects change
    
- Transition invalid → API rejects
    
- Select daily win → appears in GET today
    
- Resolve daily win → history shows it
    
- Streak increments only on DONE
    
- Weekly endpoint returns correct counts
    

**Definition of Done**

- You have a written checklist that can be used as manual tests or automated tests later
    

---

# Phase 3 Definition of Done

You are done with Phase 3 when:

- All endpoints for tasks, daily win, and metrics are defined
    
- Filters and cross-resource effects are defined
    
- Error policy is defined
    
- A test plan exists for the full daily workflow
    

No UI, no implementation—this is the contract the UI will consume.