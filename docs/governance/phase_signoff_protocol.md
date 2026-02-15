# Phase Sign-Off Protocol

## Purpose
A Phase Sign-Off formally verifies that a milestone is complete before progressing to the next phase.

No phase is considered complete without sign-off.

---

## End-Of-Phase Review Process

At the end of a phase:

1. Review the phase deliverables (can be found in docs/resources/phase_list.md)
2. Confirm all acceptance checks pass.
3. Verify no scope from later phases was implemented early.
4. Comfirm documentation reflects current system state.

---

## Codex Audit Procedure

Before Sign-Off:

1. Run repository audit using Codex.
2. Verify: 
- Required files exist
- No Missing artifacts
- No unexpected files introduced
- No partial implementation
3. Confirm structure matches documented arhitecture.

Audit findings must be either:
- Accepted (no issues)
- Remediated before sign-off

---

## Required Artifacts

Each phase must produce:

- Updated documentation
- Git log showing clean commits
- Clean "git status"
- Completed Phase Sign-Off (found in docs/resources/phase_signoff_template.md)

---

## Acceptance or Remediation Rule

If acceptance checks fail:
- The phase remains open
- Issues are corrected before continuing (No backlogging)

---

## Sign-Off Template

Each completed phase must create a file in:

docs/phase_signoffs/

File name format:
phase_X_signoff.md (Phase number goes in place of 'x')

Contents:

- Phase number:
- Date:
- Acceptance Checks Verified:
- Codex Audit Result:
- Notes:
- Status: APPROVED / REMEDIATION REQUIRED

Template found in docs/resources/phase_signoff_template.md