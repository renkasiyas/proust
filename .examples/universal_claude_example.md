# CLAUDE.md – Proust Memory Archive Configuration

_Author: Development Team_
 _Date: 2025-07-03_

> **Purpose**  
> Provide Claude Code with baseline memory patterns for the Proust project.  
> This configuration ensures consistent development practices and quality standards.

---

## 1. Project Identity
| Field               | Your Value                        |
| ------------------- | --------------------------------- |
| `project_name`      | Proust Memory Archive             |
| `runtime_stack`     | Node.js + React                  |
| `primary_language`  | TypeScript                        |
| `maintainer_handle` | @proust-team                      |

---

## 2. Senior‑Engineer Task Protocol  

1. **Clarify Scope** – _Review requirements and architecture docs first_  
2. **Locate Insertion Point** – _Identify exact files and components to modify_  
3. **Apply Minimal Change** – _Only change what's necessary for the task_  
4. **Double‑Check** – _Run tests, verify no regressions introduced_  
5. **Deliver Clearly** – _Document changes and any new dependencies_

---

## 3. Universal Development Principles  

### Code Quality
- Use Prettier for formatting with project .prettierrc config
- Enable strict TypeScript mode with no implicit any
- Pin all dependencies to exact versions in package.json

### Architecture
- Reuse existing components from src/components/ before creating new ones
- Follow atomic design principles: atoms → molecules → organisms
- Keep business logic in service layer, not in React components
- Use established patterns for state management and data fetching

### Task Execution Rules
- No TODOs left behind unless documented in docs/TODO.md
- All new features require corresponding tests
- API changes require updating OpenAPI documentation

---

## 4. Team Relationship Notes  

- Address the human as **"Ren"**
- Relationship style: collaborative and direct
- Humor policy: welcome when appropriate, not during critical debugging

---

## 5. Testing Strategy
| Type        | Must Have? | Min Coverage |
| ----------- | ---------- | ------------ |
| Unit        | YES        | 80%          |
| Integration | YES        | 70%          |
| E2E         | YES        | Key flows    |

> Critical user flows must have E2E test coverage.

---

## 6. TDD Workflow
1. Write failing test that defines the desired behavior
2. Implement minimal code to make test pass
3. Refactor while keeping tests green
4. Repeat for each feature increment

---

## 7. Shell & Tooling Preferences
- Default shell: bash
- Package manager: npm (not yarn or pnpm)
- Run commands: `npm run dev`, `npm test`, `npm run build`

---

## 8. Prohibited Practices

```
- Using console.log in production code (use proper logging)
- Hardcoding API URLs or environment-specific values
- Skipping code review with --no-verify commits
- Modifying node_modules directly
- Creating components without corresponding tests
```

---

## 9. Getting Help
- Technical architecture questions: Check docs/ARCHITECTURE.md first
- Code patterns: Look at existing similar components
- Complex decisions: Create discussion issue on GitHub

---

## 10. Version Control Etiquette
- Branch naming pattern: `feature/short-description` or `fix/issue-description`
- Commit format: Conventional commits with type(scope): description
- All commits must pass CI checks before merging

---

## 11. Appendix / References
- Project manifest: `src/.proust/manifesto.yml`
- Design guidelines: `src/.proust/brand.yml`
- Coding standards: `src/.proust/guardrails.yml`
- Architecture documentation: `src/.simone/01_PROJECT_DOCS/ARCHITECTURE.md`

---

_This configuration was customized for the Proust Memory Archive on 2025-01-03._