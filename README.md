# DocuCrew - AI Documentation Generator

An intelligent multi-agent system that automatically generates comprehensive documentation for GitHub repositories using CrewAI's collaborative agent framework.

## Quick Start (5-minute setup)

### Prerequisites
- Python 3.11+
- Node.js 18+
- OpenAI API key

### Installation
1. **Backend Setup**
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   cp .env.example .env
   # Edit .env and add your OPENAI_API_KEY
   python main.py
   ```

2. **Frontend Setup**
   ```bash
   cd frontend
   npm install
   npm run dev
   ```

3. **Usage**
   - Open http://localhost:3000
   - Enter a GitHub repository URL
   - Watch AI agents collaborate in real-time
   - Download generated documentation

## Features

- **Multi-Agent Collaboration**: Five specialized AI agents working together
- **Real-time Progress**: Watch agents analyze, write, and review documentation
- **Comprehensive Analysis**: Deep code analysis and pattern recognition
- **Professional Output**: Export-ready markdown documentation
- **Interactive UI**: Beautiful visualization of the AI workflow

## Architecture

The system uses five specialized agents:
1. **Code Analyzer** - Repository structure analysis
2. **API Documenter** - API endpoint documentation
3. **README Writer** - User-friendly documentation
4. **Example Creator** - Usage examples and samples
5. **Editor** - Quality review and polishing

## Tech Stack

**Backend**: CrewAI, LangChain, FastAPI, Python 3.11+  
**Frontend**: Next.js 14, TypeScript, Tailwind CSS, Socket.io

## Documentation

- [Development Guide](docs/DEVELOPMENT.md) - Architecture and setup details
- [API Reference](docs/API.md) - Endpoint documentation
- [Deployment Guide](docs/DEPLOYMENT.md) - Production deployment

## Contributing

This is a portfolio project demonstrating multi-agent AI systems. Feel free to explore the code and suggest improvements.

## License

MIT License - see [LICENSE](LICENSE) file for details.