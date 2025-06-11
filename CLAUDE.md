# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Development Commands

### Backend Development
```bash
cd backend
source venv/bin/activate  # Activate virtual environment
python main.py           # Start FastAPI server on localhost:8000
```

### Frontend Development
```bash
cd frontend
npm run dev             # Start Next.js dev server on localhost:3000
npm run build          # Build for production
npm run lint           # Run ESLint
```

## Environment Setup

### Required Environment Variables
- `OPENAI_API_KEY` - OpenAI API key for LLM access
- `GITHUB_TOKEN` - GitHub token for private repository access (optional)
- `FRONTEND_URL` - Frontend URL for CORS (defaults to http://localhost:3000)
- `API_HOST` - API host (defaults to 0.0.0.0)
- `API_PORT` - API port (defaults to 8000)

### Virtual Environment
Always work within a Python virtual environment in the backend directory:
```bash
cd backend
python -m venv venv
source venv/bin/activate
```

## Architecture Overview

Multi-agent system using CrewAI with five specialized agents (Code Analyzer, README Writer, API Documenter, Example Creator, Editor). FastAPI backend with WebSocket support for real-time updates. Next.js frontend with TypeScript.

See [docs/DEVELOPMENT.md](docs/DEVELOPMENT.md) for detailed architecture and development information.