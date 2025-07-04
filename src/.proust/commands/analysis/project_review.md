# Command: project_review

**Command**: `/project:project_review`
**Category**: Analysis
**Purpose**: Conduct comprehensive high-level review of entire project state with John Carmack-style analysis

## Purpose
Conduct a comprehensive, high-level review of the **entire project state**—architecture, progress, tests, file organization—and archive findings in `workspace/assessments/`.

## Context Loading

### Required Context
- `project/manifest.yml` - Project state and milestones
- `project/docs/**` - Architecture documentation
- `project/milestones/**` - Requirements and milestone definitions
- `project/sprints/**` - Sprint goals and deliverables
- `project/decisions/**` - Architectural decision records
- Previous review files in `workspace/assessments/` (optional trend analysis)

### Generated Context
- Comprehensive project health assessment
- Technical debt and complexity analysis
- Progress evaluation against planned milestones

## Inputs
| Variable        | Description                                  | Example                |
|-----------------|----------------------------------------------|------------------------|
| `$ARGUMENTS?`   | Optional focus filter (milestone, sprint…)   | `M02` or `S04`         |
| `$DATE`         | Current UTC date                             | `2025-07-04`           |

## TODO (execute sequentially)

1. **Analyze review scope & timing**
   - If `$ARGUMENTS?` empty → full project review.
   - Else limit focus to specified milestone/sprint/component.
   - Read manifest to capture current milestone, sprint, task status.

2. **Execute & assess test infrastructure health**
   - Run test suite using appropriate framework (npm test, pytest, etc.).
   - Parse results → pass rate, categories, health score (0-10).
   - Determine blocking status (<6 blocks sprint, <8 blocks milestone).

3. **Assess project documentation alignment**
   - Parallel read: ARCHITECTURE.md, requirements, ADRs.
   - Identify gaps between docs and codebase reality.

4. **Review milestone & sprint progress**
   - Compare completed vs. planned deliverables in current sprint.
   - Evaluate alignment with milestone goals.

5. **Analyze codebase architecture & structure**
   - Examine directory layout, dependencies, schemas, APIs, config patterns.
   - Flag deviations from documented architecture.

6. **Audit file organization & workflow compliance**
   - Root dir hygiene, test placement, docs placement, rogue scripts.
   - Flag violations & cleanup needs.

7. **Evaluate technical decisions & complexity**
   - Assess framework choices, scalability, over/under-engineering.

8. **Critique implementation quality (John Carmack lens)**
   - Provide 3 blunt observations on simplicity, performance, maintainability.

9. **Provide comprehensive assessment & recommendations**
   - Timestamped report in `workspace/assessments/` named:
     `YYYY-MM-DD-HH-MM-<judgment-slug>.md`
   - Use detailed markdown template (see below).

### Report Template
> Save exactly with this structure.

```markdown
# Project Review - [YYYY-MM-DDTHH:MM:SSZ]

## 🎭 Review Sentiment
[🎯💥🚀]  <!-- 3 emojis only -->

## Executive Summary
- **Result:** EXCELLENT | GOOD | NEEDS_WORK | CRITICAL_ISSUES
- **Scope:** <areas reviewed>
- **Overall Judgment:** <slug>

## Test Infrastructure Assessment
… (follow detailed template from spec)
```
*(include full sections: Development Context, Progress, Architecture, File Audit, Critical Findings, Carmack Critique, Recommendations)*

## Validation

- [ ] Report file created in `workspace/assessments/` with timestamp & slug
- Summary printed to console (Result, slug, next steps).

## Follow-ups
- If critical issues → create general tasks.
- Suggest next sprint focus based on findings.