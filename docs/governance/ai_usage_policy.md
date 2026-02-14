# AI Usage Policy

## Roles

### Human Developer:
- Makes architectural decisions
- Writes and commits code
- Approves phase completion
- Owns correctness of the system

AI does not replace responsibility

---

### ChatGPT (Control Plane)
ChatGPT is used for:
- Structured Planning
- Phase breakdown guidance
- Architecture reasoning
- Clarifying technical concepts
- Generating draft documentation

ChaptGPT is NOT used for:
- Direct repository modification
- Blind code dumping without review
- Making unverified assumptions about project state

### Codex (Repository Auditor)
Codex is used for:
- Reviewing repository structure
- Checking file consistency
- Verifying implementation matches plan
- Spotting drift between documentation and code

Codex does not decide architecture

---

## Commit Authorship Policy

All commits are authored by the human developer

AI-assisted content is allowed, but:
- The Human Developter reviews all generated material
- The Human Developer is accountable for correctness
- AI is never credited as a commit author

---

## AI Boundary Principle

AI assists with:
- Planning
- Drafting
- Reviewing

AI does not:
- Control the repository
- Override architectural rules
- Make phase progression decisions

Final authority always rests with the Human Developer