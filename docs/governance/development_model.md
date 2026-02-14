# Development Model (MBIA)

## What This Is:
This project follows **Milestone-based Incremental Architecture (MBIA)**: the system is built in strict phases where each phase proves a specific capability before any later work begins.

The goal is reliability and clarity over speed.

## Terms

### Milestone
A **Milestone** (also known as a Phase) is a section of work with a defined purpose, deilverables, and acceptance checks.

A milestone is only considered complete after a sign-off review

### Sub-Phase
A **Sub-Phase** is a small, verifiable unit of work within a milestone (or phase). For example, "static file mounting works"

Sub-phases must be completed in order and must meet their acceptance criteria before moving forward.

## Phase Progression Rule
- Phases are completed **in numeric order**
- No Skipping ahead
- No implementing later-phase features early "because it is easy"
- If a later need is discovered, it is recorded and deferred to the correct phase

## Phase Sign-Off
At the end of every phase, the contributor performs a **Phase Sign-Off**:
- verify acceptance checks
- confirm required artifacts exist
- record the sign-off result in 'docs/phase_signoffs/
- A phase is not "done" until it is singed offS