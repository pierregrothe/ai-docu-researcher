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

"""Defines constants."""
import os
import dotenv

dotenv.load_dotenv()

# Core Agent Details
AGENT_NAME = "documentary_research"
DESCRIPTION = "An AI assistant that automates the research and story-planning for documentaries."

# Google Cloud & Vertex AI Config
PROJECT = os.getenv("GOOGLE_CLOUD_PROJECT", "")
LOCATION = os.getenv("GOOGLE_CLOUD_LOCATION", "")

# Model Names
FLASH_MODEL = os.getenv("FLASH_MODEL_NAME", "gemini-2.5-flash-preview-05-20")
PRO_MODEL = os.getenv("PRO_MODEL_NAME", "gemini-2.5-pro-preview-05-06")
