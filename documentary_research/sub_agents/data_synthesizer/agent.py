# In documentary_research/sub_agents/data_synthesizer/agent.py
from google.adk.agents.llm_agent import Agent
from documentary_research.shared_libraries import constants
from . import prompt

# This agent does not need tools, it only processes data.
data_synthesizer_agent = Agent(
    model=constants.PRO_MODEL,
    name="data_synthesizer_agent",
    description="The Editor-in-Chief. Synthesizes all raw data into the final, validated, and enriched knowledge graph.",
    instruction=prompt.DATA_SYNTHESIZER_PROMPT,
)