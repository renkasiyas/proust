"""
ABOUTME: Pytest configuration and shared fixtures for Proust Framework tests.
ABOUTME: Provides common test utilities, temporary directories, and mock setups.
"""

import pytest
import tempfile
from pathlib import Path
from unittest.mock import patch
from typing import Generator, Dict, List, Optional, Any

from src.proust.core import ProustFramework
from src.proust.installer import FrameworkInstaller


@pytest.fixture
def temp_dir() -> Generator[Path, None, None]:
    """Provide a temporary directory for testing."""
    with tempfile.TemporaryDirectory() as tmp_dir:
        yield Path(tmp_dir)


@pytest.fixture
def project_dir(temp_dir: Path) -> Path:
    """Create a temporary project directory."""
    project_path = temp_dir / "test_project"
    project_path.mkdir()
    return project_path


@pytest.fixture
def external_dir(temp_dir: Path) -> Path:
    """Create a temporary external directory."""
    external_path = temp_dir / "external_proust"
    external_path.mkdir()
    return external_path


@pytest.fixture
def mock_framework(project_dir: Path) -> ProustFramework:
    """Create a ProustFramework instance for testing."""
    return ProustFramework(str(project_dir))


@pytest.fixture
def mock_installer(project_dir: Path) -> FrameworkInstaller:
    """Create a FrameworkInstaller instance for testing."""
    return FrameworkInstaller(str(project_dir))


@pytest.fixture
def mock_download() -> Generator:
    """Mock the file download functionality."""
    with patch("src.proust.installer.urllib.request.urlretrieve") as mock:
        mock.return_value = None
        yield mock


@pytest.fixture
def sample_files(project_dir: Path) -> Dict[str, Path]:
    """Create sample framework files for testing."""
    proust_dir = project_dir / ".proust"
    simone_dir = project_dir / ".simone"

    # Create directories
    proust_dir.mkdir(parents=True, exist_ok=True)
    simone_dir.mkdir(parents=True, exist_ok=True)
    (proust_dir / "commands" / "simone").mkdir(parents=True, exist_ok=True)

    # Create sample files
    files = {
        "ethos": proust_dir / "ethos.md",
        "universal_claude": proust_dir / "universal_claude.md",
        "guardrails": proust_dir / "guardrails.yml",
        "brand": proust_dir / "brand.yml",
        "manifest": simone_dir / "00_PROJECT_MANIFEST.md",
        "claude_md": simone_dir / "CLAUDE.MD",
        "readme": simone_dir / "README.md",
        "command": proust_dir / "commands" / "simone" / "test_command.md",
    }

    # Write sample content
    for name, file_path in files.items():
        file_path.parent.mkdir(parents=True, exist_ok=True)
        file_path.write_text(f"Sample {name} content")

    return files


@pytest.fixture
def cli_runner() -> object:
    """Provide a CLI test runner."""
    from click.testing import CliRunner

    return CliRunner()


class MockUrlretrieve:
    """Mock class for urllib.request.urlretrieve."""

    def __init__(self, fail_files: Optional[List[str]] = None) -> None:
        self.fail_files = fail_files or []
        self.downloaded_files: List[tuple] = []

    def __call__(self, url: str, local_path: Path) -> None:
        """Mock urlretrieve behavior."""
        self.downloaded_files.append((url, local_path))

        # Extract filename from URL
        filename = url.split("/")[-1]

        if any(fail_file in url for fail_file in self.fail_files):
            raise Exception(f"Mock download failure for {filename}")

        # Create the file with mock content
        local_path.parent.mkdir(parents=True, exist_ok=True)
        local_path.write_text(f"Mock content for {filename}")


@pytest.fixture
def mock_successful_download(monkeypatch: Any) -> MockUrlretrieve:
    """Mock successful file downloads."""
    mock = MockUrlretrieve()
    monkeypatch.setattr("src.proust.installer.urllib.request.urlretrieve", mock)
    return mock


@pytest.fixture
def mock_failed_download(monkeypatch: Any) -> MockUrlretrieve:
    """Mock failed file downloads."""
    mock = MockUrlretrieve(fail_files=["ethos.md", "brand.yml"])
    monkeypatch.setattr("src.proust.installer.urllib.request.urlretrieve", mock)
    return mock
