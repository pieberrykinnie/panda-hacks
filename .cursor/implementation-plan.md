# StudyStreak – Implementation Plan

> Follow Conventional Commits. After **every** commit, append a short entry to `.cursor/logs.md` (date, commit header, 1-sentence outcome). When logs exceed ~120 lines, condense older entries into weekly summaries to keep the file lightweight.

---

## Phase 0 – Project Bootstrap

| Seq | Commit Message (type:scope) | Description | Tests / Docs |
|---|---|---|---|
| 0.1 | chore:root initialize pnpm monorepo skeleton | Create `studystreak/` workspace, configure `package.json` workspaces & basic `.editorconfig`, `.gitignore`. | N/A |
| 0.2 | docs:root add initial README & architecture diagram | Copy proposal diagrams + quick-start commands. | doc build passes |
| 0.3 | chore:ci add GitHub Actions lint/test pipeline | ESLint, Ruff, Pytest, Playwright; matrix across web/api. | workflow executes green |

## Phase 1 – Core Infrastructure

| Seq | Commit Message | Description | Tests / Docs |
|---|---|---|---|
| 1.1 | chore:api scaffold FastAPI service | `services/api` with health endpoint, Poetry, Ruff. | Pytest health test |
| 1.2 | chore:agent scaffold LangGraph agent service | Minimal planner flow stub; connects to OpenAI via env var. | stub unit test |
| 1.3 | feat:infra configure Supabase & Fly deploy files | SQL schema: users, plans, streaks. Terraform + Fly.toml. | Supabase migration CI |
| 1.4 | chore:docker add dev containers | `docker/` for api & agent using slim images. | container builds in CI |
| 1.5 | docs:infra add environment setup guide | `.cursor/setup.md` placeholder for variables & commands. | N/A |

## Phase 2 – Authentication & Data Layer

| Seq | Commit | Description | Tests |
|---|---|---|---|
| 2.1 | feat:web implement Supabase Auth (email) | Login / sign-up pages in `apps/web`. shadcn/ui components. | Playwright auth flow |
| 2.2 | feat:api add JWT validation middleware | Protect /api routes with Supabase JWT. | Pytest auth guard |
| 2.3 | feat:api create plan CRUD endpoints | `/plans` POST, GET. | Pytest CRUD |
| 2.4 | test:db seed test fixtures | Factory Boy scripts for plans, streaks. | CI ready |
| 2.5 | docs:db update schema diagrams | Mermaid ERD. | docs |

## Phase 3 – Agentic Planner MVP

| Seq | Commit | Description | Tests |
|---|---|---|---|
| 3.1 | feat:agent implement study-plan functions | Parse syllabus, constraints → schedule JSON. | Unit test deterministic sample |
| 3.2 | feat:agent integrate Google Calendar actions | Function calls create/update events. | Mock GCal tests |
| 3.3 | feat:web add plan creation wizard | Multi-step form; POST to `/plans`. | Playwright happy path |
| 3.4 | feat:web show calendar-synced dashboard | Fetch streak metrics WebSocket. | Cypress visual diff |

## Phase 4 – Gamification & Streak Engine

| Seq | Commit | Description | Tests |
|---|---|---|---|
| 4.1 | feat:api implement streak algorithm service | “Counting-Days” logic in background task. | Unit edge cases |
| 4.2 | feat:web render leaderboard & avatars | Lottie animations. | Playwright leaderboards |
| 4.3 | perf:api cache streak calculations | Redis layer. | Benchmarks |

## Phase 5 – Vision Quiz & AR Cards

| Seq | Commit | Description | Tests |
|---|---|---|---|
| 5.1 | feat:api upload endpoint for textbook images | S3 presigned POST. | Pytest upload |
| 5.2 | feat:agent generate quiz from image using GPT-4o vision | Store Q-A set. | Unit with sample image |
| 5.3 | feat:web quiz player component | Flashcard-style UI. | Playwright quiz |
| 5.4 | feat:web AR study card viewer (Three.js) | Render GLTF models via WebXR. | Manual demo + snapshot |

## Phase 6 – Teacher Dashboard & Peer Pods

| Seq | Commit | Description | Tests |
|---|---|---|---|
| 6.1 | feat:lowcode publish Retool template | Data source configs + permission roles. | Retool unit tests |
| 6.2 | feat:agent matching algorithm for peer pods | Complementary weakness matching. | Unit algorithm |
| 6.3 | feat:web pods chat room skeleton | Socket.io rooms. | Playwright chat |

## Phase 7 – Offline & Edge Mode

| Seq | Commit | Description | Tests |
|---|---|---|---|
| 7.1 | chore:edge integrate Ollama Mistral container | Start/stop script. | Container health test |
| 7.2 | feat:agent fallback planning on-device | Detect offline; use local LLM. | Integration test plane-mode |
| 7.3 | perf:mobile enable local caching & sync | Expo SQLite. | Detox tests |

## Phase 8 – Polish & Presentation Assets

| Seq | Commit | Description | Tests / Docs |
|---|---|---|---|
| 8.1 | docs:presentation add script & storyboard | `.cursor/script.md` first draft. | md-lint |
| 8.2 | chore:assets add demo data & screenshots | `demo/` folder. | N/A |
| 8.3 | style:web final UI polish pass | Colors, fonts, dark-mode toggle. | Percy snapshots |
| 8.4 | test:e2e add full regression suite | Playwright across major flows. | CI green |
| 8.5 | refactor:root tidy import paths & types | ts-config path aliases. | tsc clean |
| 8.6 | docs:root update README with setup & usage | Final readme. | md-lint |

---

## Logging Protocol (`.cursor/logs.md`)
1. **After each commit** run: `scripts/log.sh "<commit-msg>"` which appends:
   ```
   2025-07-17 | feat:web add plan creation wizard – implemented multi-step form
   ```
2. When the file grows beyond ~120 lines, collapse the oldest week into one summarized bullet list.
3. Always push condensed logs alongside code so `git log` + `.cursor/logs.md` remain aligned.

---

## Deliverable Burndown
- Total planned commits: ~45
- MVP ready by Phase 3 / Commit 3.4
- Demo polish finished by Phase 8 / Commit 8.3

> Stay disciplined: small, test-covered commits, thorough logs, and frequent pushes will maximize scoring on *Execution* and *Presentation* criteria.