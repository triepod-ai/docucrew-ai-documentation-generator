"""
README Writer Agent - Creates comprehensive README documentation
"""
from .base_agent import BaseDocumentationAgent
from crewai import Agent


class ReadmeWriterAgent(BaseDocumentationAgent):
    """Agent responsible for writing user-friendly README documentation"""
    
    def __init__(self, **kwargs):
        super().__init__(
            role="Technical Documentation Writer",
            goal="Create clear, comprehensive, and user-friendly README documentation",
            backstory="""You are a skilled technical writer with expertise in creating 
            documentation that developers love. You understand how to balance technical 
            accuracy with readability, and you know what information developers need to 
            quickly understand and use a project. You follow README best practices and 
            create documentation that is both informative and engaging.""",
            **kwargs
        )
    
    def create_agent(self) -> Agent:
        """Create specialized README writer agent"""
        agent = super().create_agent()
        agent.tools = []  # Add specific tools if needed
        return agent
    
    def create_readme_prompt(self, analysis_data: dict) -> str:
        """Generate README creation prompt based on analysis"""
        return f"""
        Based on the following code analysis, create a comprehensive README:
        
        Project Analysis:
        {analysis_data.get('analysis', '')}
        
        Create a README with these sections:
        1. Project Title and Description
        2. Features (bullet points)
        3. Installation Instructions
        4. Usage Examples
        5. API Documentation (if applicable)
        6. Contributing Guidelines
        7. License Information
        
        Make it engaging, clear, and developer-friendly.
        """