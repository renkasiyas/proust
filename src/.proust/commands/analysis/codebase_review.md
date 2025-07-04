# Command: analyze_codebase

**Command**: `/project:analyze_codebase`
**Category**: Analysis
**Purpose**: Generate comprehensive codebase health report with architecture compliance and deployment readiness assessment

## Purpose
Generate a **single-session health report** for an existing codebase:
- Architecture & guardrail compliance
- Feature completeness vs. manifests
- Deployment readiness (GO / NO-GO)
- Actionable recommendations

## Context Loading

### Required Context
- `core/ethos.md` - Project principles and values
- `core/guardrails.yml` - Code quality standards and constraints
- `core/architecture.yml` - Technical architecture decisions
- `core/external_docs.yml` - External documentation references
- `project/manifest.yml` - Current project state and milestones
- Latest assessment under `workspace/assessments/` (if any)

### Generated Context
- Comprehensive health report with deployment readiness
- Architecture compliance analysis
- Actionable recommendations for improvements

## Inputs
| Variable          | Description                        | Example                                                 |
| ----------------- | ---------------------------------- | ------------------------------------------------------- |
| `$ROOT_PATH`      | Absolute path to repo root         | `/workspace/App-backend`                                |
| `$DATE`           | Real-world date (UTC)              | `2025-07-04`                                            |
| `$STATUS_REPORT?` | Path to latest assessment (optional) | `workspace/assessments/2025-06-20_14-00_assessment` |

## Preconditions
1. Repo is present at **`$ROOT_PATH`**.
2. Shell tools **find**, **grep**, **tree** are available.
3. Agent can write to `workspace/assessments/`.

## Steps
1. **Generate directory tree**
   ```bash
   cd "$ROOT_PATH"
   find . -type f -not -path "*/node_modules/*" -not -path "*/.git/*" \
     | sort > /tmp/dir_tree.txt
   ```
2. **Diff against previous snapshot** (if `$STATUS_REPORT?` provided) and flag new/deleted files.
3. **Guardrail scan**
   - Raw colors → `grep -R "Color(" lib/ | grep -v AppColors || true`
   - Un-pinned deps → `grep -R "\^" **/pubspec.yaml || true`
4. **Load architecture & project state**
   - Parse `core/architecture.yml` for technical decisions
   - Parse `project/manifest.yml` for current milestones and sprints
   - Load `project/milestones/` and `project/sprints/` for requirements.
5. **Feature coverage**
   - If `FEATURES.md` exists, mark each feature ✅/🔄/❌.
   - Else derive feature list from code + manifests.
6. **Run tests** (if present)
   ```bash
   flutter test -q || true
   ```
7. **Produce outputs** (see table below).
8. **Save** all outputs under `workspace/assessments/$DATE/`.

## Outputs  →  `workspace/assessments/$DATE/`
| File                       | Purpose                                          |
|----------------------------|--------------------------------------------------|
| `overall_project_status.md`| Executive summary & completion %                 |
| `feature_checklist.md`     | Feature table with completion %                  |
| `identified_issues.md`     | Guardrail & code-quality findings                |
| `recommendations.md`       | Actionable next steps                            |
| `deployment_readiness.md`  | GO / NO-GO plus blockers                         |
| `project_structure.md`     | Directory tree (+ highlights for new files)      |
| `codebase_graph.png`       | Mermaid-generated architecture graph             |

## Definition of Done
- All output files exist in `workspace/assessments/$DATE/`
- Guardrail violations documented or resolved
- Summary line **“Ready for deployment: YES/NO”** present
- Each output file ends with ISO-8601 timestamp

## Related Commands

- `/project:create_general_task` - Create tasks for each critical issue found
- `/project:project_review` - Comprehensive project state review
- `/project:consistency_audit` - Deep contradiction analysis across all documents
- `/project:testing_review` - Detailed test suite alignment assessment

## Notes

- Run after major development milestones for deployment readiness
- Compare with previous assessments to track improvement trends
- Use findings to update guardrails and architecture decisions
