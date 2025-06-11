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

### Setup Commands
```bash
# Backend setup
cd backend && ./setup.sh

# Frontend setup
cd frontend && npm install
```

## Architecture Overview

### Multi-Agent System
The project uses CrewAI to orchestrate five specialized AI agents:

1. **Code Analyzer Agent** (`agents/code_analyzer.py`) - Analyzes repository structure and code patterns
2. **README Writer Agent** (`agents/readme_writer.py`) - Creates user-friendly documentation
3. **API Documenter Agent** (`agents/api_documenter.py`) - Documents APIs with examples
4. **Example Creator Agent** (`agents/example_creator.py`) - Generates practical usage examples
5. **Editor Agent** (`agents/editor.py`) - Reviews and polishes all documentation

### Core Components

**Backend (`backend/`)**
- `crew_orchestrator.py` - Manages agent workflow and task coordination
- `main.py` - FastAPI application with WebSocket support for real-time updates
- `utils/github_analyzer.py` - GitHub API integration for repository analysis
- `agents/base_agent.py` - Base class for all agents with shared functionality

**Frontend (`frontend/`)**
- Next.js 14 application with TypeScript
- Real-time WebSocket connection to backend for live agent progress
- UI components for repository input, agent status display, and documentation preview

### Agent Workflow
1. Code Analyzer examines repository structure
2. API Documenter identifies and documents APIs
3. README Writer creates main documentation
4. Example Creator generates usage examples
5. Editor reviews and polishes final output

All agents run in sequence through CrewAI's task orchestration system, with real-time progress updates sent via WebSocket to the frontend.

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