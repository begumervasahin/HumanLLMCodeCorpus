import requests
from bs4 import BeautifulSoup
NEWS_URL = 'https:
def fetch_news_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.content
    except requests.RequestException as e:
        print("Failed to fetch content:", e)
        return None
def parse_news_content(content):
    if content:
        soup = BeautifulSoup(content, 'html.parser')
        headlines = soup.find_all('h2', class_='entry-title')
        for headline in headlines:
            print(headline.get_text(strip=True))
    else:
        print("No content to parse.")
def main():
    full_url = NEWS_URL
    content = fetch_news_content(full_url)
    parse_news_content(content)
if __name__ == "__main__":
    main()