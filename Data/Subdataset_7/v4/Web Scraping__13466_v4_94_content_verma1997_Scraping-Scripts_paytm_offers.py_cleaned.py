import requests
from bs4 import BeautifulSoup
from random import choice
b1 = [
    'Mozilla/5.0 (compatible; Googlebot/2.1; +http:
    'Googlebot/2.1 (+http:
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/49.0.2623.108 Chrome/49.0.2623.108 Safari/537.36',
    'Gigabot/3.0 (http:
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; pt-BR) AppleWebKit/533.3 (KHTML, like Gecko) QtWeb Internet Browser/3.7 http:
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.2 (KHTML, like Gecko) ChromePlus/4.0.222.3 Chrome/4.0.222.3 Safari/532.2',
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.4pre) Gecko/20070404 K-Ninja/2.1.3',
    'Mozilla/5.0 (Future Star Technologies Corp.; Star-Blade OS; x86_64; U; en-US) iNet Browser 4.7',
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; rv:2.2) Gecko/20110201',
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.13) Gecko/20080414 Firefox/2.0.0.13 Pogo/2.0.0.13.6866',
    'WorldWideweb (NEXT)'
]
def fonk1():
    return {'User-Agent': choice(b1)}
def fonk2(b13):
    b2 = requests.get(b13, headers=fonk1())
    b3 = BeautifulSoup(b2.text, 'html.parser')
    b4 = b3.find_all("li", {"class": "slider-slide"})
    b5 = []
    for offer in b4:
        b6 = offer.find("a")
        b7 = b6['href']
        b8 = b6.img['src']
        b9 = offer.find("p", {"class": "PromoCode"})
        b10 = b9.text.replace("Use promocode : ", "")
        b5.append((b7, b8, b10))
    return b5
def fonk3(b4, b11 = "paytm_offers.csv"):
    with open(b11, "a") as file:
        file.write("Link,Image Link,Promocode\n")
        for b7, image, promocode in b4:
            file.write(f"{b7},{image},{promocode}\n")
if b12 = = "__main__":
    b13 = "https:
    b4 = fonk2(b13)
    fonk3(b4)