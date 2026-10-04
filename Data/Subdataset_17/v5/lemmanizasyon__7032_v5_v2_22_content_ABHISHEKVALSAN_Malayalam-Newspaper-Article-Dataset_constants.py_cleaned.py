import requests
from bs4 import BeautifulSoup
NEWS_URL = 'https:
def fetch_news_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.content
    except requests.RequestException as e:
        print(f"Error fetching content from {url}: {e}")
        return None
def extract_headlines(content):
    soup = BeautifulSoup(content, 'html.parser')
    headlines = [headline.text.strip() for headline in soup.find_all('h2', class_='entry-title')]
    return headlines
def display_headlines(headlines):
    if headlines:
        print("Headlines:")
        for headline in headlines:
            print(f"- {headline}")
    else:
        print("No headlines found.")
def main():
    content = fetch_news_content(NEWS_URL)
    if content:
        headlines = extract_headlines(content)
        display_headlines(headlines)
    else:
        print("Failed to retrieve or parse news content.")
if __name__ == "__main__":
    main()