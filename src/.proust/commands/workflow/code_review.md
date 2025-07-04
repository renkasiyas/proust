# Command: code_review

**Command**: `/project:code_review`
**Category**: Workflow
**Purpose**: Perform deep, zero-tolerance code review with security validation and architectural compliance

## Purpose
Perform a **deep, zero-tolerance code review** of recent changes and record the verdict in the appropriate task file.

## Context Loading

### Required Context
- `core/ethos.md` - Project development principles
- `core/guardrails.yml` - Code quality standards and constraints
- `core/architecture.yml` - Technical architecture patterns
- `project/manifest.yml` - Current project state
- `project/milestones/**` - Requirements for validation
- `project/decisions/**` - Architectural decisions for compliance

### Generated Context
- Code review verdict with severity-ranked findings
- Security vulnerability assessment
- Architecture compliance report

## Inputs
| Variable          | Description                                        | Default / Example                               |
|-------------------|----------------------------------------------------|-------------------------------------------------|
| `$ARGUMENTS?`     | File path(s) or commit SHA(s) to limit review scope| _empty_ → `HEAD~1` diff                         |
| `$DATE`           | Real-world date (UTC)                              | `2025-07-04`                                    |

## Preconditions
1. Repo has Git history.
2. Agent can run shell commands (`git diff`, `grep`).
3. `.proust/` framework structure exists.

## Steps
1. **Determine scope**
   - If `$ARGUMENTS?` provided, parse into file list or commit range.
   - Else default: `git diff HEAD~1`.
2. **Gather code changes**
   ```bash
   git diff --name-status $SCOPE > /tmp/changed_files.txt
   git diff $SCOPE > /tmp/full_diff.patch
   ```
3. **Locate related PM artifacts**
   - Read `project/manifest.yml` to find current sprint.
   - Open sprint definition in `project/sprints/M##_S##_*.md`.
   - If specific task ID appears in commit message, open task file from `project/tasks/`.
4. **Compare against specifications**
   - Check changed code vs. requirements in `project/milestones/M##_*.md`.
   - Validate architectural guardrails via `core/guardrails.yml`.
   - Verify compliance with `core/architecture.yml` patterns.
5. **Security validation**
   - **Authentication checks:** Verify proper authentication/authorization for new endpoints
   - **Input validation:** Check all user inputs are validated and sanitized
   - **Secret detection:** Scan for hardcoded secrets, API keys, passwords, or tokens
   - **Permission verification:** Ensure appropriate access controls on resources
   - **Injection prevention:** Validate against SQL injection, XSS, and command injection
   - **Dependency security:** Check for known vulnerabilities in new dependencies
6. **Identify issues**
   - For each discrepancy, assign Severity **1–10**.
   - Record list `[issue, severity]`.
7. **Verdict**
   - **FAIL** if _any_ discrepancy exists.
   - **PASS** only if zero issues.
8. **Write Output Log**
   - Append block to task’s **## Output Log** section OR sprint meta if no task.
   - Block format:
     ```
     [YYYY-MM-DDTHH:MM:SSZ] Code Review - PASS/FAIL
     Result: **PASS/FAIL**
     **Scope:** <files / commit range>
     **Architecture Findings:**
     - Issue 1 (Severity 7)
     - Issue 2 (Severity 3)
     **Security Findings:**
     - Security Issue 1 (Severity 9)
     - Security Issue 2 (Severity 6)
     **Summary:** <brief>
     **Recommendation:** <next steps>
     ```
9. **Console Summary**
   - Print PASS/FAIL + issue count.

## Outputs
| Target File (auto-append)                                     | Purpose                         |
|---------------------------------------------------------------|---------------------------------|
| Task file in `project/tasks/` **or** sprint file in `project/sprints/` | Persistent review log           |

## Definition of Done
- Log entry written with timestamp.
- PASS/FAIL clearly stated.
- Each finding includes Severity (1–10).
- Console displays concise summary.

## Follow-ups
- For each Severity ≥7 issue, create task via `/project:create_general_task`.
