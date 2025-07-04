# Command: do_task

**Command**: `/project:do_task`
**Category**: Workflow
**Purpose**: Process project tasks end-to-end with status tracking and code review

## Purpose

Process a project task end-to-end: select task, set status to in_progress, perform work, run code review, and finalize status with proper documentation.

## Context Loading

### Required Context
- `core/ethos.md` - Project principles and development values
- `core/guardrails.yml` - Code quality standards and constraints
- `project/manifest.yml` - Current project state and active sprint
- `project/milestones/**` - Requirements and milestone definitions
- `project/sprints/**` - Sprint goals and task assignments
- `project/tasks/**` - Task details and acceptance criteria

### Generated Context
- Task execution log with timestamped progress
- Code review results and quality validation
- Updated project state with task completion

## Inputs
| Variable    | Description                                              | Example          |
|-------------|----------------------------------------------------------|------------------|
| `$ARGUMENTS?| Task ID, Sprint ID, or blank (`select next open task`)   | `T05_S02`        |
| `$DATE`     | UTC date                                                 | `2025-07-04`     |

## Steps
1. **Analyse scope from argument**
   - If blank → choose next open task in current sprint (status: open).
   - Log chosen scope.

2. **Identify task file**
   - Search `project/tasks/` for matching task ID.
   - Check both sprint tasks (M##_S##_T##) and general tasks (T###).
   - If none matches → ask user how to proceed.

3. **Analyse the task**
   - Read task description & front-matter.
   - **Parallel validations:**
     1. Confirm task belongs to current sprint.
     2. Check dependencies completed.
     3. Read relevant requirements docs.
     4. Ensure task aligns with sprint objectives.
   - If unclear or blockers → prompt user.

4. **Set status to _in_progress_**
   - Timestamp `$DATE` local.
   - Update task front-matter: `status: in_progress`, `updated: $DATE`.
   - Update manifest sprint/task status accordingly.

5. **Execute task work**
   - Follow Description → Goal → Acceptance Criteria.
   - Loop subtasks: mark done & append `[YYYY-MM-DDTHH:MM:SSZ]: <message>` to **## Output Log**.
   - Consult docs as needed.

6. **Placeholder** – no-op.

7. **Execute Code Review**
   - Invoke `/project:code_review $TASK_ID`.
   - If **FAIL** →
     - Add review-identified subtasks.
     - Return to Step 5.
   - If **PASS** → continue.

8. **Finalize task status**
   - Set `status: completed`.
   - Rename file `T###` → `TX###` to indicate completion.
   - Update manifest.
   - Output summary block:
     ```
     ✅ Result: success
     🔎 Scope: $TASK_ID
     💬 Summary: <one-paragraph recap>
     ⏭️ Next steps: /project:simone:commit $TASK_ID
     ```

## Definition of Done
- Task file shows `status: completed`, renamed with `TX`.
- Manifest reflects completion.
- Code review PASS.
- Summary printed.

## Follow-ups
- Recommend `/project:commit $TASK_ID`.
- Suggest `/clear` to reset context.

## Implementation Example

**Demonstration with M01_S01_T01_QRGenerationService:**

```bash
/project:do_task M01_S01_T01

🔍 Loading task context for M01_S01_T01_QRGenerationService...
📋 Implementation Plan for M01_S01_T01:
  • Install QR generation library (30min)
  • Create QR service interface (45min)
  • Implement logo overlay logic (90min)
  • Add API endpoints (60min)
  • Write unit tests (90min)
  • Update documentation (30min)

🛠  Executing: Install QR generation library
✅ Installed qrcode library with PIL support
✅ Updated requirements.txt and package.json

🛠  Executing: Create QR service interface
✅ Created QRGenerationService class
✅ Implemented generate_qr() and generate_with_logo() methods
✅ Added proper error handling and logging

🛠  Executing: Implement logo overlay logic
✅ Added image composition with PIL
✅ Implemented logo positioning and sizing logic
✅ Added scannability validation

🛠  Executing: Add API endpoints
✅ Created /api/qr/generate endpoint
✅ Added request validation and error handling
✅ Integrated with QRGenerationService

🛠  Executing: Write unit tests
✅ Added test coverage for QR generation
✅ Added logo overlay tests with sample images
✅ Added API endpoint integration tests
✅ Achieved 94% test coverage

🛠  Executing: Update documentation
✅ Generated OpenAPI specification
✅ Added usage examples and troubleshooting guide
✅ Updated technical documentation

🔍 Running code review...
✅ Guardrails compliance: PASS
✅ Architecture alignment: PASS
✅ Testing coverage: 94% (PASS)
✅ Security validation: PASS
✅ Overall score: 9.2/10 (PASS)

✅ Task Completed: M01_S01_T01_QRGenerationService

📊 Execution Summary:
├── Duration: 4h 30m (under 6h estimate)
├── Steps Completed: 6/6
├── Code Review Score: 9.2/10 (PASS)
└── Files Modified: 12

🎯 Acceptance Criteria: 15/15 (100% complete)

📁 Key Deliverables:
├── QRGenerationService with logo overlay support
├── REST API endpoints with validation
├── Comprehensive test suite (94% coverage)
├── OpenAPI documentation
└── Performance optimization (<500ms requirement met)

📈 Next Actions:
1. Review implementation: project/tasks/M01_S01_T01_QRGenerationService.md
2. Commit changes: /project:commit M01_S01_T01
3. Continue sprint: /project:do_task (next task: M01_S01_T02)
```

This execution engine transforms abstract task descriptions into concrete, working implementations while maintaining quality standards and project coherence.