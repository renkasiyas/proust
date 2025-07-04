# Command: testing_review

**Command**: `/project:testing_review`
**Category**: Analysis
**Purpose**: Assess test suite alignment with testing strategy and identify coverage gaps

## Purpose
Assess the test suite’s alignment with the defined testing strategy (or general best practices), highlight misaligned tests, identify coverage gaps, and produce an actionable alignment report.

## Context Loading

### Required Context
- `project/docs/TESTING_STRATEGY.md` (if exists) - Testing strategy and standards
- `project/manifest.yml` - Project state and milestone information
- Test directories (`tests/`, `spec/`, etc.) - Actual test implementation

### Generated Context
- Test suite alignment report with actionable recommendations
- Coverage gap analysis mapped to project requirements
- Test quality assessment with improvement suggestions

## Inputs
| Variable | Description | Example |
|----------|-------------|---------|
| *(none)* | Interactive command |

## Steps
1. **Prerequisite check**
   - Detect `project/docs/TESTING_STRATEGY.md`.
   - If not present → ask user: create strategy or proceed with generic review?
   - Record approach (strategy vs. best-practice criteria).

2. **Analyze test implementation structure**
   - Run test suite using detected framework (npm test, pytest, flutter test, etc.).
   - Explore test directory layout, naming conventions, utilities.
   - Identify categories (unit, integration, API).

3. **Evaluate test-to-code alignment**
   - For each major component, assess if tests validate behavior.
   - Flag tests focused on implementation details or with fragile setups.

4. **Identify misaligned / unnecessary tests**
   - Using strategy document (if exists) or general principles:
     - Over-engineered, out-of-scope, redundant tests.
   - Compile list for removal or simplification.

5. **Assess critical functionality coverage**
   - Verify high-priority areas (from strategy or critical paths) have adequate tests.
   - Note missing tests for auth, error handling, data integrity, integrations.

6. **Generate modification recommendations**
   - For each finding:
     ```
     File: <path>::<test_name>
     Issue: <problem>
     Action: <remove/simplify/add>
     Reason: <alignment rationale>
     ```

7. **Create alignment report**
   - Timestamped file: `workspace/assessments/YYYY-MM-DD-HH-MM-test-alignment.md`
   - Use detailed markdown template (Alignment Summary, Tests Requiring Modification, Recommended Actions, Test Health Indicators, Next Review).
   - Print concise console summary.

## Definition of Done
- Report file created with alignment rating and actionable list.
- Console summary printed.
- Any questions asked to user resolved.

## Follow-ups
- Convert recommended actions into tasks via `/create_general_task`.
- If no strategy exists, propose creating `project/docs/TESTING_STRATEGY.md`.