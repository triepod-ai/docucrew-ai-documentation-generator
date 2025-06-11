# Development Guide

## Architecture Overview

### Multi-Agent System
DocuCrew uses CrewAI to orchestrate five specialized AI agents:

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

## Development Setup

### Environment Variables
```bash
# Required
OPENAI_API_KEY=your_openai_api_key

# Optional
GITHUB_TOKEN=your_github_token  # For private repositories
FRONTEND_URL=http://localhost:3000  # CORS configuration
API_HOST=0.0.0.0  # API host
API_PORT=8000  # API port
```

### Virtual Environment
Always work within a Python virtual environment:
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Development Commands

**Backend Development**
```bash
cd backend
source venv/bin/activate
python main.py  # Start FastAPI server on localhost:8000
```

**Frontend Development**
```bash
cd frontend
npm run dev     # Start Next.js dev server on localhost:3000
npm run build   # Build for production
npm run lint    # Run ESLint
```

## Testing

### Test Repositories
Use these repositories for testing:
- Simple: `https://github.com/kennethreitz/requests`
- Medium: `https://github.com/pallets/flask`
- Complex: `https://github.com/django/django`

### API Testing
```bash
# Test backend API
curl -X POST http://localhost:8000/api/analyze \
  -H "Content-Type: application/json" \
  -d '{"repo_url": "https://github.com/python/cpython"}'
```

## Common Issues & Solutions

**Rate limit exceeded**  
→ Add delays between agent calls or use a GitHub token

**Agents not responding**  
→ Check OpenAI API key and model availability

**WebSocket disconnection**  
→ Ensure CORS settings match your frontend URL

## Project Structure

```
ai-project-documentation-generator-with-crewai/
├── backend/
│   ├── agents/           # AI agent implementations
│   ├── utils/           # Utility functions
│   ├── crew_orchestrator.py  # Agent coordination
│   ├── main.py          # FastAPI application
│   └── requirements.txt
├── frontend/
│   ├── components/      # React components
│   ├── pages/          # Next.js pages
│   └── package.json
├── docs/               # Documentation
├── examples/           # Example outputs
└── archive/           # Archived files
```

## Contributing

1. Follow existing code patterns and conventions
2. Test with multiple repository types
3. Update documentation for any new features
4. Ensure WebSocket communication works properly
5. Maintain agent prompt quality and specificity