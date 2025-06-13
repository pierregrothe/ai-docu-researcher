"""Defines custom tools for the documentary research agent."""
import os
from googleapiclient.discovery import build

def web_search(query: str, num_pages: int = 3) -> dict:
    """Performs a multi-page web search using the Google Custom Search API."""
    try:
        # The tool needs to find the keys from the environment variables
        api_key = os.environ["GOOGLE_API_KEY"]
        search_engine_id = os.environ["GOOGLE_CSE_ID"]
        service = build("customsearch", "v1", developerKey=api_key)
        
        all_results = []
        for page in range(num_pages):
            start_index = 1 + page * 10
            res = (
                service.cse()
                .list(
                    q=query,
                    cx=search_engine_id,
                    num=10,
                    start=start_index,
                )
                .execute()
            )
            
            page_results = [
                {"title": item["title"], "link": item["link"], "snippet": item["snippet"]}
                for item in res.get("items", [])
            ]
            all_results.extend(page_results)
            
        return {"status": "success", "results": all_results}

    except Exception as e:
        return {"status": "error", "error_message": str(e)}