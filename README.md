# AI Documentary Researcher

An autonomous multi-agent framework designed to automate the initial research and story-planning phase for video production. Leveraging Google's Agent Development Kit (ADK) and Vertex AI's Gemini models, this system takes a high-level topic and generates a comprehensive, structured JSON research brief for creative teams.

## Key Features

- **Autonomous Research:** Takes a single topic and independently plans and executes a research strategy.
- **Structured JSON Output:** Produces a rich JSON file with narrative nodes, sourced facts, and metadata, ready for creative use.
- **Modular Agent Design:** Built with a clean, sequential agent architecture using the Google Agent Development Kit (ADK).
- **Extensible & Observable:** Includes built-in support for logging and metadata collection for easy troubleshooting and analysis.

## Architecture

The system is designed as a sequential workflow orchestrated by a master `SequentialAgent`.

1.  **`StrategistAgent` (`LlmAgent`):** Receives the main topic, brainstorms a narrative structure, and generates a "Research Plan" containing chapters and targeted search queries.
2.  **`ResearchLoopAgent` (`LoopAgent`):** Iterates through each chapter of the research plan. For each chapter, it runs:
    - **The Enhanced `AnalystAgent`:** This `LlmAgent` is the core worker. It takes the search queries, uses custom tools to search the web and browse pages, validates page relevance, extracts key facts, and structures them.
3.  **`DataConsolidatorAgent` (`CustomAgent`):** Gathers all the processed data, adds final metadata (timestamps, session IDs), and produces the final, clean JSON object.

## Technology Stack

- **Platform:** Google Cloud Platform (GCP)
- **AI/LLM:** Vertex AI (Gemini 1.5 Pro)
- **Agent Framework:** Google Agent Development Kit (ADK)
- **Core Language:** Python 3.10+
- **Key APIs:** Google Custom Search API

---

## Getting Started

### Prerequisites

- Python 3.10 or later
- A Google Cloud Project with the Vertex AI API enabled.
- Authentication configured for GCP (e.g., by running `gcloud auth application-default login`).

### 1. Clone the Repository

```bash
git clone [YOUR_GITHUB_REPO_URL]
cd ai-docu-researcher
```

### 2. Set Up a Virtual Environment

```bash
# For macOS / Linux
python3 -m venv venv
source venv/bin/activate

# For Windows
python -m venv venv
.\venv\Scripts\activate
```

### 3. Install Dependencies

Create a `requirements.txt` file (we will do this next) and install the packages.

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a file named `.env` in the root of the project. **This file should not be committed to GitHub.** Add your project-specific configuration:

```
# .env file
GCP_PROJECT_ID="your-gcp-project-id"
GCP_REGION="us-central1"
# Add your Google Custom Search Engine ID and API Key if needed
CUSTOM_SEARCH_ENGINE_ID="your-cx-id"
CUSTOM_SEARCH_API_KEY="your-search-api-key"
```

## Usage

To run the research agent, execute the main application script from your terminal.

```bash
python run_research.py --subject "The History of Pong" --ref "BBP_001"
```

The script will invoke the agent workflow and, upon completion, save a detailed JSON file named `BBP_001_research.json` in the project's root directory.

## License

This project is licensed under the MIT License.
