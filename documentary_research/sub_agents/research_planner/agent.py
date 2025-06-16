# In documentary_research/sub_agents/research_planner/agent.py
from google.adk.agents.llm_agent import Agent
from documentary_research.tools.web_search import web_search
from documentary_research.shared_libraries import constants
from . import prompt

research_planner = Agent(
    model=constants.FLASH_MODEL,
    name="research_planner",
    description="Takes a high-level documentary topic and creates an exhaustive research plan by identifying all relevant entities.",
    instruction=prompt.RESEARCH_PLANNER_PROMPT,
    tools=[web_search],
)