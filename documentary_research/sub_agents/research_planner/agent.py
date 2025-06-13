"""Defines the Research Planner Agent"""
import os
from google.adk.agents.llm_agent import Agent
# Import the official GoogleSearchTool class
from google.adk.tools.google_search_tool import GoogleSearchTool
from documentary_research.shared_libraries import constants
from . import prompt
from documentary_research.tools.web_search import web_search

# Initialize the tool with your credentials from the constants file
# The ADK will automatically use the API keys when you run the agent
search_tool = GoogleSearchTool()

research_planner = Agent(
    model=constants.FLASH_MODEL,
    name="research_planner",
    description="Takes a high-level documentary topic and breaks it down into a narrative plan of 5-7 logical chapters or 'knowledge nodes'.",
    instruction=prompt.RESEARCH_PLANNER_PROMPT,
    tools=[web_search],
)