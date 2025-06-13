from google.adk.agents import LoopAgent, SequentialAgent

# Import our specialists from their dedicated modules
from .sub_agents.strategist.agent import strategist
from .sub_agents.analyst.agent import analyst
from .sub_agents.fact_checker.agent import fact_checker

# --- WORKFLOW DEFINITION ---

# This sub-sequence defines the research for a single node.
# It finds sources, then extracts facts from them.
research_node_workflow = SequentialAgent(
    name="node_researcher",
    agents=[analyst, fact_checker]
)

# This loop agent will run the sub-sequence for every node in the plan.
research_loop = LoopAgent(
    agent=research_node_workflow,
    input_list_key="knowledge_nodes",
    input_item_key="suggested_queries",
    output_item_key="research_findings"
)

# This is the single, final agent exposed to the UI.
# It runs the strategist, then the loop.
root_agent = SequentialAgent(
    name="documentary_research_workflow",
    agents=[strategist, research_loop]
)