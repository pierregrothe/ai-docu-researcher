# In documentary_research/sub_agents/fact_extractor/agent.py
from google.adk.agents.llm_agent import Agent
from documentary_research.shared_libraries import constants
from . import prompt
from documentary_research.tools.page_reader import read_web_page

fact_extractor_agent = Agent(
    model=constants.PRO_MODEL,
    name="fact_extractor",
    description="Given a single URL, reads the page and extracts all atomic facts, with a focus on entertaining details.",
    instruction=prompt.FACT_EXTRACTOR_PROMPT,
    tools=[read_web_page],
)