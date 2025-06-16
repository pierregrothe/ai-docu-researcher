# In documentary_research/schemas.py
from pydantic import BaseModel, Field
from typing import List, Literal

class Source(BaseModel):
    source_id: str = Field(..., description="A unique identifier for the source, e.g., 'SRC_001'.")
    url: str = Field(..., description="The full URL of the source document.")
    source_type: str = Field(..., description="The type of the source, e.g., 'Encyclopedia', 'Museum', 'Industry Publication'.")
    credibility_score: int = Field(..., description="An integer from 1-10 indicating the source's authority.")
    justification: str = Field(..., description="A brief explanation for the credibility score.")

class Fact(BaseModel):
    fact_id: str = Field(..., description="A unique identifier for the fact, e.g., 'ATARI_001'.")
    description: str = Field(..., description="The text of the fact itself.")
    source_references: List[str] = Field(..., description="A list of source_ids that support this fact.")
    confidence_rating: Literal['Very High', 'High', 'Medium', 'Low', 'Very Low'] = Field(..., description="Confidence in the fact based on cross-referencing.")
    fact_type: Literal['Genesis', 'Development Anecdote', 'Technical Spec', 'Business Decision', 'Legal Challenge', 'Biographical Detail', 'Direct Quote', 'Fun Fact', 'Gossip/Interpersonal'] = Field(..., description="The category of the fact.")
    sentiment: Literal['Neutral', 'Positive', 'Negative', 'Ironic'] = Field(..., description="The emotional tone of the fact.")
    significance_rating: Literal['Critical', 'High', 'Medium', 'Low'] = Field(..., description="The fact's importance to the overall narrative.")
    potential_narrative_beat_type: Literal['Genesis', 'Turning Point', 'Anecdotal Detail', 'Consequence', 'Foreshadowing', 'Climax/Reveal', 'Payoff'] = Field(..., description="How the fact could be used in a story.")
    is_shareable_nugget: bool = Field(..., description="Indicates if the fact is a fun, easily digestible piece of trivia.")

class KnowledgeNode(BaseModel):
    facts: List[Fact]

class FinalOutput(BaseModel):
    episode_identifier: str = Field(..., description="The unique reference ID for this research project.")
    episode_topic: str = Field(..., description="A compelling, documentary-style title for the research topic.")
    source_library: List[Source] = Field(..., description="A comprehensive library of all evaluated sources.")
    knowledge_base: dict[str, KnowledgeNode] = Field(..., description="A dictionary where each key is a researched entity, and the value contains the list of facts about it.")