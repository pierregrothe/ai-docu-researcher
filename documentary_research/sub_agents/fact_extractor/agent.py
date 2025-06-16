"""Defines the Fact Extractor Agent"""
from google.adk.agents.llm_agent import Agent
from documentary_research.shared_libraries import constants
from . import prompt
from documentary_research.tools.page_reader import read_web_page # This agent ONLY reads pages

fact_extractor_agent = Agent(
    model=constants.PRO_MODEL,
    name="fact_extractor", # New name
    description="Given a list of approved URLs, this agent reads each one and performs an exhaustive fact extraction.",
    instruction=prompt.FACT_EXTRACTOR_PROMPT,
    tools=[
        read_web_page, # This agent no longer uses web_search
    ],
)