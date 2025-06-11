"""
Editor Agent - Reviews and polishes documentation
"""
from .base_agent import BaseDocumentationAgent
from crewai import Agent


class EditorAgent(BaseDocumentationAgent):
    """Agent responsible for reviewing and polishing all documentation"""
    
    def __init__(self, **kwargs):
        super().__init__(
            role="Senior Technical Editor",
            goal="Review, refine, and ensure consistency across all documentation",
            backstory="""You are a meticulous technical editor with a keen eye for detail. 
            You've edited documentation for major open-source projects and tech companies. 
            You ensure consistency in tone, style, and formatting while maintaining technical 
            accuracy. You catch errors others miss and transform good documentation into 
            great documentation. You follow industry best practices and style guides.""",
            **kwargs
        )
    
    def create_agent(self) -> Agent:
        """Create specialized editor agent"""
        agent = super().create_agent()
        agent.tools = []  # Add specific tools if needed
        return agent
    
    def edit_documentation_prompt(self, all_docs: dict) -> str:
        """Generate editing prompt for all documentation"""
        return f"""
        Review and edit the following documentation for quality and consistency:
        
        README:
        {all_docs.get('readme', '')}
        
        API Documentation:
        {all_docs.get('api_docs', '')}
        
        Examples:
        {all_docs.get('examples', '')}
        
        Please:
        1. Ensure consistent formatting and style
        2. Fix any grammatical or spelling errors
        3. Verify technical accuracy
        4. Improve clarity where needed
        5. Add missing sections if necessary
        6. Create a cohesive documentation package
        
        Return the polished, final documentation.
        """