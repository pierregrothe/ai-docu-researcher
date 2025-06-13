"""Defines the Web Researcher Agent"""
import os
from google.adk.agents.llm_agent import Agent
# Import the official GoogleSearchTool class
from google.adk.tools.google_search_tool import GoogleSearchTool
from documentary_research.shared_libraries import constants
from . import prompt
from documentary_research.tools.web_search import web_search

# Initialize the tool with your credentials from the constants file
search_tool = GoogleSearchTool()


web_researcher = Agent(
    model=constants.FLASH_MODEL,
    name="web_researcher",
    description="Given a specific chapter title (knowledge node), this agent finds the best sources online, reads their snippets, and extracts raw facts.",
    instruction=prompt.WEB_RESEARCHER_PROMPT,
    tools=[web_search],
)