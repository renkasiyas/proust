"""
Core Proust Framework functionality.
"""

from pathlib import Path
from typing import Dict, List, Optional


class ProustFramework:
    """Main Proust Framework class for managing AI context and project memory."""

    def __init__(
        self, project_root: str = ".", external_location: Optional[str] = None
    ):
        """Initialize Proust Framework in the given project root."""
        self.project_root = Path(project_root).resolve()

        if external_location:
            # Use external location for .proust directory
            self.proust_dir = Path(external_location).resolve() / ".proust"
        else:
            # Check if .proust in project root is a symlink
            project_proust = self.project_root / ".proust"
            if project_proust.exists() and project_proust.is_symlink():
                # Follow symlink to actual location
                self.proust_dir = project_proust.resolve()
            else:
                # Use project root
                self.proust_dir = project_proust

    def is_using_symlink(self) -> bool:
        """Check if the framework directory is symlinked."""
        project_proust = self.project_root / ".proust"
        return project_proust.is_symlink()

    def is_initialized(self) -> bool:
        """Check if Proust framework is initialized in the project."""
        return (
            self.proust_dir.exists()
            and (self.proust_dir / "core").exists()
            and (self.proust_dir / "core" / "ethos.md").exists()
        )

    def get_commands(self) -> Dict[str, List[str]]:
        """Get list of available Proust commands organized by category."""
        commands_dir = self.proust_dir / "commands"
        if not commands_dir.exists():
            return {}

        commands = {}

        # Scan each category directory
        for category_dir in commands_dir.iterdir():
            if category_dir.is_dir() and not category_dir.name.startswith("."):
                category_commands = []
                for file in category_dir.glob("*.md"):
                    if file.name != "README.md":
                        category_commands.append(file.stem)

                if category_commands:
                    commands[category_dir.name] = sorted(category_commands)

        return commands

    def get_command_path(self, command: str) -> Optional[Path]:
        """Get path to a specific command file."""
        commands_dir = self.proust_dir / "commands"
        if not commands_dir.exists():
            return None

        # Search in all category directories
        for category_dir in commands_dir.iterdir():
            if category_dir.is_dir():
                command_path = category_dir / f"{command}.md"
                if command_path.exists():
                    return command_path

        return None

    def get_project_manifest(self) -> Optional[Path]:
        """Get path to project manifest file."""
        manifest_path = self.proust_dir / "project" / "manifest.yml"
        return manifest_path if manifest_path.exists() else None

    def get_ethos(self) -> Optional[Path]:
        """Get path to ethos file."""
        ethos_path = self.proust_dir / "core" / "ethos.md"
        return ethos_path if ethos_path.exists() else None

    def validate_framework(self) -> Dict[str, List[str]]:
        """Validate framework integrity and return issues."""
        issues: Dict[str, List[str]] = {
            "critical": [],
            "high": [],
            "medium": [],
            "low": [],
        }

        # Check core directory exists
        core_dir = self.proust_dir / "core"
        if not core_dir.exists():
            issues["critical"].append("Missing core/ directory")
            return issues  # Can't check further without core

        # Check essential core files
        core_files = {
            "ethos.md": "critical",
            "guardrails.yml": "high",
            "brand.yml": "medium",
            "architecture.yml": "medium",
        }

        for file, severity in core_files.items():
            if not (core_dir / file).exists():
                issues[severity].append(f"Missing core file: core/{file}")

        # Check project directory structure
        project_dir = self.proust_dir / "project"
        if not project_dir.exists():
            issues["high"].append("Missing project/ directory")
        else:
            # Check project subdirectories
            project_subdirs = ["milestones", "sprints", "tasks", "decisions"]
            for subdir in project_subdirs:
                if not (project_dir / subdir).exists():
                    issues["medium"].append(
                        f"Missing project subdirectory: project/{subdir}/"
                    )

            # Check project manifest
            if not (project_dir / "manifest.yml").exists():
                issues["high"].append("Missing project manifest: project/manifest.yml")

        # Check commands directory
        commands_dir = self.proust_dir / "commands"
        if not commands_dir.exists():
            issues["high"].append("Missing commands/ directory")
        else:
            # Check for at least one command category
            has_commands = False
            for category_dir in commands_dir.iterdir():
                if category_dir.is_dir() and any(category_dir.glob("*.md")):
                    has_commands = True
                    break

            if not has_commands:
                issues["medium"].append("No command files found in commands/ directory")

        # Check workspace directory
        workspace_dir = self.proust_dir / "workspace"
        if not workspace_dir.exists():
            issues["low"].append("Missing workspace/ directory")

        return issues
