"""Defines the Source Finder Agent"""
from google.adk.agents.llm_agent import Agent
from documentary_research.shared_libraries import constants
from . import prompt
from documentary_research.tools.web_search import web_search

source_finder_agent = Agent(
    model=constants.FLASH_MODEL,
    name="source_finder",
    description="Given a research chapter and queries, finds all promising URLs and presents them for user selection.",
    instruction=prompt.SOURCE_FINDER_PROMPT,
    tools=[
        web_search,
    ],
)