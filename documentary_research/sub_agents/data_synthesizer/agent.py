"""Defines the Data Synthesizer Agent"""
from google.adk.agents.llm_agent import Agent
from documentary_research.shared_libraries import constants
from documentary_research.schemas import FinalOutput
from . import prompt

data_synthesizer = Agent(
    model=constants.PRO_MODEL, # Use the powerful model for structuring data
    name="data_synthesizer_agent",
    description="Takes all the raw research notes and meticulously structures them into the final, validated JSON output format.",
    instruction=prompt.DATA_SYNTHESIZER_PROMPT,
)