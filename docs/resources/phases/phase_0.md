Phase 0 - Project Skeleton & Environment Boot

**Goal:**  
The app runs locally.  
You understand the file structure.  
Nothing fancy exists yet.

This phase is about environment + wiring — not business logic.

## 0.1 — Repository Initialization

## Objective

Create a clean, controlled project container.

## Tasks

- Create root project folder
    
- Initialize Git repository
    
- Create virtual environment
    
- Create `requirements.txt`
    
- Install core dependencies:
    
    - FastAPI
        
    - Uvicorn
        
    - Jinja2
        
    - SQLAlchemy
        

## Acceptance Criteria

- `pip list` shows required dependencies
    
- `.venv` exists and is ignored by `.gitignore`
    
- Git repo initializes cleanly
    
- First commit contains only scaffold + requirements
    

---

# 0.2 — Folder Architecture Layout

## Objective

Define structural boundaries before implementation.

Create:

`app/     main.py     settings.py     db.py     templates/     static/ docs/     governance/     architecture/     phase_signoffs/   resources/  phases/

No business logic yet.

This is architectural zoning.

## Acceptance Criteria

- Folder structure matches exactly
    
- No unexplained files
    
- You can explain responsibility of:
    
    - main.py
        
    - settings.py
        
    - db.py
        
    - templates/
        
    - static/
        
    - docs/

---

# 0.3 — Documentation Foundation

## Objective

Establish formal development governance under the Milestone-Based Incremental Architecture (MBIA) model.

Create the following files:

docs/governance/development_model.md
docs/governance/ai_usage_policy.md
docs/governance/phase_signoff_protocol.md
docs/architecture/system_overview.md
docs/resources/phase_signoff_template.md
docs/resources/phase_list.md
README.md

---

## Required Initial Content

### development_model.md

Must define:

- Milestone-Based Incremental Architecture (MBIA)
    
- Definition of Milestone vs Sub-Step
    
- Phase progression rule (no skipping)
    
- Definition of Phase Sign-Off
    

Keep under 2 pages.

---

### ai_usage_policy.md

Must define:

- Roles:
    
    - Human Developer
        
    - ChatGPT (Control Plane)
        
    - Codex (Repository Auditor)
        
- What AI is used for
    
- What AI is NOT used for
    
- Commit authorship policy
    

Clear, concise, non-defensive.

---

### phase_signoff_protocol.md

Must include:

- End-of-phase review process
    
- Codex audit procedure
    
- Required artifacts:
    
    - Audit report
        
    - git log
        
    - git status
        
- Acceptance or remediation rule
    
- Reference to `phase_signoff_template.md` as the required sign-off structure
    

---

### system_overview.md

Must define:

- Project purpose
    
- Core invariant:
    
    > Exactly one Daily Win per day
    
- Architectural philosophy:
    
    - Server-side authority
        
    - State machine enforcement
        
- High-level component description (text only)
    

No diagrams required yet.

---

### phase_signoff_template.md

Must provide a reusable, fillable template including:

- Phase Number
    
- Date
    
- Deliverables Verified
    
- Acceptance Checks Verified
    
- Codex Audit Result
    
- Deviations / Notes
    
- Final Status (APPROVED / REMEDIATION REQUIRED)
    

This file is copied into `/docs/phase_signoffs/` at the end of each phase.

---

### phase_list.md

Must define:

- Full ordered list of project phases
    
- One-sentence purpose for each phase
    
- Clear boundary that phases are sequential and gated by sign-off
    

This acts as the canonical roadmap reference.

---

### Add individual phase documents to docs/resources/phases/

Must define:

- Import obsidian documentation on each phase into docs/resources/phases    

Thes act as the canonical roadmap reference for each phase.

---



### README.md

Must define:

- Project name: **householdMomentumTracker**
    
- One-paragraph purpose statement (what the system exists to do)
    
- Core invariant:
    
    > Exactly one Daily Win per day
    
- Statement that development follows **Milestone-Based Incremental Architecture (MBIA)**
    
- Link to `docs/governance/development_model.md`
    
- Minimal local run instructions:
    
    - activate `.trackerENV`
        
    - run `uvicorn app.main:app --reload`
        
- Clear note that phases are sequential and gated by formal sign-off
    

This acts as the repository’s public-facing entry point and architectural anchor.

---

## Acceptance Criteria

- `/docs` folder exists
    
- All six required documentation files exist
    
- `phase_signoff_template.md` exists and is usable
    
- `phase_list.md` reflects the intended project roadmap
    
- README references the development model
    
- Governance feels deliberate, not improvised
    
- README exists
    
- README references development_model.md
    
- README contains local run command

---

# 0.4 — Application Entry Point

## Objective

Prove FastAPI boots.

Implement:

- `FastAPI()` instance
    
- `/api/health` endpoint returning JSON
    

## Acceptance Criteria

- `uvicorn app.main:app --reload` runs without error
    
- `/api/health` returns `{ "status": "ok" }`
    
- No console errors
    

If this fails, fix before proceeding.

---

# 0.5 — Static File Mounting

## Objective

Confirm asset pipeline works.

Implement:

- `app.mount("/static", StaticFiles(...))`
    
- Basic CSS file
    

## Acceptance Criteria

- `/static/styles.css` loads
    
- CSS changes reflect on refresh
    

---

# 0.6 — Template Rendering (Jinja Wiring)

## Objective

Confirm server-rendered HTML works.

Implement:

- `Jinja2Templates(directory="app/templates")`
    
- Root `/` route rendering `home.html`
    
- Basic `base.html` inheritance
    

## Acceptance Criteria

- Visiting `/` renders HTML
    
- Template variables render correctly
    
- No template errors
    

---

# 0.7 — Configuration Isolation

## Objective

Separate config from logic.

Implement:

- `settings.py`
    
- Database URL stored in settings
    
- App name pulled from settings
    

## Acceptance Criteria

- Changing app name reflects in browser
    
- No hardcoded values in `main.py`
    

---

# 0.8 — Database Wiring (No Models Yet)

## Objective

Confirm DB connectivity layer initializes cleanly.

Implement:

- SQLAlchemy engine
    
- `SessionLocal`
    
- `get_db()` dependency function
    

Do NOT create models yet.

## Acceptance Criteria

- No startup errors
    
- DB file appears when used later
    
- Importing `get_db` works without circular imports
    

---

# Phase 0 Definition of Done

Phase 0 is complete when:

- App boots cleanly
    
- `/api/health` works
    
- `/` renders HTML
    
- Static files load
    
- Settings file works
    
- DB engine initializes
    
- `/docs` structure exists
    
- Governance documents exist
    
- No TODO comments in Phase 0 files
    
- You can explain every file without guessing