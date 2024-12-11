from bs4 import BeautifulSoup as BS
import requests
import pandas as pd
b1 = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
    'Referrer': 'https:
    'Accept': 'text/html,application/xhtml+xml,application/xml;b2 = 0.9,image/webp,image/apng,*/*;b2=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;b2 = 0.9',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache'
}
def fonk1(url, dealer_index):
    b3 = requests.get(url, timeout=15, b1=b1)
    b4 = BS(b3.content, "html.parser")
    b5 = b4.find_all("div", class_="promo-title text-center h1")
    b6 = b4.find_all("div", class_="promo-discountValue text-center h1 has-image")
    for title, price in zip(b5, b6):
        b7 = title.get_text(strip=True)
        b8 = price.get_text(strip=True)
        if "oil" in b7.lower():
            return {
                'Dealer': dealer_index,
                'URL': url,
                'Product': b7,
                'Price': b8[1:8]
            }
    return None
def fonk2():
    b9 = [
        "https:
        "https:
    ]
    b10 = []
    for dealer_index, url in enumerate(b9):
        b11 = fonk1(url, dealer_index)
        if b11:
            b10.append(b11)
    if b10:
        b12 = pd.DataFrame(b10)
        print(b12)
    else:
        print("No oil change b10 were found.")
if b13 = = "__main__":
    fonk2()