# StudyStreak Monorepo

A privacy-first, agentic, gamified study companion for high-school students. Built for Panda Hacks 2025.

## Overview
StudyStreak helps students build effective study habits through personalized planning, spaced-practice streaks, and engaging game mechanics. It features an agentic AI planner, AR/vision flashcards, peer pods, and teacher dashboards.

## Monorepo Structure
```
studystreak/
  apps/        # Frontend (web/mobile)
  services/    # API, agent, background jobs
  packages/    # Shared UI/components/utils
  infra/       # Docker, Terraform, IaC
  tests/       # E2E and integration tests
```

## System Flow Diagram
```mermaid
flowchart TD
    subgraph Student Device (PWA/Mobile)
        A[Student sets goal] --> B[StudyStreak PWA]
    end
    B -->|call| C[FastAPI /api]
    C -->|invoke| D[LangGraph Study Agent]
    D -->|create events| E[Google Calendar]
    D -->|store plan| F[Supabase]
    B -->|sync| F
    subgraph Optional Offline
        B -- local LLM --> G[Mistral-7B via Ollama]
    end
    D -->|push| H[WebSocket Streak Service]
    H --> B
```

## Quick Start
1. Install dependencies: `pnpm install` (Node), `uv pip install -r requirements.txt` (Python)
2. See each package/README.md for setup and usage.

## License
MIT (see LICENSE)
