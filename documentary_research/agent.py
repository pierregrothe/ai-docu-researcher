# In documentary_research/agent.py
from google.adk.agents.llm_agent import Agent
from documentary_research.shared_libraries import constants
from . import prompt
from .schemas import FinalOutput

# Import all the specialized agents
from .sub_agents.research_planner.agent import research_planner
from .sub_agents.source_evaluator.agent import source_evaluator_agent
from .sub_agents.fact_extractor.agent import fact_extractor_agent
from .sub_agents.data_synthesizer.agent import data_synthesizer_agent

root_agent = Agent(
    model=constants.PRO_MODEL,
    name=constants.AGENT_NAME,
    description=constants.DESCRIPTION,
    instruction=prompt.ROOT_PROMPT,
    output_schema=FinalOutput, # The final output will be the complete knowledge graph
    sub_agents=[
        research_planner,
        source_evaluator_agent,
        fact_extractor_agent,
        data_synthesizer_agent,
    ],
)