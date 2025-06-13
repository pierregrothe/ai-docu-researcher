"""Defines the Root Documentary Research Agent"""
from google.adk.agents.llm_agent import Agent
from .shared_libraries import constants
from .sub_agents.research_planner.agent import research_planner
from .sub_agents.web_researcher.agent import web_researcher
from .sub_agents.data_synthesizer.agent import data_synthesizer
from . import prompt

root_agent = Agent(
    model=constants.PRO_MODEL, # The orchestrator should be powerful
    name=constants.AGENT_NAME,
    description=constants.DESCRIPTION,
    instruction=prompt.ROOT_PROMPT,
    sub_agents=[
        research_planner,
        web_researcher,
        data_synthesizer,
    ],
)