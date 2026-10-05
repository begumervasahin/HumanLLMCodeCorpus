
from bs4 import BeautifulSoup as BS
import requests
import pandas as pd
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
    'referrer': 'https:
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache'
}
urls = [
    "https:
    "https:
]
def scrape_subaru_of_miami(url):
    scraped_data = {"miami": {}}
    response = requests.get(url, timeout=15, headers=headers)
    soup = BS(response.content, "html.parser")
    promo_titles = soup.find_all("div", class_="promo-title text-center h1")
    promo_price = soup.find_all("div", class_="promo-discountValue text-center h1 has-image")[2]
    for title in promo_titles:
        if "OIL" in title.text.strip():
            scraped_data["miami"]["url"] = url[0:29]
            scraped_data["miami"]["product"] = title.text.strip()
            scraped_data["miami"]["price"] = promo_price.text[1:8]
    print(pd.DataFrame.from_dict(scraped_data, orient='index'))
def scrape_lehman_subaru(url):
    scraped_data = {"lehmans": {}}
    response = requests.get(url, timeout=15, headers=headers)
    soup = BS(response.content, "html.parser")
    promo_titles = soup.find_all("div", class_="promo-title text-center h1")
    promo_price = soup.find_all("div", class_="promo-discountValue text-center h1 has-image")[4]
    for title in promo_titles:
        if "Oil" in title.text.strip():
            scraped_data["lehmans"]["url"] = url[0:29]
            scraped_data["lehmans"]["product"] = title.text.strip()
            scraped_data["lehmans"]["price"] = promo_price.text[1:8]
    print(pd.DataFrame.from_dict(scraped_data, orient='index'))
scrape_subaru_of_miami(urls[0])
scrape_lehman_subaru(urls[1])