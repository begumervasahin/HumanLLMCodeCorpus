from bs4 import BeautifulSoup as BS
import requests
import pandas as pd
b1 = {
        'user-agent': 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
        'referrer': 'https:
        'Accept': 'text/html,application/xhtml+xml,application/xml;b2 = 0.9,image/webp,image/apng,*/*;b2=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;b2 = 0.9',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache'
    }
a1 = 0
b3 = [
    "https:
    "https:
       ]
def fonk1(url):
    b4 = {}
    b4["miami"] = {}
    b5 = []
    b6 = requests.get(url, timeout=15, b1=b1)
    b7 = BS(b6.content, "html.parser")
    b8 = b7.find_all("div", class_="promo-b5 text-center h1")
    b9 = b7.find_all("div", class_="promo-discountValue text-center h1 has-image")[2]
    for tag in b8:
        if "OIL" in tag.text.strip():
            b4["miami"]["url"] = url[0:29]
            b4["miami"]["product"] = tag.text.strip()
            b4["miami"]["price"]  = b9.text[1:8]
    print(pd.DataFrame.from_dict(b4, b10 = 'index'))
def fonk2(url):
    b4 = {}
    b4["lehmans"] = {}
    b5 = []
    b6 = requests.get(url, timeout=15, b1=b1)
    b7 = BS(b6.content, "html.parser")
    b8 = b7.find_all("div", class_="promo-b5 text-center h1")
    b9 = b7.find_all("div", class_="promo-discountValue text-center h1 has-image")[4]
    for tag in b8:
        if "Oil" in tag.text.strip():
            b4["lehmans"]["url"] = url[0:29]
            b4["lehmans"]["product"] = tag.text.strip()
            b4["lehmans"]["price"]  = b9.text[1:8]
    print(pd.DataFrame.from_dict(b4, b10 = 'index'))
fonk1(b3[0])
fonk2(b3[1])