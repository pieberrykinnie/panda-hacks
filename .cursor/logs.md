2025-07-17 | chore:root initialize pnpm monorepo skeleton – created studystreak/ workspace and base directories
2025-07-17 | docs:root add initial README & architecture diagram – added project overview and Mermaid system flowchart to studystreak/README.md
2025-07-17 | chore:api scaffold FastAPI service – FastAPI app with /health endpoint, uv, Ruff, and Pytest configured
2025-07-17 | test:api add pytest for health endpoint – test_main.py covers /health, Ruff linting enforced
2025-07-17 | feat:infra configure Supabase & Fly deploy files – SQL schema, Fly.toml, Terraform IaC created
2025-07-17 | chore:docker add dev containers – Dockerfile.api, Dockerfile.agent, docker-compose.yml with slim images
2025-07-17 | fix:agent resolve langchain-openai dependency – added langchain-openai==0.2.14, tests now pass
2025-07-17 | feat:web implement Supabase Auth (email) – React TypeScript app with Auth UI, login/signup pages