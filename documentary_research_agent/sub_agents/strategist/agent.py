import os
from google.adk.agents import Agent
from .prompt import INSTRUCTION

strategist = Agent(
    name="strategist_agent",
    model=os.getenv("PRO_MODEL_NAME"),
    instruction=INSTRUCTION
)