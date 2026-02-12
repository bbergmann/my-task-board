# Project: My Task Board

## Overview
A Kanban-style task board where users can create, move, and assign tasks across status columns (To Do, In Progress, Done).

## Tech Stack
- **Backend:** Python 3.11+ / FastAPI / SQLite (dev) / Pydantic for validation
- **Frontend:** React 18 / Vite / JavaScript
- **Database:** SQLite for development, Postgres for Docker/production
- **Testing:** pytest (backend), Vitest or Jest (frontend)

## Project Structure
```
backend/
  app/
    main.py          # FastAPI app entry point
    database.py      # Database connection and session
    models/          # SQLAlchemy models
    routers/         # API endpoint routers
    schemas/         # Pydantic request/response schemas
frontend/
  src/
    components/      # Reusable UI components
    pages/           # Page-level components (one per route)
    api/             # API client functions
    App.jsx          # Root component with routing
```

## Conventions
- **Backend:** Snake_case for files and functions. Type hints on all function signatures. Pydantic models for all request/response bodies.
- **Frontend:** PascalCase for components, camelCase for functions/variables. One component per file.
- **API:** RESTful routes under `/api/`. Return JSON. Use HTTP status codes correctly (201 for created, 404 for not found, 422 for validation errors).
- **Routers:** Each resource gets `routers/{resource}.py` with prefix `/api/{resource}` and a `tags` list.
- **Schemas:** Pydantic schemas go in `schemas/{resource}.py` with `Create`, `Update`, and `Response` variants.
- **DB Sessions:** Use dependency injection via `Depends(get_db)` — never create sessions manually.
- **Commits:** Specific `git add <files>` — never `git add .`. Conventional commit messages.

## Key Commands
```bash
# Backend
cd backend && python -m uvicorn app.main:app --reload
cd backend && python -m pytest

# Frontend
cd frontend && npm run dev
cd frontend && npm run build

# Both (Docker)
docker compose up --build
```

## What NOT to Do
- Do NOT use `created_at` for business dates (use specific fields like `due_date`, etc.)
- Do NOT set CORS to `*` — restrict to `http://localhost:5173` in development
- Do NOT add comments to obvious code
- Do NOT create utility files for one-time operations
- Do NOT use LLM/AI API calls for calculations that can be done with simple functions
