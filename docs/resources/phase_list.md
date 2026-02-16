Phase 0 — Project skeleton and boot

**Purpose:** Prove the app runs and you have a sane structure.

**Deliverables**

- Repo folders in place (`app/`, `templates/`, `static/`)
    
- FastAPI app boots
    
- Jinja renders a basic page
    
- Static assets load
    

**Acceptance checks**

- `uvicorn app.main:app --reload` runs
    
- `GET /api/health` returns `{"status":"ok"}`
    
- `GET /` returns HTML
    
- `/static/styles.css` loads in dev tools network tab
    

---

## Phase 1 — Data layer and models

**Purpose:** Establish the “truth” of the app: schema + DB session + migrations.

**Deliverables**

- SQLAlchemy Base + models: `User`, `Task`, `DailyWin`
    
- SQLite DB file created locally
    
- Simple migration strategy (Alembic recommended, but can start with `create_all`)
    

**Acceptance checks**

- App boots and creates/uses DB
    
- You can create/read rows via a tiny script or a temporary endpoint
    
- Model constraints match your rules (statuses, required fields)
    

---

## Phase 2 — Core domain rules: state machine + Daily Win enforcement

**Purpose:** This is the heart. Everything else is UI.

**Deliverables**

- Task state machine implemented (valid transitions only)
    
- Daily Win selection logic:
    
    - only 1 ACTIVE per date
        
    - cannot switch unless current is DONE or PAUSED/BLOCKED with note
        
- “Definition of Done” required on task creation
    
- Basic domain validation and error responses
    

**Acceptance checks**

- API refuses invalid transitions
    
- API refuses selecting a new Daily Win when today’s is unresolved
    
- API requires notes for PAUSED/BLOCKED
    
- 3–5 tests pass proving these invariants (even minimal tests)
    

---

## Phase 3 — API surface (CRUD + queries)

**Purpose:** Make the backend usable by any frontend (Jinja now, React later).

**Deliverables**

- Task endpoints:
    
    - create/edit/list/filter
        
    - transition endpoint
        
- Daily Win endpoints:
    
    - get today
        
    - select today
        
    - complete / pause / block today
        
- Minimal metrics endpoints:
    
    - weekly wins (last 7)
        
    - streak count (current consecutive days)
        

**Acceptance checks**

- You can operate the full Daily Win lifecycle via API alone
    
- Filters work (owner, domain, status, effort)
    
- No endpoint returns ambiguous junk; responses are predictable
    

---

## Phase 4 — Wall Board UI (display-first)

**Purpose:** The “TV dashboard” that changes behavior via visibility.

**Deliverables**

- `/board` fullscreen layout
    
- Shows:
    
    - Today’s Win (title, owner, definition of done, materials)
        
    - status badge (ACTIVE/PAUSED/BLOCKED/DONE)
        
    - streak + weekly completions
        
- Auto-refresh (poll every 15–30s) OR websocket (later)
    

**Acceptance checks**

- Board loads cleanly on a TV browser in fullscreen
    
- It updates when you change state in another tab/device
    
- It never shows the full backlog by default (minimal cognitive load)
    

---

## Phase 5 — Web Editor UI (control panel)

**Purpose:** Make the system operable without touching the database or code.

**Deliverables**

- `/app` basic pages:
    
    - Today (select/resolve Daily Win)
        
    - Backlog (add/edit tasks, filters)
        
    - History (past Daily Wins list)
        
- Forms with validation messages
    
- “Select Daily Win” flow that respects Phase 2 rules
    

**Acceptance checks**

- You can run the household workflow with _no API tool usage_
    
- Adding/editing tasks doesn’t break rules
    
- Switching Daily Win is impossible unless allowed
    

---

## Phase 6 — Suggestions engine (momentum support, not “productivity app”)

**Purpose:** Reduce decision friction each morning.

**Deliverables**

- Suggest 3 tasks based on:
    
    - effort (Tiny/Small)
        
    - owner availability (optional)
        
    - not recently completed (optional)
        
- Optional “energy mode” filter (Low/Med/High) — keep it simple
    

**Acceptance checks**

- Suggestions are stable and understandable (no “why did it pick this?” confusion)
    
- You can still manually pick any task
    

---

## Phase 7 — Persistence hardening + housekeeping

**Purpose:** Prevent the app from rotting over time.

**Deliverables**

- Data cleanup rules:
    
    - auto-close previous day’s ACTIVE as PAUSED (optional) OR “carryover” logic
        
- Basic audit fields (created_at/updated_at)
    
- Safe defaults for missing owners, domains, materials
    

**Acceptance checks**

- App behaves predictably when you skip days
    
- No “phantom active task” issues
    
- DB stays consistent over weeks
    

---

## Phase 8 — Deployment for a household (real-world use)

**Purpose:** Make it run reliably on a box you control.

**Deliverables (pick one)**

- **Simplest:** run on a spare PC / mini PC with `uvicorn` + startup script
    
- **Cleaner:** Docker + docker-compose
    
- Optional: reverse proxy (Caddy/Nginx) if you want LAN access
    

**Acceptance checks**

- Reboot machine → app comes back automatically
    
- TV can load `/board` from LAN reliably
    
- Backup plan exists (copy DB file daily/weekly)
    

---

## Phase 9 — React frontend swap (after v1 is stable)

**Purpose:** Upgrade UX without rewriting core logic.

**Deliverables**

- React app consuming your existing API
    
- Board view + editor view reimplemented
    
- CORS configured (or serve React build from FastAPI)
    

**Acceptance checks**

- All workflows still work with same backend invariants
    
- No rule moved to frontend-only (rules stay server-side)
    
- Jinja version can remain as fallback during transition
    

---

## Phase 10 — Optional “grown-up” features (only after you’ve shipped)

**Pick only if needed**

- Auth + roles
    
- Per-user energy + availability windows
    
- Notifications (digest, not nag spam)
    
- Inventory tracking for materials
    
- Recurring task generation
    
- Mobile-friendly layout
    

**Acceptance checks**

- Every new feature has a reason tied to household behavior, not “cool”