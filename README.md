# DocuCrew - AI Project Documentation Generator

An intelligent multi-agent system that automatically generates comprehensive documentation for GitHub repositories using CrewAI's collaborative agent framework.

## 🎯 Overview

DocuCrew employs five specialized AI agents that work together to analyze code, create documentation, and ensure quality:

- **Code Analyzer Agent** - Analyzes repository structure and patterns
- **README Writer Agent** - Creates user-friendly documentation
- **API Documenter Agent** - Documents APIs with examples
- **Example Creator Agent** - Generates practical usage examples
- **Editor Agent** - Reviews and polishes all documentation

## 🚀 Features

- **Multi-Agent Collaboration**: Watch AI agents work together in real-time
- **Comprehensive Analysis**: Deep code analysis and pattern recognition
- **Live Progress Tracking**: See each agent's thoughts and progress
- **Beautiful UI**: Interactive visualization of the documentation process
- **Export Ready**: Generate markdown documentation ready for your repo

## 🛠️ Tech Stack

**Backend:**
- CrewAI - Multi-agent orchestration
- LangChain - LLM integration
- FastAPI - REST API & WebSockets
- Python 3.11+

**Frontend:**
- Next.js 14 - React framework
- TypeScript - Type safety
- Tailwind CSS - Styling
- Framer Motion - Animations
- Socket.io - Real-time updates

## 📋 Prerequisites

- Python 3.11 or higher
- Node.js 18 or higher
- OpenAI API key
- GitHub token (optional, for private repos)

## 🔧 Installation

### Backend Setup

1. Navigate to the backend directory:
```bash
cd backend
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
cp .env.example .env
# Edit .env and add your OpenAI API key
```

5. Start the backend server:
```bash
python main.py
```

The API will be available at `http://localhost:8000`

### Frontend Setup

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm run dev
```

The frontend will be available at `http://localhost:3000`

## 📖 Usage

1. Open the DocuCrew interface at `http://localhost:3000`
2. Enter a GitHub repository URL (e.g., `https://github.com/username/repo`)
3. Click "Generate Documentation"
4. Watch the agents collaborate in real-time
5. Download or copy the generated documentation

## 🏗️ Project Structure

```
ai-project-documentation-generator-with-crewai/
├── backend/
│   ├── agents/
│   │   ├── base_agent.py
│   │   ├── code_analyzer.py
│   │   ├── readme_writer.py
│   │   ├── api_documenter.py
│   │   ├── example_creator.py
│   │   └── editor.py
│   ├── api/
│   ├── utils/
│   │   └── github_analyzer.py
│   ├── crew_orchestrator.py
│   ├── main.py
│   └── requirements.txt
├── frontend/
│   ├── components/
│   ├── pages/
│   ├── styles/
│   └── package.json
└── README.md
```

## 🎨 Architecture

The system follows a multi-agent architecture where each agent has a specific role:

1. **Code Analyzer** examines the repository structure
2. **API Documenter** identifies and documents APIs
3. **README Writer** creates the main documentation
4. **Example Creator** generates usage examples
5. **Editor** reviews and polishes everything

## 🤝 Contributing

Feel free to open issues or submit pull requests!