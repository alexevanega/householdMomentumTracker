Phase 10 - React Retrofit & UI Swap

**Goal:**  
Replace the Jinja-based UI with a React frontend **without changing the backend rules**. This is a UI layer swap, not a rewrite.

**Non-goals (Phase 10):**

- No redesigning core logic (state machine + Daily Win rules stay server-side)
    
- No “new feature” spree while refactoring
    
- No premature scaling/enterprise architecture
    
- No auth unless you already proved you need it in Phase 9
    

---

## 10.1 — Lock the Backend Contract

**Objective:** Freeze the API so React has a stable target.

**Outputs**

- A short “API Contract” note:
    
    - endpoints used by board/editor
        
    - request/response shapes (examples)
        
    - error cases and codes
        
- Decide whether any endpoints need minor cleanup _before_ React begins
    

**Definition of Done**

- You can build React purely by consuming the API
    
- You are not tempted to “fix things” mid-frontend build
    

---

## 10.2 — Decide the React Hosting Strategy

**Objective:** Choose how React will be served.

**Outputs (choose one)**

- **A) Separate dev server + CORS**
    
    - React dev server during development
        
    - backend serves API only
        
- **B) Build React and serve static build from FastAPI**
    
    - single server in deployment
        
    - simplest long-term household hosting
        

**Definition of Done**

- One strategy chosen and documented with a one-sentence reason
    

---

## 10.3 — Recreate the Wall Board in React

**Objective:** Replace `/board` with a React board view, same behavior.

**Outputs**

- Fullscreen board page:
    
    - today’s win
        
    - status + note
        
    - owner
        
    - DoD + materials
        
    - streak + weekly wins
        
- Refresh strategy:
    
    - polling at same interval as Jinja version (keep it stable)
        

**Definition of Done**

- Board is functionally identical to Jinja version
    
- It works on the wall display in kiosk mode
    

---

## 10.4 — Recreate the Web Editor in React

**Objective:** Replace `/app` workflows, not “improve everything.”

**Outputs**  
React pages:

- Today
    
- Backlog
    
- History
    

Flows:

- select daily win
    
- resolve win with note
    
- CRUD tasks
    
- task transition actions
    
- filters
    

**Definition of Done**

- Household can run the system entirely from React UI
    
- No loss of capabilities from Jinja UI
    

---

## 10.5 — Frontend Validation Rules (Client-Side Convenience Only)

**Objective:** Improve UX without moving authority to the client.

**Outputs**

- Client-side validation mirrors server rules:
    
    - required fields (title, DoD)
        
    - note required for pause/block
        
- Server remains the enforcer; client just reduces annoying errors
    

**Definition of Done**

- Breaking rules still fails safely server-side
    
- UI prevents obvious mistakes but cannot bypass invariants
    

---

## 10.6 — Data Fetching and Error Handling Standardization

**Objective:** Keep network logic consistent.

**Outputs**

- One pattern for:
    
    - loading states
        
    - error banners
        
    - retry behavior
        
- Decide whether to use:
    
    - fetch only (simple)
        
    - a lightweight helper wrapper
        
    - avoid heavy state libs for v1 retrofit
        

**Definition of Done**

- All pages handle API down situations gracefully
    
- You don’t duplicate error-handling logic everywhere
    

---

## 10.7 — Deployment Transition Plan

**Objective:** Swap UIs without breaking the home setup.

**Outputs**

- Decide:
    
    - Keep Jinja routes available as fallback for a while, or remove them
        
- Update kiosk URL if needed
    
- Ensure single deployment path remains simple
    

**Definition of Done**

- Wall display still “just works”
    
- If React build fails, you have a rollback path
    

---

## 10.8 — Cutover and Cleanup

**Objective:** Remove dead UI code and finalize.

**Outputs**

- Remove or archive:
    
    - Jinja templates (if fully replaced)
        
    - redundant routes
        
- Update README:
    
    - how to run dev
        
    - how to build
        
    - how to deploy
        
- Confirm API contract unchanged
    

**Definition of Done**

- Repo is understandable again (no “two half frontends” confusion)
    
- React is the primary UI and is stable
    

---

## 10.9 — Post-Retrofit Stability Check

**Objective:** Ensure the swap didn’t introduce regressions.

**Outputs**  
Regression checklist:

- daily win selection rules still enforced
    
- pause/block note required
    
- board refresh works
    
- history accurate
    
- backlog filters work
    
- deployment auto-start still works
    

**Definition of Done**

- React UI passes the same workflow checklist as the original Jinja UI
    

---

# Phase 10 Definition of Done

Phase 10 is complete when:

- React fully replaces Jinja for board + editor
    
- Backend rules are unchanged and still authoritative
    
- Deployment remains simple and reliable for household use
    
- You have a rollback plan (even if just “use the previous build”)