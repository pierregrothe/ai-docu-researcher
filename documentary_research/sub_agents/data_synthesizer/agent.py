"""Defines the Data Synthesizer Agent"""
from google.adk.agents.llm_agent import Agent
from documentary_research.shared_libraries import constants
# The schema import was missing in the file you sent, which might be another issue.
# I've added it back in based on your previous code structure.
from documentary_research.schemas import FinalOutput
from . import prompt

# This variable name is the fix.
# It's now 'data_synthesizer_agent' to match the import statement.
data_synthesizer_agent = Agent(
    model=constants.PRO_MODEL, # Use the powerful model for structuring data
    name="data_synthesizer_agent",
    description="Takes all the raw research notes and meticulously structures them into the final, validated JSON output format.",
    instruction=prompt.DATA_SYNTHESIZER_PROMPT,
    # The `output_schema` was also missing from the file content you sent.
    # This is critical for the synthesizer to work.
    output_schema=FinalOutput
)