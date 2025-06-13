import os
from google.adk.agents import Agent
from ...tools.research_tools import browse_tool
from .prompt import INSTRUCTION

fact_checker = Agent(
    name="fact_checker_agent",
    model=os.getenv("PRO_MODEL_NAME"),
    instruction=INSTRUCTION,
    tools=[browse_tool]
)