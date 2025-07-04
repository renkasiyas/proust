"""
Proust Framework installer for setting up projects.
"""

import shutil
from pathlib import Path
from typing import Optional
import importlib.resources


class FrameworkInstaller:
    """Installer for Proust Framework files."""

    def __init__(
        self, project_root: str = ".", external_location: Optional[str] = None
    ):
        """Initialize installer for given project root."""
        self.project_root = Path(project_root).resolve()
        self.external_location = external_location

        if external_location:
            # Use external location for .proust directory
            self.proust_dir = Path(external_location).resolve() / ".proust"
            self.is_external = True
        else:
            # Use project root for .proust directory
            self.proust_dir = self.project_root / ".proust"
            self.is_external = False

    def create_symlink(self) -> bool:
        """Create symlink in project root pointing to external .proust directory."""
        if not self.is_external:
            return True

        project_link = self.project_root / ".proust"

        # Check if link already exists
        if project_link.exists():
            if project_link.is_symlink():
                existing_target = project_link.resolve()
                if existing_target == self.proust_dir.resolve():
                    print("Symlink .proust already points to correct location")
                    return True
                else:
                    print(
                        f"Warning: .proust symlink exists but points to {existing_target}"
                    )
                    print(f"Expected: {self.proust_dir}")
                    return False
            else:
                print(
                    "Warning: .proust exists as a regular directory/file, cannot create symlink"
                )
                return False

        # Create the symlink
        try:
            project_link.symlink_to(self.proust_dir)
            print(f"✅ Created symlink: {project_link} -> {self.proust_dir}")
            return True
        except OSError as e:
            print(f"❌ Could not create .proust symlink: {e}")
            return False

    def copy_template(self, template: str = "minimal") -> bool:
        """Copy template files to .proust directory."""
        try:
            # Get the templates directory from the package
            if hasattr(importlib.resources, "files"):
                # Python 3.9+
                templates = (
                    importlib.resources.files("proust") / ".." / ".." / "templates"
                )
            else:
                # Python 3.8
                import pkg_resources  # type: ignore

                templates = Path(
                    pkg_resources.resource_filename("proust", "../../templates")
                )

            # Resolve to actual path
            templates = templates.resolve()

            # If running from source, templates might be in the project root
            if not templates.exists():
                # Try relative to this file
                templates = Path(__file__).parent.parent.parent / "templates"

            if not templates.exists():
                print(f"❌ Templates directory not found at {templates}")
                return False

            # Select template source
            if template == "minimal":
                template_dir = templates / "starters" / "minimal"
            elif template == "standard":
                template_dir = templates / "starters" / "standard"
            else:
                print(f"❌ Unknown template: {template}")
                return False

            if not template_dir.exists():
                print(f"❌ Template directory not found: {template_dir}")
                return False

            # Copy template files
            print(f"Copying {template} template files...")

            # Create base .proust directory
            self.proust_dir.mkdir(parents=True, exist_ok=True)

            # Copy all files from template
            for item in template_dir.rglob("*"):
                if item.is_file():
                    relative_path = item.relative_to(template_dir)
                    target_path = self.proust_dir / relative_path

                    # Create parent directories
                    target_path.parent.mkdir(parents=True, exist_ok=True)

                    # Copy file
                    shutil.copy2(item, target_path)
                    print(f"  ✓ {relative_path}")

            # Create additional directories that might not be in templates
            additional_dirs = [
                "commands/core",
                "commands/planning",
                "commands/workflow",
                "commands/analysis",
                "commands/meta",
                "workspace/assessments",
                "workspace/context",
                "workspace/reviews",
                "project/milestones",
                "project/sprints",
                "project/tasks",
                "project/decisions",
            ]

            for dir_path in additional_dirs:
                (self.proust_dir / dir_path).mkdir(parents=True, exist_ok=True)

            # Copy command files from src/.proust/commands if available
            src_commands = (
                Path(__file__).parent.parent.parent / "src" / ".proust" / "commands"
            )
            if src_commands.exists():
                print("Copying command files...")
                for cmd_file in src_commands.rglob("*.md"):
                    relative_path = cmd_file.relative_to(src_commands.parent)
                    target_path = self.proust_dir / relative_path
                    target_path.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(cmd_file, target_path)
                    print(f"  ✓ {relative_path}")

            return True

        except Exception as e:
            print(f"❌ Error copying template: {e}")
            return False

    def install_all(self, template: str = "minimal", force: bool = False) -> bool:
        """Install complete Proust framework."""
        # Check if already installed
        if self.proust_dir.exists() and not force:
            print(f"❌ .proust directory already exists at {self.proust_dir}")
            print("Use --force to overwrite existing installation")
            return False

        # Remove existing directory if force
        if force and self.proust_dir.exists():
            print(f"Removing existing .proust directory at {self.proust_dir}...")
            shutil.rmtree(self.proust_dir)

        print(f"Installing Proust framework with {template} template...")

        # Copy template files
        if not self.copy_template(template):
            return False

        # Create symlink if using external location
        if self.is_external:
            if not self.create_symlink():
                return False

        print("✅ Proust framework installed successfully!")
        return True
