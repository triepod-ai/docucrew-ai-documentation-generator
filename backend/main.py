"""
DocuCrew API - FastAPI backend for multi-agent documentation generation
"""
from fastapi import FastAPI, WebSocket, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict, Any, Optional
import asyncio
import json
from datetime import datetime
import os
from dotenv import load_dotenv

from crew_orchestrator import DocuCrew
from utils import GitHubAnalyzer

# Load environment variables
load_dotenv()

# Initialize FastAPI app
app = FastAPI(
    title="DocuCrew API",
    description="Multi-agent documentation generator powered by CrewAI",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[os.getenv("FRONTEND_URL", "http://localhost:3000")],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# WebSocket connection manager
class ConnectionManager:
    def __init__(self):
        self.active_connections: list[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)

manager = ConnectionManager()

# Request/Response models
class GenerateDocsRequest(BaseModel):
    repo_url: str
    github_token: Optional[str] = None

class GenerateDocsResponse(BaseModel):
    success: bool
    documentation: Optional[Dict[str, Any]] = None
    error: Optional[str] = None
    timestamp: str

# Health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}

# Analyze repository endpoint
@app.post("/api/analyze")
async def analyze_repository(request: GenerateDocsRequest):
    """Analyze a GitHub repository structure"""
    try:
        # Initialize GitHub analyzer
        analyzer = GitHubAnalyzer(request.github_token or os.getenv("GITHUB_TOKEN"))
        
        # Parse repository URL
        owner, repo_name = analyzer.parse_repo_url(request.repo_url)
        
        # Get repository data
        repo_data = analyzer.get_repository_structure(owner, repo_name)
        
        return {
            "success": True,
            "data": repo_data,
            "timestamp": datetime.now().isoformat()
        }
        
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# WebSocket endpoint for real-time updates
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            # Keep connection alive
            await websocket.receive_text()
    except:
        manager.disconnect(websocket)

# Generate documentation endpoint
@app.post("/api/generate", response_model=GenerateDocsResponse)
async def generate_documentation(request: GenerateDocsRequest):
    """Generate documentation for a GitHub repository"""
    try:
        # Initialize components
        analyzer = GitHubAnalyzer(request.github_token or os.getenv("GITHUB_TOKEN"))
        crew = DocuCrew(verbose=True)
        
        # Set up progress callback for WebSocket updates
        async def progress_callback(update: Dict[str, Any]):
            await manager.broadcast(json.dumps(update))
        
        crew.set_progress_callback(progress_callback)
        
        # Parse and analyze repository
        owner, repo_name = analyzer.parse_repo_url(request.repo_url)
        repo_data = analyzer.get_repository_structure(owner, repo_name)
        
        # Generate documentation
        result = await crew.generate_documentation(repo_data)
        
        return GenerateDocsResponse(
            success=result['success'],
            documentation=result.get('documentation'),
            error=result.get('error'),
            timestamp=datetime.now().isoformat()
        )
        
    except Exception as e:
        return GenerateDocsResponse(
            success=False,
            error=str(e),
            timestamp=datetime.now().isoformat()
        )

# Sample repositories endpoint
@app.get("/api/samples")
async def get_sample_repositories():
    """Get list of sample repositories for testing"""
    return {
        "repositories": [
            {
                "name": "Simple Python CLI",
                "url": "https://github.com/python/cpython",
                "description": "Python programming language"
            },
            {
                "name": "FastAPI Project",
                "url": "https://github.com/tiangolo/fastapi",
                "description": "Modern web API framework"
            },
            {
                "name": "React Library",
                "url": "https://github.com/facebook/react",
                "description": "JavaScript library for UIs"
            }
        ]
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        app,
        host=os.getenv("API_HOST", "0.0.0.0"),
        port=int(os.getenv("API_PORT", 8000))
    )