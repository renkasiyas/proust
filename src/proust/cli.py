"""
Command line interface for Proust Framework.
"""

import click
from .core import ProustFramework
from .installer import FrameworkInstaller
from . import __version__


@click.group()
@click.version_option(version=__version__, package_name="proust-framework")
def main() -> None:
    """Proust Framework - AI Memory & Context Archivist"""
    pass


@main.command()
@click.option("--project-root", default=".", help="Project root directory")
@click.option(
    "--external-location",
    help="External location for .proust directory (creates symlink in project)",
)
@click.option(
    "--template",
    type=click.Choice(["minimal", "standard"]),
    default="minimal",
    help="Template to use for initialization",
)
@click.option(
    "--force",
    is_flag=True,
    help="Force installation even if .proust already exists",
)
def install(
    project_root: str, external_location: str, template: str, force: bool
) -> None:
    """Install Proust framework in the current or specified project."""
    installer = FrameworkInstaller(project_root, external_location)

    if installer.install_all(template=template, force=force):
        click.echo("🎉 Proust framework installed successfully!")
        click.echo("📁 Created .proust/ directory structure")
        click.echo("🚀 Run 'proust status' to verify installation")
        click.echo("📝 Edit .proust/core/ethos.md to define your project philosophy")
    else:
        click.echo("❌ Installation failed. See errors above.")
        raise click.Abort()


@main.command()
@click.option("--project-root", default=".", help="Project root directory")
@click.option(
    "--external-location",
    help="External location for .proust directory (creates symlink in project)",
)
def status(project_root: str, external_location: str) -> None:
    """Check Proust framework status in the project."""
    framework = ProustFramework(project_root, external_location)

    if framework.is_initialized():
        click.echo("✅ Proust framework is initialized")

        # Show available commands
        commands = framework.get_commands()
        if commands:
            total_commands = sum(len(cmds) for cmds in commands.values())
            click.echo(f"📋 Available commands: {total_commands}")
            for category, cmds in commands.items():
                if cmds:
                    click.echo(f"  {category}: {len(cmds)} commands")
        else:
            click.echo("⚠️  No commands found")

        # Show validation issues
        issues = framework.validate_framework()
        total_issues = sum(len(issues[level]) for level in issues)

        if total_issues > 0:
            click.echo(f"⚠️  Found {total_issues} validation issues:")
            for level, issue_list in issues.items():
                if issue_list:
                    click.echo(f"  {level.upper()}:")
                    for issue in issue_list:
                        click.echo(f"    - {issue}")
        else:
            click.echo("✅ Framework validation passed")
    else:
        click.echo("❌ Proust framework is not initialized")
        click.echo("Run 'proust install' to set up the framework")


@main.command()
@click.option("--project-root", default=".", help="Project root directory")
@click.option(
    "--external-location",
    help="External location for .proust directory (creates symlink in project)",
)
def commands(project_root: str, external_location: str) -> None:
    """List available Proust commands."""
    framework = ProustFramework(project_root, external_location)

    if not framework.is_initialized():
        click.echo("❌ Proust framework is not initialized")
        click.echo("Run 'proust install' to set up the framework")
        return

    if commands := framework.get_commands():
        total_commands = sum(len(cmds) for cmds in commands.values())
        click.echo(f"📋 Available Proust commands ({total_commands}):")
        for category, cmds in sorted(commands.items()):
            if cmds:
                click.echo(f"\n  {category}:")
                for cmd in cmds:
                    click.echo(f"    - {cmd}")
    else:
        click.echo("No commands found")


@main.command()
@click.argument("command")
@click.option("--project-root", default=".", help="Project root directory")
@click.option(
    "--external-location",
    help="External location for .proust directory (creates symlink in project)",
)
def show(command: str, project_root: str, external_location: str) -> None:
    """Show details of a specific Proust command."""
    framework = ProustFramework(project_root, external_location)

    if not framework.is_initialized():
        click.echo("❌ Proust framework is not initialized")
        return

    command_path = framework.get_command_path(command)
    if not command_path:
        click.echo(f"❌ Command '{command}' not found")
        return

    try:
        with open(command_path, "r") as f:
            content = f.read()
        click.echo(content)
    except Exception as e:
        click.echo(f"❌ Error reading command file: {e}")


@main.command()
@click.option("--project-root", default=".", help="Project root directory")
@click.option(
    "--external-location",
    help="External location for .proust directory (creates symlink in project)",
)
def validate(project_root: str, external_location: str) -> None:
    """Validate Proust framework integrity."""
    framework = ProustFramework(project_root, external_location)

    if not framework.is_initialized():
        click.echo("❌ Proust framework is not initialized")
        return

    issues = framework.validate_framework()
    total_issues = sum(len(issues[level]) for level in issues)

    if total_issues == 0:
        click.echo("✅ Framework validation passed")
        return

    click.echo(f"Found {total_issues} validation issues:")

    for level, issue_list in issues.items():
        if issue_list:
            click.echo(f"\n{level.upper()} ({len(issue_list)} issues):")
            for issue in issue_list:
                click.echo(f"  - {issue}")


if __name__ == "__main__":
    main()
