# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Defines the Pydantic models for the final JSON output."""
import datetime
from typing import List, Literal
from pydantic import BaseModel, Field

class FactPoint(BaseModel):
    fact_id: str = Field(description="A unique ID for the fact, e.g., 'NODE1_FACT001'.")
    description: str = Field(description="The detailed factual statement.")
    fact_type: Literal["anecdote", "statistic", "biographical_detail", "quote", "event", "technical_detail"] = Field(description="A category for the fact.")
    significance_rating: int = Field(ge=1, le=10, description="A numerical score (1-10) of how important this fact is for the documentary.")
    confidence_score: int = Field(ge=1, le=100, description="A numerical score (1-100) of how likely the fact is to be accurate based on the source.")
    source_url: str = Field(description="The URL of the source where this fact was found.")

class TopSource(BaseModel):
    url: str
    title: str
    justification: str = Field(description="Why this source is considered reliable and relevant for this topic.")

class ResearchFindings(BaseModel):
    top_sources: List[TopSource]
    fact_points: List[FactPoint]

class KnowledgeNode(BaseModel):
    node_title: str = Field(description="The title of the chapter or story segment.")
    research_findings: ResearchFindings

class Metadata(BaseModel):
    generation_date: str = Field(default_factory=lambda: datetime.datetime.now(datetime.timezone.utc).isoformat())
    models_used: List[str]
    warnings: List[str] = []

class FinalOutput(BaseModel):
    reference_ID: str
    topic: str
    narrative_summary: str = Field(description="A one-sentence summary of the documentary's angle.")
    metadata: Metadata
    knowledge_nodes: List[KnowledgeNode]