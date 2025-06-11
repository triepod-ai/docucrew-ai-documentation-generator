"""
API Documenter Agent - Documents APIs and endpoints
"""
from .base_agent import BaseDocumentationAgent
from crewai import Agent


class ApiDocumenterAgent(BaseDocumentationAgent):
    """Agent responsible for documenting APIs and interfaces"""
    
    def __init__(self, **kwargs):
        super().__init__(
            role="API Documentation Specialist",
            goal="Extract and document all APIs, endpoints, and interfaces with clear examples",
            backstory="""You are an API documentation expert who has documented hundreds of 
            APIs for major tech companies. You understand REST principles, GraphQL schemas, 
            and various API patterns. You excel at creating documentation that includes 
            clear examples, request/response formats, and authentication details. Your 
            documentation helps developers integrate with APIs quickly and correctly.""",
            **kwargs
        )
    
    def create_agent(self) -> Agent:
        """Create specialized API documenter agent"""
        agent = super().create_agent()
        agent.tools = []  # Add specific tools if needed
        return agent
    
    def document_apis_prompt(self, code_data: dict) -> str:
        """Generate API documentation prompt"""
        return f"""
        Analyze and document the APIs found in this codebase:
        
        Code Files:
        {code_data.get('api_files', '')}
        
        Please document:
        1. All endpoints (REST/GraphQL/RPC)
        2. Request/Response formats
        3. Authentication requirements
        4. Parameters and their types
        5. Example requests with curl/fetch
        6. Error responses
        7. Rate limiting information
        
        Format as clean, structured API documentation.
        """