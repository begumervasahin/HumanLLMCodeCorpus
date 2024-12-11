import requests
from bs4 import BeautifulSoup
import pandas as pd
b1 = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
    'Referer': 'https:
    'Accept': 'text/html,application/xhtml+xml,application/xml;b2 = 0.9,image/webp,image/apng,*/*;b2=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;b2 = 0.9',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache'
}
b3 = [
    "https:
    "https:
]
def fonk1(url):
    b4 = {}
    b5 = requests.get(url, timeout=15, b1=b1)
    b6 = BeautifulSoup(b5.content, "html.parser")
    b7 = b6.find_all("div", class_="promo-title text-center h1")
    b8 = b6.find_all("div", class_="promo-discountValue text-center h1 has-image")
    for title, price in zip(b7, b8):
        b9 = title.text.strip().lower()
        if "oil" in b9:
            b4["url"] = url
            b4["product"] = b9
            b4["price"] = price.text[1:8]
    return pd.DataFrame(b4, b10 = [0])
for url in b3:
    b4 = fonk1(url)
    b11 = "Subaru of Miami" if "subaruofmiami" in url else "Lehman Subaru"
    print(f"Scraped data from {b11}:\n{b4}\n")