import os
from google.adk.agents import Agent
from ...tools.research_tools import web_search
from .prompt import INSTRUCTION

analyst = Agent(
    name="analyst_agent",
    model=os.getenv("FLASH_MODEL_NAME"),
    instruction=INSTRUCTION,
    tools=[web_search]
)