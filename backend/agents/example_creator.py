"""
Example Creator Agent - Generates practical usage examples
"""
from .base_agent import BaseDocumentationAgent
from crewai import Agent


class ExampleCreatorAgent(BaseDocumentationAgent):
    """Agent responsible for creating practical usage examples"""
    
    def __init__(self, **kwargs):
        super().__init__(
            role="Developer Advocate",
            goal="Create practical, real-world examples that demonstrate project usage",
            backstory="""You are a developer advocate with years of experience helping 
            developers learn new tools and libraries. You understand that good examples 
            are worth a thousand words of documentation. You create examples that are 
            simple enough to understand but realistic enough to be useful. You always 
            consider common use cases and edge cases that developers might encounter.""",
            **kwargs
        )
    
    def create_agent(self) -> Agent:
        """Create specialized example creator agent"""
        agent = super().create_agent()
        agent.tools = []  # Add specific tools if needed
        return agent
    
    def create_examples_prompt(self, project_data: dict) -> str:
        """Generate examples creation prompt"""
        return f"""
        Create practical usage examples for this project:
        
        Project Type: {project_data.get('type', 'Unknown')}
        Main Features: {project_data.get('features', '')}
        API Summary: {project_data.get('api_summary', '')}
        
        Create examples for:
        1. Basic "Hello World" usage
        2. Common use case implementation
        3. Advanced feature demonstration
        4. Error handling example
        5. Integration with other tools
        
        Each example should include:
        - Clear description
        - Complete, runnable code
        - Expected output
        - Common pitfalls to avoid
        """