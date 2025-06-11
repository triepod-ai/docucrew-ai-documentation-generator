"""
Base Agent Implementation for DocuCrew
"""
from crewai import Agent
from langchain_openai import ChatOpenAI
from typing import Dict, Any, Optional


class BaseDocumentationAgent:
    """Base class for all documentation agents"""
    
    def __init__(
        self,
        role: str,
        goal: str,
        backstory: str,
        llm: Optional[ChatOpenAI] = None,
        verbose: bool = True
    ):
        self.role = role
        self.goal = goal
        self.backstory = backstory
        self.llm = llm or ChatOpenAI(temperature=0.7, model="gpt-4")
        self.verbose = verbose
        
    def create_agent(self) -> Agent:
        """Create and return a CrewAI agent"""
        return Agent(
            role=self.role,
            goal=self.goal,
            backstory=self.backstory,
            llm=self.llm,
            verbose=self.verbose,
            allow_delegation=False
        )
    
    def format_output(self, output: str) -> Dict[str, Any]:
        """Format agent output for frontend consumption"""
        return {
            "agent": self.role,
            "output": output,
            "timestamp": None  # Will be set by API
        }