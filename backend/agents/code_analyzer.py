"""
Code Analyzer Agent - Analyzes repository structure and code patterns
"""
from .base_agent import BaseDocumentationAgent
from crewai import Agent


class CodeAnalyzerAgent(BaseDocumentationAgent):
    """Agent responsible for analyzing code structure and patterns"""
    
    def __init__(self, **kwargs):
        super().__init__(
            role="Senior Code Analyst",
            goal="Analyze repository structure, identify key components, patterns, and architectural decisions",
            backstory="""You are an experienced software architect with 15+ years of experience 
            analyzing codebases across multiple languages and frameworks. You excel at quickly 
            understanding project structure, identifying design patterns, and recognizing 
            architectural decisions. You provide clear, concise analysis that helps others 
            understand complex codebases.""",
            **kwargs
        )
    
    def create_agent(self) -> Agent:
        """Create specialized code analyzer agent"""
        agent = super().create_agent()
        agent.tools = []  # Add specific tools if needed
        return agent
    
    def analyze_repository_prompt(self, repo_data: dict) -> str:
        """Generate analysis prompt for repository"""
        return f"""
        Analyze the following repository structure and provide insights:
        
        Repository: {repo_data.get('name', 'Unknown')}
        Files: {repo_data.get('file_count', 0)}
        Main Language: {repo_data.get('main_language', 'Unknown')}
        
        File Structure:
        {repo_data.get('structure', '')}
        
        Please provide:
        1. Overview of project structure
        2. Key architectural patterns identified
        3. Main components and their purposes
        4. Technology stack analysis
        5. Code organization assessment
        """