# Proust Framework - Setup from URL

Set up the Proust Memory Archive framework in any project without cloning the repository.

## Quick Setup (One-liner)

```bash
curl -sSL https://raw.githubusercontent.com/renkasiyas/proust/main/SETUP_FROM_URL.md | bash -s -- setup
```

## Manual Setup Process

### 1. Download Framework Structure

```bash
# Create framework directories
mkdir -p src/.proust/commands/simone src/.proust/manifesto src/.simone/{01_PROJECT_DOCS,02_REQUIREMENTS,03_SPRINTS,04_GENERAL_TASKS,05_ARCHITECTURAL_DECISIONS,99_TEMPLATES} .examples

# Download core framework files
curl -o src/.proust/ethos.md https://raw.githubusercontent.com/renkasiyas/proust/main/src/.proust/ethos.md
curl -o src/.proust/universal_claude.md https://raw.githubusercontent.com/renkasiyas/proust/main/src/.proust/universal_claude.md
curl -o src/.proust/guardrails.yml https://raw.githubusercontent.com/renkasiyas/proust/main/src/.proust/guardrails.yml
curl -o src/.proust/brand.yml https://raw.githubusercontent.com/renkasiyas/proust/main/src/.proust/brand.yml
curl -o src/.proust/external_docs.yml https://raw.githubusercontent.com/renkasiyas/proust/main/src/.proust/external_docs.yml
curl -o src/.proust/manifesto/manifesto.yml https://raw.githubusercontent.com/renkasiyas/proust/main/src/.proust/manifesto/manifesto.yml

# Download Simone command structure
for cmd in analyze_codebase brainstorm code_review commit consistency_audit context_management create_general_task create_sprint_tasks create_sprints_from_milestone discuss_review do_task gh_do_issues initialize initialize_new_project prime project_review reflect_on_solution test testing_review yolo; do
  curl -o "src/.proust/commands/simone/${cmd}.md" "https://raw.githubusercontent.com/renkasiyas/proust/main/src/.proust/commands/simone/${cmd}.md"
done

# Download Simone project structure  
curl -o src/.simone/README.md https://raw.githubusercontent.com/renkasiyas/proust/main/src/.simone/README.md
curl -o src/.simone/CLAUDE.MD https://raw.githubusercontent.com/renkasiyas/proust/main/src/.simone/CLAUDE.MD

# Download templates
for template in adr_template milestone_meta_template project_manifest_template sprint_meta_template task_template; do
  curl -o "src/.simone/99_TEMPLATES/${template}.md" "https://raw.githubusercontent.com/renkasiyas/proust/main/src/.simone/99_TEMPLATES/${template}.md"
done

# Download examples
for example in README brand_example.yml ethos_example.md guardrails_example.yml manifesto_example.yml universal_claude_example.md; do
  curl -o ".examples/${example}" "https://raw.githubusercontent.com/renkasiyas/proust/main/.examples/${example}"
done

# Download documentation
curl -o README.md https://raw.githubusercontent.com/renkasiyas/proust/main/README.md
curl -o FRAMEWORK_README.md https://raw.githubusercontent.com/renkasiyas/proust/main/FRAMEWORK_README.md
curl -o TEMPLATE_GUIDE.md https://raw.githubusercontent.com/renkasiyas/proust/main/TEMPLATE_GUIDE.md
curl -o AUDIT_SUPER_PROMPT.md https://raw.githubusercontent.com/renkasiyas/proust/main/AUDIT_SUPER_PROMPT.md
```

### 2. Customize for Your Project

Replace template placeholders with your project values:

```bash
# Update project identity in core files
sed -i '' 's/{{PROJECT_NAME}}/YourProjectName/g' src/.proust/ethos.md
sed -i '' 's/{{COMPANY_NAME}}/YourCompany/g' src/.proust/ethos.md
sed -i '' 's/{{MAINTAINER_HANDLE}}/@yourusername/g' src/.proust/universal_claude.md

# Update technical stack in manifesto
sed -i '' 's/{{TECH_STACK}}/YourTechStack/g' src/.proust/manifesto/manifesto.yml
sed -i '' 's/{{DEPLOYMENT_TARGET}}/YourDeployment/g' src/.proust/manifesto/manifesto.yml
```

### 3. Initialize Project Structure

```bash
# Create your first project manifest
curl -o src/.simone/00_PROJECT_MANIFEST.md https://raw.githubusercontent.com/renkasiyas/proust/main/src/.simone/00_PROJECT_MANIFEST.md

# Add to git
git add src/.proust src/.simone .examples *.md
git commit -m "Add Proust Memory Archive framework

🤖 Generated with [Claude Code](https://claude.ai/code)

Co-Authored-By: Claude <noreply@anthropic.com>"
```

## Automated Setup Script

This setup can be automated with a single script:

```bash
#!/bin/bash
# setup-proust.sh - Automated Proust framework setup

if [ "$1" == "setup" ]; then
  echo "Setting up Proust Memory Archive framework..."
  
  # Create directory structure
  mkdir -p src/.proust/commands/simone src/.proust/manifesto src/.simone/{01_PROJECT_DOCS,02_REQUIREMENTS,03_SPRINTS,04_GENERAL_TASKS,05_ARCHITECTURAL_DECISIONS,99_TEMPLATES} .examples
  
  # Download all framework files
  BASE_URL="https://raw.githubusercontent.com/renkasiyas/proust/main"
  
  # Core framework files
  curl -sSL -o src/.proust/ethos.md "$BASE_URL/src/.proust/ethos.md"
  curl -sSL -o src/.proust/universal_claude.md "$BASE_URL/src/.proust/universal_claude.md"
  curl -sSL -o src/.proust/guardrails.yml "$BASE_URL/src/.proust/guardrails.yml"
  curl -sSL -o src/.proust/brand.yml "$BASE_URL/src/.proust/brand.yml"
  curl -sSL -o src/.proust/external_docs.yml "$BASE_URL/src/.proust/external_docs.yml"
  curl -sSL -o src/.proust/manifesto/manifesto.yml "$BASE_URL/src/.proust/manifesto/manifesto.yml"
  
  # Commands
  for cmd in analyze_codebase brainstorm code_review commit consistency_audit context_management create_general_task create_sprint_tasks create_sprints_from_milestone discuss_review do_task gh_do_issues initialize initialize_new_project prime project_review reflect_on_solution test testing_review yolo; do
    curl -sSL -o "src/.proust/commands/simone/${cmd}.md" "$BASE_URL/src/.proust/commands/simone/${cmd}.md"
  done
  
  # Simone structure
  curl -sSL -o src/.simone/README.md "$BASE_URL/src/.simone/README.md"
  curl -sSL -o src/.simone/CLAUDE.MD "$BASE_URL/src/.simone/CLAUDE.MD"
  curl -sSL -o src/.simone/00_PROJECT_MANIFEST.md "$BASE_URL/src/.simone/00_PROJECT_MANIFEST.md"
  
  # Templates
  for template in adr_template milestone_meta_template project_manifest_template sprint_meta_template task_template; do
    curl -sSL -o "src/.simone/99_TEMPLATES/${template}.md" "$BASE_URL/src/.simone/99_TEMPLATES/${template}.md"
  done
  
  # Examples
  for example in README.md brand_example.yml ethos_example.md guardrails_example.yml manifesto_example.yml universal_claude_example.md; do
    curl -sSL -o ".examples/${example}" "$BASE_URL/.examples/${example}"
  done
  
  # Documentation
  curl -sSL -o README.md "$BASE_URL/README.md"
  curl -sSL -o FRAMEWORK_README.md "$BASE_URL/FRAMEWORK_README.md"
  curl -sSL -o TEMPLATE_GUIDE.md "$BASE_URL/TEMPLATE_GUIDE.md"
  curl -sSL -o AUDIT_SUPER_PROMPT.md "$BASE_URL/AUDIT_SUPER_PROMPT.md"
  
  echo "✅ Proust framework installed successfully!"
  echo "📖 See FRAMEWORK_README.md to get started"
  echo "🔧 Customize templates in src/.proust/ for your project"
else
  echo "Usage: curl -sSL https://raw.githubusercontent.com/renkasiyas/proust/main/SETUP_FROM_URL.md | bash -s -- setup"
fi
```

## Verification

After setup, verify the framework is installed correctly:

```bash
# Check directory structure
find src/.proust src/.simone .examples -type f | wc -l
# Should show 40+ files

# Check core files exist
ls src/.proust/ethos.md src/.proust/universal_claude.md src/.simone/README.md

# Verify examples are available
ls .examples/
```

## Next Steps

1. **Customize Configuration**: Edit `src/.proust/ethos.md` and `src/.proust/manifesto/manifesto.yml` with your project details
2. **Review Examples**: Check `.examples/` directory for properly filled templates
3. **Initialize Project**: Create your first project manifest using Simone templates
4. **Start Using Commands**: Reference `src/.proust/commands/simone/` for available project management commands

---

_Last updated: 2025-01-03_