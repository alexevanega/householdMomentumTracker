Phase 1 - Data Modeling & Persistence

**Goal:**  
Your database becomes the single source of truth: models exist, tables exist, and you can create/read real data reliably.

**Non-goals (Phase 1):**

- No Daily Win “rules” enforcement yet (that’s Phase 2)
    
- No UI work beyond what already exists
    
- No “nice” filtering or metrics
    

---

## 1.1 — Create the Models Module Boundary

**Objective:** Put all DB model definitions in one place so imports don’t turn into spaghetti.

**Tasks**

- Create `app/models/` folder
    
- Add:
    
    - `app/models/__init__.py`
        
    - `app/models/base.py`
        
    - `app/models/user.py`
        
    - `app/models/task.py`
        
    - `app/models/daily_win.py`
        

**Acceptance Criteria**

- App still boots after these files exist (even empty placeholders)
    
- You can import `Base` without circular import errors
    

---

## 1.2 — Define `Base` (Declarative Base + Timestamps Helper)

**Objective:** Establish the shared SQLAlchemy foundation.

**Tasks**

- In `app/models/base.py`:
    
    - Create `Base = declarative_base()`
        
    - Add a `TimestampMixin` with `created_at` and `updated_at`
        
    - Ensure `updated_at` auto-updates on changes
        

**Acceptance Criteria**

- Importing `Base` and `TimestampMixin` works
    
- No DB actions yet; just definitions compile
    

---

## 1.3 — Define the `User` Model

**Objective:** Represent household members.

**Tasks**

- In `app/models/user.py` create `User` table with:
    
    - `id` (int PK)
        
    - `name` (required)
        
    - `role` (optional string)
        
    - `active` (bool default True)
        
    - `created_at`, `updated_at`
        

**Acceptance Criteria**

- Model imports cleanly
    
- Table name is stable (`users`)
    
- `name` is non-null
    

---

## 1.4 — Define Task Enums (Domain, Effort, Status)

**Objective:** Centralize allowed values so the app doesn’t drift.

**Tasks**

- Create `app/models/enums.py` with:
    
    - `TaskDomain`: CHORES, BILLS, FOOD, REPAIRS, OTHER
        
    - `TaskEffort`: TINY, SMALL, MEDIUM, COMPLEX
        
    - `TaskStatus`: BACKLOG, ACTIVE, PAUSED, BLOCKED, DONE, ABANDONED
        

**Acceptance Criteria**

- You can import enums anywhere without circular imports
    
- No validation logic yet—just definitions
    

---

## 1.5 — Define the `Task` Model

**Objective:** Represent “work items” (not a to-do list—stateful items).

**Tasks**

- In `app/models/task.py` create `Task` with:
    
    - `id` (PK)
        
    - `title` (required)
        
    - `domain` (required; enum stored as string)
        
    - `effort` (required; enum stored as string)
        
    - `definition_of_done` (required text)
        
    - `materials_needed` (optional text)
        
    - `owner_user_id` (nullable FK → users.id)
        
    - `status` (required; default BACKLOG)
        
    - timestamps
        

**Acceptance Criteria**

- Task model imports without errors
    
- FK to users compiles
    
- Required fields are non-null
    

---

## 1.6 — Define the `DailyWin` Model

**Objective:** Store Daily Win history cleanly.

**Tasks**

- In `app/models/daily_win.py` create `DailyWin` with:
    
    - `id` (PK)
        
    - `date` (required, unique per day)
        
    - `task_id` (required FK → tasks.id)
        
    - `status` (required; ACTIVE/DONE/PAUSED/BLOCKED)
        
    - `note` (optional for now; we enforce it in Phase 2)
        
    - `selected_by_user_id` (nullable FK → users.id)
        
    - `completed_at` (nullable datetime)
        
    - timestamps
        

**Acceptance Criteria**

- Unique constraint on `date` exists
    
- FKs compile correctly
    
- Model imports cleanly
    

---

## 1.7 — Wire Models Into DB Initialization

**Objective:** Ensure the DB tables actually get created.

**Tasks**

- Update `app/db.py` to import `Base`
    
- Add a function like `init_db()` that runs `Base.metadata.create_all(bind=engine)`
    
- Call `init_db()` once at app startup (in `main.py`)
    

**Acceptance Criteria**

- On first run, `momentum.db` appears
    
- Tables exist in the DB file
    

---

## 1.8 — Add a “DB Smoke Test” Endpoint (Temporary)

**Objective:** Prove persistence works before writing real CRUD.

**Tasks**

- Add temporary endpoints:
    
    - `POST /api/dev/seed` (creates 2 users and 2 tasks)
        
    - `GET /api/dev/status` (returns counts: users/tasks/daily_wins)
        

**Acceptance Criteria**

- You can seed once
    
- Refresh and counts persist
    
- No crashing on repeated requests (idempotency not required yet, but it shouldn’t explode)
    

---

## 1.9 — Phase 1 Cleanup (Remove What You Don’t Need Yet)

**Objective:** Keep Phase 1 clean and ready for Phase 2.

**Tasks**

- Leave dev endpoints in place but clearly labeled `/api/dev/*`
    
- Add a comment: “Remove dev routes before deployment” (later phase)
    
- Ensure all model imports are stable from `app/models/__init__.py`
    

**Acceptance Criteria**

- App still boots
    
- DB persists
    
- You can explain the schema without hand-waving
    

---

# Phase 1 Definition of Done

You are done with Phase 1 when:

- DB file exists
    
- Tables exist: `users`, `tasks`, `daily_wins`
    
- You can insert and read sample rows
    
- No circular import pain
    
- You have a stable place to add logic next phase