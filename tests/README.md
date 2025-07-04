# Proust Framework Test Suite

A comprehensive test suite for the Proust Framework with multiple testing strategies and beautiful reporting.

## Test Structure

```
tests/
├── __init__.py                     # Test package initialization
├── conftest.py                     # Pytest configuration and fixtures
├── README.md                       # This file
├── features/                       # BDD-style feature tests
│   ├── test_installation_feature.py    # Installation scenarios
│   └── test_symlink_feature.py         # Symlink scenarios
├── test_cli.py                     # CLI command tests
├── test_core.py                    # ProustFramework class tests
├── test_installer.py               # FrameworkInstaller class tests
└── test_symlinks.py                # Symlink integration tests
```

## Test Categories

### 🔧 Unit Tests (`@pytest.mark.unit`)
- **Purpose**: Test individual components in isolation
- **Files**: `test_core.py`, `test_installer.py`
- **Coverage**: Core business logic, path resolution, validation
- **Speed**: Fast (< 1s each)

### 🔗 Integration Tests (`@pytest.mark.integration`)
- **Purpose**: Test component interactions and end-to-end workflows
- **Files**: `test_symlinks.py`, feature tests
- **Coverage**: Installation process, symlink creation, framework interaction
- **Speed**: Medium (1-5s each)

### 💻 CLI Tests (`@pytest.mark.cli`)
- **Purpose**: Test command-line interface and user interactions
- **Files**: `test_cli.py`
- **Coverage**: All CLI commands, parameter validation, error handling
- **Speed**: Medium (1-3s each)

### 🔗 Symlink Tests (`@pytest.mark.symlink`)
- **Purpose**: Test symlink functionality across platforms
- **Files**: `test_symlinks.py`, feature tests
- **Coverage**: External location detection, symlink creation, path resolution
- **Speed**: Medium (1-5s each)

### 🌐 Network Tests (`@pytest.mark.network`)
- **Purpose**: Test actual network operations (disabled by default)
- **Coverage**: Real file downloads, repository access
- **Speed**: Slow (5-30s each)

## Running Tests

### Quick Commands
```bash
# Run all tests
make test

# Run specific test categories
make test-unit
make test-integration
make test-cli
make test-symlink

# Run fast tests only
make test-fast

# Generate HTML coverage report
make test-html
```

### Advanced Usage
```bash
# Run tests with verbose output
uv run pytest -v

# Run specific test file
uv run pytest tests/test_core.py

# Run specific test by name pattern
uv run pytest -k "test_install"

# Run tests with coverage
uv run pytest --cov=src --cov-report=html

# Run tests in parallel (with pytest-xdist)
uv run pytest -n auto

# Run tests and stop on first failure
uv run pytest -x
```

## Test Scenarios (BDD Style)

### Installation Feature
- ✅ Basic installation in a new project
- ✅ Shared configuration installation with external location
- ✅ Installation with existing files (preservation)
- ✅ Installation status checking and validation
- ✅ Multiple projects sharing same configuration
- ✅ Installation failure handling

### Symlink Feature
- ✅ Developer shares AI prompts across projects
- ✅ Team lead creates shared coding standards
- ✅ Consultant uses portable AI configuration
- ✅ Commands work transparently with symlinks
- ✅ Broken symlink handling

## Fixtures and Utilities

### Core Fixtures
- `temp_dir`: Temporary directory for test isolation
- `project_dir`: Mock project directory
- `external_dir`: Mock external configuration directory
- `mock_framework`: ProustFramework instance for testing
- `mock_installer`: FrameworkInstaller instance for testing

### Mock Fixtures
- `mock_successful_download`: Simulates successful file downloads
- `mock_failed_download`: Simulates failed file downloads
- `sample_files`: Creates a complete framework structure for testing

### CLI Fixtures
- `cli_runner`: Click CLI test runner for command testing

## Test Configuration

### Pytest Settings
- **Test discovery**: Automatic discovery of `test_*.py` files
- **Markers**: Custom markers for test categorization
- **Coverage**: 80% minimum coverage requirement
- **Reporting**: HTML and terminal coverage reports

### Pre-commit Integration
- **Fast tests**: Run on every commit (`-m "not slow"`)
- **Unit tests**: Run on push (`-m unit`)
- **Quality checks**: Linting, formatting, type checking

### CI/CD Pipeline
- **Matrix testing**: Python 3.8-3.12 on Ubuntu, macOS, Windows
- **Parallel execution**: Different test categories run in parallel
- **Artifacts**: Test reports, coverage reports, security scans
- **Quality gates**: Coverage threshold, security checks

## Writing New Tests

### Test Naming Convention
```python
def test_[component]_[behavior]_[expected_outcome](fixtures):
    """Test description following Given-When-Then pattern."""
    # Given: Setup test conditions
    # When: Execute the action being tested
    # Then: Assert expected outcomes
```

### Test Categories
Mark your tests with appropriate markers:
```python
@pytest.mark.unit
def test_core_functionality():
    """Unit test for core functionality."""
    pass

@pytest.mark.integration
def test_end_to_end_workflow():
    """Integration test for complete workflow."""
    pass

@pytest.mark.symlink
def test_symlink_behavior():
    """Test symlink-specific functionality."""
    pass
```

### BDD-Style Feature Tests
Create feature tests in `tests/features/` following this pattern:
```python
class TestNewFeature:
    """
    Feature: Description of the feature
    As a [user type]
    I want to [goal]
    So that [benefit]
    """

    def test_scenario_descriptive_name(self, fixtures):
        """
        Scenario: Specific scenario description
        Given [initial condition]
        When [action]
        Then [expected outcome]
        And [additional assertions]
        """
        # Implementation
```

## Coverage Requirements

- **Minimum coverage**: 80%
- **Core modules**: 90%+ coverage expected
- **CLI commands**: All code paths tested
- **Error handling**: Exception paths covered
- **Edge cases**: Symlink edge cases, permission errors, network failures

## Troubleshooting

### Common Issues
1. **Symlink tests failing on Windows**: Some tests are skipped on Windows due to symlink limitations
2. **Permission errors**: Ensure test directories are writable
3. **Import errors**: Check that `src/` is in Python path
4. **Coverage too low**: Add tests for uncovered branches

### Debug Mode
```bash
# Run with debugging
uv run pytest --pdb

# Run with print statements
uv run pytest -s

# Run single test with verbose output
uv run pytest tests/test_core.py::TestProustFramework::test_specific_method -v
```

## Performance

- **Fast tests**: < 1 second each
- **Integration tests**: 1-5 seconds each
- **Full suite**: < 30 seconds on modern hardware
- **Parallel execution**: Scales with CPU cores

## Quality Metrics

- ✅ **Test Coverage**: 80%+ maintained
- ✅ **Test Speed**: Fast feedback loop
- ✅ **Test Reliability**: No flaky tests
- ✅ **Documentation**: All scenarios documented
- ✅ **Maintainability**: Clear, readable test code