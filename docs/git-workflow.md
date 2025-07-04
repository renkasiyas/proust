# Git Workflow Documentation

## Branch Strategy

This project follows a simple two-branch workflow:

- **main**: Production-ready releases with automated PyPI publishing
- **dev**: Development branch for ongoing work

## Development Process

### 1. Working on Features
```bash
# Start from dev branch
git checkout dev
git pull origin dev

# Create feature branch (optional for major features)
git checkout -b feature/your-feature-name

# Make changes and commit
git add .
git commit -m "Your commit message"
```

### 2. Merging to Main (Releases)
```bash
# Switch to main and merge dev
git checkout main
git merge dev --squash  # Squash all commits into one

# Commit with clean message (no co-authoring)
git commit -m "Release v0.x.x: Brief description of changes"
```

### 3. Automated Publishing
When code is pushed to main with changes to:
- `src/`
- `pyproject.toml`
- `README.md`
- `LICENSE`

GitHub Actions automatically:
1. Builds the package with `uv build`
2. Publishes to PyPI using stored `PYPI_API_TOKEN`

### 4. Tagging and Releases
```bash
# After successful merge to main
git tag v0.x.x
git push origin main --tags

# Create GitHub release (manual or automated)
gh release create v0.x.x --generate-notes
```

## Version Management

- Update version in `src/proust/__init__.py`
- Follow semantic versioning (MAJOR.MINOR.PATCH)
- Keep versions unified across all branches

## Commit Guidelines

- Use clean, descriptive commit messages
- No co-authoring for automated commits
- Squash commit history when merging to main
- Reference issues/PRs when applicable

## Repository Setup Requirements

### GitHub Secrets
- `PYPI_API_TOKEN`: PyPI token for automated publishing

### Protected Branches
- main: Require PR reviews for direct pushes (optional)
- dev: Allow direct pushes for development

## Testing Installation

```bash
# Test local installation
uv tool install proust-framework

# Verify CLI works
proust --help
proust install
```

## Emergency Procedures

### Rollback Release
```bash
# If a release is broken
git revert HEAD
git tag v0.x.x-hotfix
git push origin main --tags
```

### Manual PyPI Release
```bash
# If automated publishing fails
uv build
uv publish --token $PYPI_API_TOKEN
```