"""
DocuCrew Orchestrator - Manages the documentation generation crew
"""
from crewai import Crew, Task
from typing import Dict, Any, List
import asyncio
from datetime import datetime

from .agents import (
    CodeAnalyzerAgent,
    ReadmeWriterAgent,
    ApiDocumenterAgent,
    ExampleCreatorAgent,
    EditorAgent
)


class DocuCrew:
    """Orchestrates the multi-agent documentation generation process"""
    
    def __init__(self, verbose: bool = True):
        self.verbose = verbose
        self.progress_callback = None
        
        # Initialize all agents
        self.code_analyzer = CodeAnalyzerAgent(verbose=verbose)
        self.readme_writer = ReadmeWriterAgent(verbose=verbose)
        self.api_documenter = ApiDocumenterAgent(verbose=verbose)
        self.example_creator = ExampleCreatorAgent(verbose=verbose)
        self.editor = EditorAgent(verbose=verbose)
        
        # Create agent instances
        self.agents = {
            'code_analyzer': self.code_analyzer.create_agent(),
            'readme_writer': self.readme_writer.create_agent(),
            'api_documenter': self.api_documenter.create_agent(),
            'example_creator': self.example_creator.create_agent(),
            'editor': self.editor.create_agent()
        }
    
    def set_progress_callback(self, callback):
        """Set callback for progress updates"""
        self.progress_callback = callback
    
    def _emit_progress(self, agent_name: str, status: str, message: str):
        """Emit progress update"""
        if self.progress_callback:
            self.progress_callback({
                'agent': agent_name,
                'status': status,
                'message': message,
                'timestamp': datetime.now().isoformat()
            })
    
    async def generate_documentation(self, repo_data: Dict[str, Any]) -> Dict[str, Any]:
        """Generate documentation for a repository"""
        results = {}
        
        # Task 1: Code Analysis
        self._emit_progress('code_analyzer', 'working', 'Analyzing repository structure...')
        
        analysis_task = Task(
            description=self.code_analyzer.analyze_repository_prompt(repo_data),
            agent=self.agents['code_analyzer'],
            expected_output="Detailed analysis of repository structure and patterns"
        )
        
        # Task 2: API Documentation
        self._emit_progress('api_documenter', 'waiting', 'Waiting to document APIs...')
        
        api_task = Task(
            description=self.api_documenter.document_apis_prompt(repo_data),
            agent=self.agents['api_documenter'],
            expected_output="Complete API documentation with examples"
        )
        
        # Task 3: README Creation
        self._emit_progress('readme_writer', 'waiting', 'Waiting to write README...')
        
        readme_task = Task(
            description=self.readme_writer.create_readme_prompt(repo_data),
            agent=self.agents['readme_writer'],
            expected_output="Comprehensive README documentation"
        )
        
        # Task 4: Example Creation
        self._emit_progress('example_creator', 'waiting', 'Waiting to create examples...')
        
        examples_task = Task(
            description=self.example_creator.create_examples_prompt(repo_data),
            agent=self.agents['example_creator'],
            expected_output="Practical usage examples with code"
        )
        
        # Task 5: Final Editing
        self._emit_progress('editor', 'waiting', 'Waiting to review documentation...')
        
        editor_task = Task(
            description=self.editor.edit_documentation_prompt({}),
            agent=self.agents['editor'],
            expected_output="Polished final documentation package"
        )
        
        # Create and run the crew
        crew = Crew(
            agents=list(self.agents.values()),
            tasks=[analysis_task, api_task, readme_task, examples_task, editor_task],
            verbose=self.verbose
        )
        
        # Execute the crew
        try:
            result = crew.kickoff()
            
            # Update all agents to completed
            for agent_name in self.agents:
                self._emit_progress(agent_name, 'completed', 'Task completed successfully')
            
            return {
                'success': True,
                'documentation': result,
                'timestamp': datetime.now().isoformat()
            }
            
        except Exception as e:
            return {
                'success': False,
                'error': str(e),
                'timestamp': datetime.now().isoformat()
            }