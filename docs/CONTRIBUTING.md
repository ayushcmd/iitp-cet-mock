# Git Workflow & Contributing Guide — IIT Patna CET Mock

This repository enforces strict Git hygiene, branching policies, and pull request workflows. All contributors and agents must follow these guidelines.

---

## 1. Repository Configuration

- **Repository Root**: `C:\Projects\AYUSHCMD-GITHUB\iitp-cet-mock`
- **Remote Origin**: `https://github.com/ayushcmd/iitp-cet-mock.git`
- **Default Branch**: `master`
- **Git Author**: `ayushcmd <ayush_24a12res897@iitp.ac.in>`

---

## 2. Branching Strategy

- **Direct commits to `master` are strictly prohibited.**
- Before starting any development task:
  1. Inspect the working tree (`git status`).
  2. Fetch remote changes (`git fetch origin`).
  3. Switch to default branch (`git checkout master`).
  4. Fast-forward from remote (`git pull --ff-only origin master`).
  5. Create a descriptive working branch:
     - Feature branches: `feat/<feature-name>` (e.g. `feat/academic-pages`, `feat/institutional-pages`)
     - Bug fixes: `fix/<issue-name>` (e.g. `fix/homepage-layout`)
     - Refactoring: `refactor/<scope>` (e.g. `refactor/shared-components`)
     - Documentation: `docs/<topic>` (e.g. `docs/git-workflow`)

---

## 3. Conventional Commits

All commit messages must adhere to the Conventional Commits standard describing actual modifications:

- `feat: add academic calendar and holiday pages`
- `feat: implement responsive semester timetables`
- `feat: add evaluation and re-examination schedules`
- `feat: build academic program and eligibility pages`
- `fix: correct nested-page navigation and asset paths`
- `docs: document academic page implementation`
- `test: verify nested-page navigation`

**Prohibited Messages**: Generic milestone messages such as `feat: phase 4 completed`, `chore: work done`, `update files`, or `final commit` are rejected.

---

## 4. Push & Pull Request Requirements

After each approved development batch:
1. Review all modifications via `git diff` and `git status`.
2. Run local tests (viewports 1440px, 1024px, 768px, 390px, 320px).
3. Confirm `.gitignore` excludes temporary, secret, or log files.
4. Commit changes on the active working branch.
5. Push the working branch to GitHub:
   ```bash
   git push -u origin <branch-name>
   ```
6. Open a Pull Request targeting `master` using the GitHub CLI (`gh pr create`).
7. The PR description must include:
   - Summary of implemented features
   - List of changed pages
   - Tests performed
   - Screenshots or visual comparisons
   - Known issues and review checklist

---

## 5. Merge Policy

- **Never merge Pull Requests automatically.**
- The repository owner (`ayushcmd`) reviews and merges PRs manually.
- Never force-push or rewrite shared history.
- After creating a PR, halt and wait for explicit owner confirmation and approval before starting the next batch.

---

## 6. Post-Merge Workflow

Once the repository owner confirms the PR is merged:
1. `git checkout master`
2. `git pull --ff-only origin master`
3. Verify local master is clean and up to date.
4. Branch off for the next approved milestone.
