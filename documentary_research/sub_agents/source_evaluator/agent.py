# In documentary_research/sub_agents/source_evaluator/agent.py
from google.adk.agents.llm_agent import Agent
from documentary_research.tools.web_search import web_search
from documentary_research.shared_libraries import constants
from . import prompt

source_evaluator_agent = Agent(
    model=constants.FLASH_MODEL,
    name="source_evaluator",
    description="Given an entity and search queries, finds, evaluates, and ranks all potential online sources.",
    instruction=prompt.SOURCE_EVALUATOR_PROMPT,
    tools=[web_search],
)