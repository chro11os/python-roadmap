# Phase 1 — Fundamentals
**Time:** 6–12 weeks · **Goal:** write Python you'd trust in production, and speak basic ML.

## 1. Python, production-grade
- [x] Types & type hints, dataclasses / Pydantic models
- [x] Error handling: `try/except`, custom exceptions, retries with backoff
- [x] Files & data: JSON, CSV, `pathlib`
- [x] HTTP: `requests` / `httpx`, status codes, timeouts, auth headers
- [ ] Async basics: `async/await`, `asyncio.gather` (you'll call many APIs concurrently)
- [ ] Env vars & secrets: `.env`, never commit keys
- [ ] Virtual envs & deps: `venv` or `uv`, `pyproject.toml`
- [ ] Testing: `pytest`, mocking an HTTP call
- [ ] Logging instead of `print`

## 2. Git & GitHub
- [ ] Commit, branch, merge, rebase, resolve conflicts
- [ ] Pull requests & code review flow
- [ ] `.gitignore`, READMEs that explain *how to run it*
- [ ] GitHub Actions: run tests on push

## 3. Web / backend basics
- [ ] Build a small REST API with FastAPI
- [ ] Request validation, error responses
- [ ] SQL basics + SQLite/Postgres

## 4. ML concepts (no heavy math needed)
- [ ] What a model is; training vs. inference
- [ ] Supervised vs. unsupervised; classification vs. regression
- [ ] Overfitting, train/val/test splits, evaluation metrics (accuracy, precision, recall)
- [ ] Tokens & tokenization
- [ ] Embeddings & vector similarity (cosine)
- [ ] What a transformer / LLM is at a high level; context window, temperature
- [ ] Vocabulary: parameters, fine-tuning, hallucination, latency, throughput

## ✅ Milestone project
A FastAPI service that fetches data from a public API, validates it, stores it in SQLite, has tests, and runs CI on GitHub.

## Done when…
- You can build and debug an API client without a tutorial open
- You can explain embeddings to a non-engineer in 2 sentences
