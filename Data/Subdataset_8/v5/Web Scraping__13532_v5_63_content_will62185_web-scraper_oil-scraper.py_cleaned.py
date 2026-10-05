import requests
from bs4 import BeautifulSoup
import pandas as pd
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
    'Referer': 'https:
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
def scrape_promotions(url):
    scraped_data = {}
    response = requests.get(url, timeout=15, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    promo_titles = soup.find_all("div", class_="promo-title text-center h1")
    promo_prices = soup.find_all("div", class_="promo-discountValue text-center h1 has-image")
    for title, price in zip(promo_titles, promo_prices):
        title_text = title.text.strip().lower()
        if "oil" in title_text:
            scraped_data["url"] = url
            scraped_data["product"] = title_text
            scraped_data["price"] = price.text[1:8]
    return pd.DataFrame(scraped_data, index=[0])
for url in urls:
    scraped_data = scrape_promotions(url)
    dealer_name = "Subaru of Miami" if "subaruofmiami" in url else "Lehman Subaru"
    print(f"Scraped data from {dealer_name}:\n{scraped_data}\n")