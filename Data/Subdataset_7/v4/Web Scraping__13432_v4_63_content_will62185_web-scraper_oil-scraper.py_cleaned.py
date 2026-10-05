
from bs4 import BeautifulSoup as BS
import requests
import pandas as pd
b1 = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
    'referrer': 'https:
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
    b4 = {"miami": {}}
    b5 = requests.get(url, timeout=15, b1=b1)
    b6 = BS(b5.content, "html.parser")
    b7 = b6.find_all("div", class_="promo-title text-center h1")
    b8 = b6.find_all("div", class_="promo-discountValue text-center h1 has-image")[2]
    for title in b7:
        if "OIL" in title.text.strip():
            b4["miami"]["url"] = url[0:29]
            b4["miami"]["product"] = title.text.strip()
            b4["miami"]["price"] = b8.text[1:8]
    print(pd.DataFrame.from_dict(b4, b9 = 'index'))
def fonk2(url):
    b4 = {"lehmans": {}}
    b5 = requests.get(url, timeout=15, b1=b1)
    b6 = BS(b5.content, "html.parser")
    b7 = b6.find_all("div", class_="promo-title text-center h1")
    b8 = b6.find_all("div", class_="promo-discountValue text-center h1 has-image")[4]
    for title in b7:
        if "Oil" in title.text.strip():
            b4["lehmans"]["url"] = url[0:29]
            b4["lehmans"]["product"] = title.text.strip()
            b4["lehmans"]["price"] = b8.text[1:8]
    print(pd.DataFrame.from_dict(b4, b9 = 'index'))
fonk1(b3[0])
fonk2(b3[1])