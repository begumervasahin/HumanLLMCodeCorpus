import requests
from bs4 import BeautifulSoup
URL_PREFIX = 'https:
def fetch_news_content(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.content
        else:
            print(f"Failed to fetch content. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
def parse_news_content(content):
    if content:
        soup = BeautifulSoup(content, 'html.parser')
        headlines = soup.find_all('h2', class_='entry-title')
        for headline in headlines:
            print(headline.text.strip())
    else:
        print("No content to parse.")
def main():
    full_url = URL_PREFIX
    content = fetch_news_content(full_url)
    parse_news_content(content)
if __name__ == "__main__":
    main()