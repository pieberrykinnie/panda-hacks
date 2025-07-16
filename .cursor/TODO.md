# Panda Hacks 2025 – Project TODO

> Reminder: After completing **each** numbered section, flush prior context tokens except for the information relevant to the next section, and update this checklist.

## 1. CREATE `.cursor/TODO.md`
- [ ] Ensure a `.cursor/` directory exists.
- [ ] Add this checklist to `.cursor/TODO.md`.
- [ ] Commit the file to version control.

## 2. INGEST HACKATHON DETAILS `.cursor/hackathon.md`
- [x] Extract and record all required details (name, problem statements, deliverables, judging criteria, prize categories, judges).
- [x] Save them to `.cursor/hackathon.md`.
- [x] Commit changes.

## 3. BRAINSTORM PROJECT IDEA `.cursor/brainstorm.md`
- [ ] Perform at least 10 distinct web searches (one per iteration) on potential project ideas.
- [ ] After each search, append findings under a new `## Iteration X` heading in `.cursor/brainstorm.md`.
- [ ] Ensure at least five feasible winning ideas are documented.
- [ ] Commit after completing all iterations.

## 4. FINALIZE PROJECT IDEA `.cursor/proposal.md`
- [ ] Draft a comprehensive project proposal following hackathon requirements.
- [ ] Include solution name, features, tech stack, project structure, flow diagrams, and future improvements.
- [ ] Commit the proposal.

## 5. GENERATE IMPLEMENTATION PLAN `.cursor/implementation-plan.md`
- [ ] Break the project into granular, Conventional-Commit-style steps with testing and documentation tasks.
- [ ] Reference `.cursor/logs.md` usage and condensation rules.
- [ ] Ensure plan culminates in a deployable application, ≤10 docs files, and error-free dev commands.
- [ ] Commit the implementation plan.

## 6. DEFINE DEVELOPMENT GUIDELINES `.cursorrules`
- [ ] Research and draft development rules (tools, commands, coding standards, env-management, etc.).
- [ ] Commit `.cursorrules`.

## 7. DEVELOP THE PROTOTYPE `.cursor/logs.md`
- [ ] Follow implementation plan and `.cursorrules` rigorously.
- [ ] Log progress to `.cursor/logs.md` after every step, condensing older logs as needed.
- [ ] Ensure `git log` mirrors the implementation plan exactly.

## 8. (OPTIONAL) CREATE SETUP GUIDELINES `.cursor/setup.md`
- [ ] If human intervention is needed (env vars, deployment), document steps in `.cursor/setup.md`.
- [ ] Commit the setup guide.

## 9. CREATE PRESENTATION SCRIPT `.cursor/script.md`
- [ ] Write a full presentation script aligned with hackathon deliverables.
- [ ] Build Marimo slides in `slides/` directory.
- [ ] Add TODOs for any external assets required.
- [ ] Commit both script and slides.

## 10. (OPTIONAL) FINISH UP RELATED DELIVERABLES
- [ ] Complete any additional required deliverables not covered above.
- [ ] Commit final additions.