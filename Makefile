# Proust Framework Test Suite Makefile

.PHONY: test test-unit test-integration test-cli test-symlink test-fast test-cov test-html help clean install-dev

# Default target
help:
	@echo "🧪 Proust Framework Test Suite"
	@echo ""
	@echo "Available test commands:"
	@echo "  make test              - Run all tests with coverage"
	@echo "  make test-unit         - Run unit tests only"
	@echo "  make test-integration  - Run integration tests only"
	@echo "  make test-cli          - Run CLI tests only"
	@echo "  make test-symlink      - Run symlink functionality tests"
	@echo "  make test-fast         - Run fast tests (exclude slow ones)"
	@echo "  make test-cov          - Run tests with detailed coverage report"
	@echo "  make test-html         - Run tests and generate HTML coverage report"
	@echo "  make test-watch        - Run tests in watch mode (reruns on file changes)"
	@echo "  make test-verbose      - Run tests with verbose output"
	@echo ""
	@echo "Development commands:"
	@echo "  make install-dev       - Install development dependencies"
	@echo "  make lint              - Run code linting"
	@echo "  make format            - Format code with black"
	@echo "  make type-check        - Run type checking with mypy"
	@echo "  make pre-commit        - Run pre-commit hooks"
	@echo "  make clean             - Clean up test artifacts"

# Install development dependencies
install-dev:
	@echo "📦 Installing development dependencies..."
	uv sync --extra dev

# Run all tests
test:
	@echo "🧪 Running all tests with coverage..."
	uv run pytest --cov=src --cov-report=term-missing

# Run unit tests only
test-unit:
	@echo "🔧 Running unit tests..."
	uv run pytest -m unit --cov=src --cov-report=term-missing

# Run integration tests only
test-integration:
	@echo "🔗 Running integration tests..."
	uv run pytest -m integration --cov=src --cov-report=term-missing

# Run CLI tests only
test-cli:
	@echo "💻 Running CLI tests..."
	uv run pytest -m cli --cov=src --cov-report=term-missing

# Run symlink functionality tests
test-symlink:
	@echo "🔗 Running symlink functionality tests..."
	uv run pytest -m symlink --cov=src --cov-report=term-missing

# Run fast tests (exclude slow ones)
test-fast:
	@echo "⚡ Running fast tests..."
	uv run pytest -m "not slow" --cov=src --cov-report=term-missing

# Run tests with detailed coverage
test-cov:
	@echo "📊 Running tests with detailed coverage..."
	uv run pytest --cov=src --cov-report=term-missing --cov-report=html:htmlcov
	@echo "📈 Coverage report available in htmlcov/index.html"

# Run tests and generate HTML coverage report
test-html:
	@echo "🌐 Running tests and generating HTML coverage report..."
	uv run pytest --cov=src --cov-report=html:htmlcov
	@echo "📊 HTML coverage report generated in htmlcov/index.html"

# Run tests in watch mode (requires pytest-watch)
test-watch:
	@echo "👀 Running tests in watch mode..."
	uv run ptw --runner "pytest --cov=src --cov-report=term-missing"

# Run tests with verbose output
test-verbose:
	@echo "📢 Running tests with verbose output..."
	uv run pytest -v --cov=src --cov-report=term-missing

# Run tests for specific file
test-file:
	@echo "📁 Running tests for specific file: $(FILE)"
	uv run pytest $(FILE) -v --cov=src --cov-report=term-missing

# Run specific test by name
test-name:
	@echo "🎯 Running specific test: $(NAME)"
	uv run pytest -k "$(NAME)" -v --cov=src --cov-report=term-missing

# Code quality commands
lint:
	@echo "🔍 Running linting..."
	uv run flake8 src/
	uv run ruff check src/

format:
	@echo "🎨 Formatting code..."
	uv run black src/ tests/
	uv run ruff format src/ tests/

type-check:
	@echo "🔍 Running type checking..."
	uv run mypy src/

pre-commit:
	@echo "🔒 Running pre-commit hooks..."
	uv run pre-commit run --all-files

# Clean up test artifacts
clean:
	@echo "🧹 Cleaning up test artifacts..."
	rm -rf .pytest_cache/
	rm -rf htmlcov/
	rm -rf .coverage
	rm -rf __pycache__/
	find . -name "*.pyc" -delete
	find . -name "__pycache__" -type d -exec rm -rf {} +
	@echo "✨ Cleanup complete!"

# Example usage targets
examples:
	@echo "📚 Example test commands:"
	@echo ""
	@echo "  # Run tests for a specific file:"
	@echo "  make test-file FILE=tests/test_core.py"
	@echo ""
	@echo "  # Run tests matching a specific name pattern:"
	@echo "  make test-name NAME='test_install'"
	@echo ""
	@echo "  # Run symlink tests with verbose output:"
	@echo "  make test-symlink && make test-verbose -k symlink"