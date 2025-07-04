# Proust Framework Documentation

Documentation for the Proust Framework Python package and CLI tools.

## Package Documentation

### Core Features
- **[Command Execution](command-execution.md)** - How Proust commands work and execution model
- **[Status Values](status-values.md)** - Project and task status definitions used throughout the framework
- **[Claude Integration](claude-integration.md)** - Integration with Claude Code slash commands

### Development
- **[Git Workflow](git-workflow.md)** - Git integration patterns and workflows
- **[Framework Auditing](audit-super-prompt.md)** - Validation and integrity checking

## Quick Reference

### CLI Commands
```bash
proust install              # Install framework structure
proust status              # Check framework health
proust validate            # Validate project integrity
proust commands            # Show available commands
proust --version           # Display version info
```

### Key Directories
- `.proust/core/` - Project identity and configuration
- `.proust/project/` - Project management structure
- `.proust/commands/` - Structured workflow templates
- `.proust/workspace/` - Temporary files and scratch space
- `.proust/templates/` - Reference examples and starters

### Template System
- `templates/starters/` - Starting templates for new projects
- `templates/examples/` - Complete project examples for learning

## External Resources

- **[Main README](../README.md)** - Package overview and installation
- **[Test Suite](../tests/README.md)** - Comprehensive test documentation
- **[Templates Guide](../templates/README.md)** - Template system documentation
- **[Contributing Guidelines](../CONTRIBUTING.md)** - How to contribute to the project

## Getting Help

1. Check the relevant documentation file for your topic
2. Review examples in the `templates/` directory
3. Run `proust status` to validate your installation
4. Check the test suite for implementation examples

The documentation focuses on practical usage of the Python package and CLI tools.