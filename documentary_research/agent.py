"""Defines the Root Agent for the Documentary Research App."""
from google.adk.agents.llm_agent import Agent
from .sub_agents.research_planner.agent import research_planner
# Import the two new agents
from .sub_agents.source_finder.agent import source_finder_agent
from .sub_agents.fact_extractor.agent import fact_extractor_agent
from .sub_agents.data_synthesizer.agent import data_synthesizer_agent
from . import prompt
from .shared_libraries import constants

root_agent = Agent(
    model=constants.PRO_MODEL,
    name="documentary_research",
    description="An AI assistant that automates the research and story-planning for documentaries.",
    instruction=prompt.ROOT_PROMPT,
    sub_agents=[
        research_planner,
        source_finder_agent,    # Add the new scout
        fact_extractor_agent,   # Add the new researcher
        data_synthesizer_agent,
    ]
)