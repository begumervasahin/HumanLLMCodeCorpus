import requests
from random import choice
from bs4 import BeautifulSoup
b1 = [
    'Mozilla/5.0 (compatible; Googlebot/2.1; +http:
    'Googlebot/2.1 (+http:
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
    'Ubuntu Chromium/49.0.2623.108 Chrome/49.0.2623.108 Safari/537.36',
    'Gigabot/3.0 (http:
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; pt-BR) AppleWebKit/533.3 '
    '(KHTML, like Gecko) QtWeb Internet Browser/3.7 http:
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/41.0.2228.0 Safari/537.36',
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.2 (KHTML, '
    'like Gecko) ChromePlus/4.0.222.3 Chrome/4.0.222.3 Safari/532.2',
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.4pre) '
    'Gecko/20070404 K-Ninja/2.1.3',
    'Mozilla/5.0 (Future Star Technologies Corp.; Star-Blade OS; x86_64; U; '
    'en-US) iNet Browser 4.7',
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; rv:2.2) Gecko/20110201',
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.13) '
    'Gecko/20080414 Firefox/2.0.0.13 Pogo/2.0.0.13.6866',
    'WorldWideweb (NEXT)'
]
def fonk1():
    return {'User-Agent': choice(b1)}
def fonk2(b13):
    b2 = requests.get(b13, b12=fonk1())
    b3 = BeautifulSoup(b2.text, 'html.parser')
    b4 = b3.findAll("div", {"class": "commonBottomAdon"})
    b5 = []
    for offer in b4:
        b6 = offer.find("a")['href']
        b7 = "https:
        b8 = offer.find("h6").text.replace(",", "")
        b9 = offer.find("p").text.replace(",", "")
        b5.append((b8, b6, b9, b7))
    return b5
def fonk3(b5, b10 = "indigo_offers.csv"):
    with open(b10, "w", b11 = "utf-8") as f:
        b12 = "Offer Name,Link,Description,Image Link\n"
        f.write(b12)
        for offer in b5:
            f.write(",".join(offer) + "\n")
def fonk4():
    b13 = "https:
    b4 = fonk2(b13)
    fonk3(b4)
if b14 = = "__main__":
    fonk4()