Phase 8 - Deployment & Environmental Setup

**Goal:**  
Get the app running reliably in your home environment (LAN-accessible, wall-display friendly, auto-starts after reboot, and recoverable if something breaks).

**Non-goals (Phase 8):**

- No React retrofit (later)
    
- No cloud hosting requirements
    
- No enterprise security posture
    
- No complex HA/cluster setups
    
- No overbuilt DevOps
    

---

## 8.1 — Define the Target Runtime Environment

**Objective:** Decide where this lives physically.

**Outputs**

- Host device decision:
    
    - spare desktop/laptop
        
    - mini PC (ideal)
        
    - NAS/docker host
        
    - Raspberry Pi (possible but adds constraints)
        
- Always-on expectation:
    
    - 24/7 or “most days”
        
- Network:
    
    - LAN-only access
        
    - Wi-Fi vs ethernet reliability preference
        

**Definition of Done**

- You can answer: “What machine runs this, where is it, and is it always on?”
    

---

## 8.2 — Define “Wall Display” Hardware and Browser Mode

**Objective:** Ensure the board is effortless to show.

**Outputs**

- Display device:
    
    - TV with built-in browser
        
    - Chromecast + kiosk page
        
    - cheap mini PC connected via HDMI
        
- Kiosk behavior:
    
    - full-screen startup
        
    - reload on crash
        
- Input method:
    
    - display-only (no mouse)
        
    - light-touch (remote/mouse)
        

**Definition of Done**

- You can answer: “How does the board stay open on the wall without constant fiddling?”
    

---

## 8.3 — Choose the Deployment Method (One Only)

**Objective:** Pick a deployment style that matches household reliability.

**Outputs**  
Pick one:

- **A) Simple service on the host machine**
    
    - run `uvicorn` as a service
        
- **B) Docker (recommended if you’re comfortable)**
    
    - containerized app + volume for SQLite DB
        
- **C) Hybrid**
    
    - docker only later, start simple first
        

**Definition of Done**

- You’ve chosen one method and documented why (simplicity vs repeatability)
    

---

## 8.4 — Define Environment Configuration Strategy

**Objective:** Stop config from being hard-coded.

**Outputs**

- Config mechanism:
    
    - `.env` file on the host
        
    - environment variables
        
- What becomes configurable:
    
    - DB path
        
    - host/port
        
    - dev/prod mode toggle
        
    - “disable dev endpoints” flag
        

**Definition of Done**

- You can list what settings differ between development and household deployment
    

---

## 8.5 — Define Data Persistence and Storage Location

**Objective:** Make sure your SQLite DB doesn’t vanish.

**Outputs**

- Decide where `momentum.db` lives in deployment:
    
    - local folder on host
        
    - mounted volume (if docker)
        
- Decide file permissions + ownership expectations
    
- Decide backup target folder
    

**Definition of Done**

- You can answer: “If I reinstall the app, where is the DB and how do I keep it?”
    

---

## 8.6 — Define Auto-Start on Boot

**Objective:** Remove “someone has to start the server” dependency.

**Outputs**  
Pick based on OS:

- Windows: Task Scheduler
    
- Linux: systemd service
    
- macOS: launchd
    

Define:

- start command
    
- working directory
    
- restart policy
    

**Definition of Done**

- A reboot brings the app back without manual intervention
    

---

## 8.7 — Define LAN Access and Addressing

**Objective:** Make it reachable from the wall display and household devices.

**Outputs**

- Host binding choice:
    
    - bind to `0.0.0.0`
        
- Fixed address strategy:
    
    - static local IP OR router DHCP reservation
        
- Access URL policy:
    
    - use IP:port
        
    - or local hostname (optional)
        

**Definition of Done**

- You can consistently load `/board` from another device on the network
    

---

## 8.8 — Define Reverse Proxy or “Direct Port” Policy

**Objective:** Decide whether you keep it simple or make it nicer.

**Outputs**  
Choose one:

- **Direct port** (simplest): `http://host:8000/board`
    
- **Reverse proxy** (cleaner): `http://momentum-board.local/board`
    

**Definition of Done**

- Your access method is documented and repeatable
    

---

## 8.9 — Define Operational Monitoring (Very Minimal)

**Objective:** Know when it’s broken.

**Outputs**

- Decide minimal monitoring:
    
    - “health endpoint check” manual
        
    - log file location
        
    - optional: simple uptime ping (later)
        
- Decide what family does when board is blank:
    
    - restart display browser
        
    - restart service (one simple step)
        

**Definition of Done**

- There’s a simple “if it breaks, do this” procedure that isn’t you doing forensic debugging at midnight
    

---

## 8.10 — Define Deployment Validation Checklist

**Objective:** Prove it’s usable in real household conditions.

Checklist:

- App auto-starts after reboot
    
- Board loads in fullscreen on the wall device
    
- Board survives idle mode / screen saver behavior (if applicable)
    
- Web editor accessible from phone/laptop on LAN
    
- DB persists after restart
    
- Backup procedure works (copy DB, restore DB)
    
- Dev endpoints disabled in “prod mode” (if that’s your rule)
    
- Performance is smooth enough for household use
    

**Definition of Done**

- You can run through the checklist and confidently call it “deployed”
    

---

# Phase 8 Definition of Done

Phase 8 is complete when:

- The app runs on a chosen host reliably
    
- The wall display is stable and easy
    
- The editor is accessible on LAN
    
- Auto-start and persistence are solved
    
- Backup and recovery is documented