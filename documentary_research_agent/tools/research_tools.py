import os
import requests
from bs4 import BeautifulSoup
from googleapiclient.discovery import build

def web_search(query: str, num_pages: int = 3) -> dict:
    """Performs a multi-page web search using the Google Custom Search API."""
    try:
        api_key = os.environ["CUSTOM_SEARCH_API_KEY"]
        search_engine_id = os.environ["CUSTOM_SEARCH_ENGINE_ID"]
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
                {"title": item["title"], "link": item["link"]}
                for item in res.get("items", [])
            ]
            all_results.extend(page_results)
            
        return {"status": "success", "results": all_results}

    except Exception as e:
        return {"status": "error", "error_message": str(e)}

def browse_tool(url: str) -> dict:
    """Reads the full text content of a single web page."""
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        for script_or_style in soup(["script", "style", "nav", "footer", "header"]):
            script_or_style.decompose()
        
        text = soup.get_text()
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text = '\n'.join(chunk for chunk in chunks if chunk)
        
        return {"status": "success", "content": text[:20000]}

    except Exception as e:
        return {"status": "error", "error_message": str(e)}