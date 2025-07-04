# Proust Framework

*"In reality, every reader is, while reading, the reader of his own self."* — Marcel Proust

A Python package that installs structured project templates and commands to maintain persistent AI context across development sessions.

> **⚠️ EXPERIMENTAL ALPHA SOFTWARE**
>
> This is a highly experimental, work-in-progress alpha package. Expect:
> - **Breaking changes** between any versions
> - **Incomplete features** and missing functionality
> - **API instability** - commands and structure may change drastically
> - **Limited documentation** - many features are still being designed
> - **No upgrade path** - updates may require complete reinstallation
>
> This package is under active development and is not ready for production use.
> Use at your own risk and expect to adapt to significant changes.

## What is Proust?

Proust is a CLI tool that sets up standardized project structure for AI-assisted development. It creates consistent directory layouts, configuration files, and command templates that help AI assistants maintain context and follow project-specific guidelines.

**Core Components:**
- **Python CLI**: Install, validate, and manage project structures
- **Project Templates**: Consistent layouts for `.proust/` directories
- **Command System**: Structured workflows for development tasks
- **Validation Framework**: Ensure project integrity and completeness

## Installation

Install the Proust Framework using pip or uv:

```bash
# Using uv (recommended)
uv tool install proust-framework
proust install

# Using pip
pip install proust-framework
proust install

# Or run without installing
uv run --with proust-framework proust install
```

## Quick Start

1. **Install the CLI**: `uv tool install proust-framework`
2. **Initialize project**: `proust install` (creates `.proust/` directory structure)
3. **Check status**: `proust status` (validates installation)
4. **Use templates**: Copy from `templates/` directory as needed

## CLI Commands

### Core Commands
```bash
# Install framework structure
proust install [--external-location DIR]

# Check framework health
proust status

# Validate project integrity
proust validate

# Show available commands
proust commands

# Display version info
proust --version
```

### Installation Options
```bash
# Standard installation (current directory)
proust install

# External/shared configuration
proust install --external-location ~/shared-ai-config

# Force reinstall
proust install --force
```

## Project Structure

After installation, Proust creates this structure:

```
your-project/
└── .proust/           # AI memory and context (symlinked if external)
    ├── core/          # Project identity and configuration
    │   ├── ethos.md           # Project philosophy
    │   ├── architecture.yml   # Technical decisions
    │   ├── guardrails.yml     # AI behavior rules
    │   └── brand.yml          # Design guidelines
    ├── project/       # Project management structure
    │   ├── manifest.yml       # Central project state
    │   ├── milestones/        # Major project phases
    │   ├── sprints/           # Development iterations
    │   ├── tasks/             # Individual work items
    │   └── decisions/         # Architecture decision records
    ├── commands/      # Structured workflow templates
    │   ├── core/              # Framework management
    │   ├── planning/          # Project planning workflows
    │   ├── workflow/          # Daily development commands
    │   ├── analysis/          # Project assessment tools
    │   └── meta/              # Framework introspection
    ├── workspace/     # Temporary files and scratch space
    └── templates/     # Reference examples and starters
        ├── examples/          # Complete project examples
        └── starters/          # Starting templates
```

## Key Features

- 🏗️ **Structured Setup** - Consistent project layout across teams
- 📋 **Template System** - Ready-to-use project configurations
- ✅ **Validation** - Ensure project integrity and completeness
- 🔗 **External Configs** - Share configurations across multiple projects
- 🧩 **Extensible** - Add custom templates and commands
- ⚡ **Fast CLI** - Quick installation and status checking

## Template System

### Starters (for new projects)
```bash
# Copy minimal starter
cp -r templates/starters/minimal/* ./.proust/

# Copy full-featured starter
cp -r templates/starters/standard/* ./.proust/
```

### Examples (for learning)
- `templates/examples/webapp_project/` - Simple web app configuration
- `templates/examples/fake_project/` - Enterprise-scale example

### Customization
1. Replace `{{PLACEHOLDER}}` values with project-specific content
2. Update `core/ethos.md` with project philosophy
3. Modify `project/manifest.yml` with current state
4. Remove template instructions and TODOs

## External Configuration

Share configurations across multiple projects:

```bash
# Create shared configuration directory
mkdir ~/shared-ai-config

# Install with external location
cd project-1/
proust install --external-location ~/shared-ai-config

cd ../project-2/
proust install --external-location ~/shared-ai-config
```

Both projects will symlink to the same `.proust/` configuration, enabling consistent AI behavior and guidelines across all your work.

## Usage Examples

### Basic Project Setup
```bash
# Install framework
proust install

# Customize with minimal template
cp -r templates/starters/minimal/* ./.proust/

# Check everything is working
proust status
```

### Shared Team Configuration
```bash
# Team lead creates shared config
proust install --external-location ~/team-ai-standards

# Team members use shared config
proust install --external-location ~/team-ai-standards

# Updates to shared config affect all projects
```

### Validation and Health Checks
```bash
# Check project integrity
proust validate

# Show available commands
proust commands

# Display installation details
proust status
```

## Documentation

- **[Test Suite](tests/README.md)** - Comprehensive test documentation
- **[Templates](templates/README.md)** - Template system guide
- **[Command Reference](docs/command-execution.md)** - Command execution model
- **[Status Values](docs/status-values.md)** - Project status definitions
- **[Claude Integration](docs/claude-integration.md)** - Claude Code integration

## Development

### Running Tests
```bash
# Install development dependencies
uv sync

# Run test suite
make test

# Run with coverage
make test-html
```

### Building Package
```bash
# Build package
uv build

# Install locally for testing
uv tool install -e .
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make changes with tests
4. Submit a pull request

Focus on:
- Python package functionality
- CLI usability improvements
- Template quality and completeness
- Documentation clarity

## License

MIT License - See [LICENSE](LICENSE) for details.

## Package Information

- **Version:** 0.3.2
- **Python Support:** 3.8+
- **Repository:** https://github.com/renkasiyas/proust
- **PyPI:** https://pypi.org/project/proust-framework/
- **Dependencies:** click, pyyaml, requests

## Acknowledgments

See [ACKNOWLEDGMENTS.md](ACKNOWLEDGMENTS.md) for attribution and inspiration.

---

*"In reality, every reader is, while reading, the reader of his own self."* — Marcel Proust