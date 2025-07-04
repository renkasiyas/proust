# Command: gh_do_issues

**Command**: `/project:gh_do_issues`
**Category**: Workflow
**Purpose**: Select and implement small GitHub issues with automated PR creation

## Purpose
Select a small GitHub issue, plan a fix, implement it on a new branch with tests, submit a pull request, and keep the issue open until merged—all in a reproducible, documented flow.

## Context Loading

### Required Context
- `core/ethos.md` - Development principles and contribution standards
- `project/manifest.yml` - Current project state
- `project/docs/**` - Architecture documentation
- `project/decisions/**` - Architectural decision records

### Generated Context
- GitHub issue analysis and implementation plan
- Branch and PR creation with proper linking
- Test coverage for implemented fixes

## Inputs
| Variable       | Description                                     | Example             |
|----------------|-------------------------------------------------|---------------------|
| `$ISSUE_URL?`  | Optional GitHub issue URL to target             | `https://github.com/org/repo/issues/42` |
| `$DATE`        | Current UTC date                                | `2025-07-04`        |

## Preconditions
1. Local repo linked to GitHub origin.
2. Issue list accessible via `gh issue list` or web API.
3. Tests runnable via project’s test suite (`npm test`, `flutter test`, etc.).

## Steps
1. **Review GitHub issues & choose one**
   - If `$ISSUE_URL?` provided → verify it’s small & quick.
   - Else list open issues sorted by “good first issue” label and low effort tags.
   - Log chosen issue ID and title.

2. **Plan approach & comment**
   - Draft plan: scope, files to change, test strategy.
   - Post comment on issue via `gh issue comment` or web UI.
   - Wait for maintainer acknowledgment if required.

3. **Create new branch & implement**
   - Branch name: `issue/<number>-<slug>`
   - Implement fix with robust, documented code.
   - Add/extend tests; include debug logging where appropriate.
   - Run full test suite; ensure green.

4. **Open pull request**
   - Push branch to origin.
   - PR title: `fix: <issue title> (closes #<number>)`.
   - Base branch = previous unmerged branch if chained, else main.
   - Fill PR description with plan recap and test evidence.

5. **Keep issue open until PR merged**
   - Link PR to issue via “closes #<number>”.
   - Monitor CI; address review feedback promptly.
   - Once merged, verify issue auto-closes. If not, close manually.

6. **Report results**
   - Output summary:
     ```
     ✅ Branch: issue/<number>-<slug>
     🔗 PR URL: <link>
     🧪 Tests: All passed
     ```
   - If blocked (no small issues), prompt user for next action.

## Definition of Done
- PR opened and linked to chosen issue.
- All tests pass.
- Issue remains open (or auto-linked) awaiting merge.

## Follow-ups
- After merge, run `/project:commit` if local commits pending.
- If new tasks arise, create via `/project:create_general_task`.