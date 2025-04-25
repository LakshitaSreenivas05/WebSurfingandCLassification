
import requests
from bs4 import BeautifulSoup
from readability import Document

def google_search(query, api_key, cx, num_results=5):
    # Construct the API URL
    url = f"https://www.googleapis.com/customsearch/v1?q={query}&key={api_key}&cx={cx}&num={num_results}"

    response = requests.get(url)
    
    if response.status_code == 200:
        search_results = response.json()
        # Extract URLs from the results
        links = []
        for item in search_results.get('items', []):
            links.append(item['link'])
        return links
    else:
        print("Error fetching search results:", response.status_code)
        return []

# Example usage
api_key = "API key"
cx = "Search Engine key"  # Extract just the ID from the full URL

query = "AI in Defence"
urls = google_search(query, api_key, cx)
print(urls)

def extract_main_text(url):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        }
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            doc = Document(response.text)
            html = doc.summary()
            soup = BeautifulSoup(html, 'html.parser')
            return soup.get_text(separator="\n", strip=True)
        else:
            print(f"Error fetching URL {url}: {response.status_code}")
            return ""
    except Exception as e:
        print(f"Exception scraping {url}: {e}")
        return ""
    
search_results = google_search(query, api_key, cx)

for url in search_results:
    print(f"\nExtracting from: {url}")
    text = extract_main_text(url)

