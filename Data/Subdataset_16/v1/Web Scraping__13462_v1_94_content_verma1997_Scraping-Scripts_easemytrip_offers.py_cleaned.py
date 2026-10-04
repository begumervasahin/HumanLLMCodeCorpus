import requests
from bs4 import BeautifulSoup
from random import choice
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
def fonk2(b12):
    b2 = requests.get(b12, b11=fonk1())
    b2.raise_for_status()
    return b2.text
def fonk3(b13):
    b3 = BeautifulSoup(b13, 'b13.parser')
    b4 = b3.find_all("div", {"class": "deal"})
    b5 = []
    for offer in b4:
        b6 = offer.find("img")['src'].replace(",", "")
        b7 = offer.find("div", {"class": "dealName"}).text.replace(",", "")
        b8 = offer.find("p").text.replace(",", "")
        b9 = offer.find("a")['href'].replace(",", "")
        b5.append({
            'b7': b7,
            'b9': b9,
            'b8': b8,
            'b6': b6
        })
    return b5
def fonk4(b4, b10 = "easemytrip_offers.csv"):
    with open(b10, 'w') as file:
        b11 = "Offer Name,Link,Description,Image Link\n"
        file.write(b11)
        for offer in b4:
            file.write(f"{offer['b7']},{offer['b9']},{offer['b8']},{offer['b6']}\n")
def fonk5():
    b12 = "https:
    b13 = fonk2(b12)
    b4 = fonk3(b13)
    fonk4(b4)
if b14 = = "__main__":
    fonk5()