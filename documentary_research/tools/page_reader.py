# In documentary_research/tools/page_reader.py
import requests
from bs4 import BeautifulSoup

def read_web_page(url: str) -> dict:
    """
    Takes a URL, fetches the HTML content, and extracts the clean text content.
    Returns a dictionary containing the status and the extracted text.
    """
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers, timeout=20)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')

        for script_or_style in soup(["script", "style", "nav", "footer", "header"]):
            script_or_style.decompose()

        text = soup.get_text()
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        clean_text = '\n'.join(chunk for chunk in chunks if chunk)

        if not clean_text:
            return {"status": "error", "error_message": "Failed to extract meaningful text."}

        return {"status": "success", "text_content": clean_text}

    except requests.exceptions.RequestException as e:
        return {"status": "error", "error_message": f"Failed to fetch URL: {e}"}