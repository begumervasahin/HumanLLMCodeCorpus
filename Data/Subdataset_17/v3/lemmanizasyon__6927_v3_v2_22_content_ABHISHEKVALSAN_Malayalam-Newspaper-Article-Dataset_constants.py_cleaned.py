import requests
from bs4 import BeautifulSoup
BASE_URL = 'https:
def fetch_news_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.content
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")
    return None
def parse_news_content(content):
    if not content:
        print("No content to parse.")
        return
    soup = BeautifulSoup(content, 'html.parser')
    headlines = soup.find_all('h2', class_='entry-title')
    for headline in headlines:
        print(headline.get_text(strip=True))
def main():
    content = fetch_news_content(BASE_URL)
    parse_news_content(content)
if __name__ == "__main__":
    main()