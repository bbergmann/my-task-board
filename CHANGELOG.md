# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased]

### Phase 0 — Setup
- Initial project setup with CLAUDE.md, tracking files, and permissions
- Chose Task Board with FastAPI + React + Vite + SQLite stack

### Phase 1 — Foundation
- Scaffolded FastAPI backend with health endpoint and SQLite
- Scaffolded React + Vite frontend with routing
- Added ping endpoint (1-shot health check passed)
- Created /add-endpoint custom skill
- Date: 2026-02-11

### Phase 2 — Backend Core
- Added SQLAlchemy models for tasks and columns with FK relationship
- Created full CRUD endpoints for both resources with Pydantic validation
- Set up Alembic migrations (initial schema + notes field addition)
- Updated CLAUDE.md with backend conventions (router, schema, DI patterns)
- Date: 2026-02-11

<!--
Format for future entries:

### Phase N — [Phase Name]
- What was added, changed, or fixed
- Keep it brief — one line per meaningful change
- Date: YYYY-MM-DD
-->
