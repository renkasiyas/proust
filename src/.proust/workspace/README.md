# Workspace Directory

This directory contains temporary and generated files created during development workflows. Files here are safe to delete and will be regenerated as needed.

## Directory Structure

```
workspace/
├── assessments/        # Code analysis results
├── reviews/           # Review outputs and reports
├── context/           # Generated context files
└── README.md         # This file
```

## Usage

### assessments/
Contains outputs from `/project:analyze_codebase` and related analysis commands:
- Architecture analysis reports
- Code quality assessments
- Dependency analysis
- Security scan results
- Performance profiling data

### reviews/
Stores results from review commands:
- Code review summaries from `/project:code_review`
- Project review reports from `/project:project_review`
- Testing analysis from `/project:testing_review`
- Consistency audit results from `/project:consistency_audit`

### context/
Temporary context files generated during command execution:
- Aggregated context for complex commands
- Intermediate analysis results
- Command execution logs
- Debug information

## File Lifecycle

### Automatic Generation
Files in workspace/ are created automatically by commands as needed:
```bash
/project:analyze_codebase
# Creates: workspace/assessments/codebase_analysis_2024-12-27.md

/project:code_review
# Creates: workspace/reviews/code_review_M01_S01_T01.md

/project:do_task -t M01_S01_T01 --debug
# Creates: workspace/context/task_context_M01_S01_T01.yml
```

### Automatic Cleanup
- Files older than 30 days are automatically removed
- Command outputs are archived after sprint completion
- Debug files are cleaned up after successful task completion

### Manual Management
```bash
# Clean all workspace files
rm -rf workspace/{assessments,reviews,context}/*

# Clean only old files (7+ days)
find workspace/ -name "*.md" -mtime +7 -delete

# Archive current sprint's workspace
tar -czf workspace_M01_S01.tar.gz workspace/
```

## .gitignore Integration

Workspace files should be excluded from version control:
```gitignore
# Proust Framework workspace
.proust/workspace/
```

## Security Note

Workspace files may contain:
- Code analysis that reveals architectural patterns
- Review comments with sensitive context
- Debug information with system details

**Never commit workspace/ contents to public repositories.**

## Command Integration

Commands use workspace/ for:

### Intermediate Processing
- Breaking down complex analysis into steps
- Storing temporary context during multi-step operations
- Caching expensive analysis results

### Human Review
- Generating reports for human consumption
- Creating reviewable summaries of AI analysis
- Providing audit trails for decisions

### Debug Information
- Capturing context loading details
- Logging command execution steps
- Recording AI reasoning processes

This workspace enables powerful command functionality while keeping the core project structure clean and focused.