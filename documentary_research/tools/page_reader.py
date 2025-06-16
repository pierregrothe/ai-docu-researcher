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
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()  # Will raise an exception for 4xx/5xx status codes

        soup = BeautifulSoup(response.content, 'html.parser')

        # Remove script and style elements
        for script_or_style in soup(["script", "style"]):
            script_or_style.decompose()

        # Get text and clean it up
        text = soup.get_text()
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        clean_text = '\n'.join(chunk for chunk in chunks if chunk)

        if not clean_text:
            return {"status": "error", "error_message": "Failed to extract meaningful text from the page."}

        return {"status": "success", "text_content": clean_text}

    except requests.exceptions.RequestException as e:
        return {"status": "error", "error_message": f"Failed to fetch URL: {e}"}
    except Exception as e:
        return {"status": "error", "error_message": str(e)}