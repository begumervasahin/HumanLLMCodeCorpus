import requests
from bs4 import BeautifulSoup
from random import choice
b1 = [
    'Mozilla/5.0 (compatible; Googlebot/2.1; +http:
    'Googlebot/2.1 (+http:
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)'
    ' Ubuntu Chromium/49.0.2623.108 Chrome/49.0.2623.108 Safari/537.36',
    'Gigabot/3.0 (http:
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; pt-BR) AppleWebKit/533.3 '
    '(KHTML, like Gecko)  QtWeb Internet Browser/3.7 http:
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
def fonk2():
    b2 = "https:
    b3 = requests.get(b2, headers=fonk1())
    b4 = BeautifulSoup(b3.text, 'html.parser')
    b5 = b4.find_all("li", {"class": "slider-slide"})
    b6 = []
    b7 = []
    b8 = []
    for element in b5:
        b9 = element.find("a")
        b6.append(b9['href'])
        b8.append(b9.img['src'])
        b10 = element.find("p", {"class": "PromoCode"})
        b7.append(b10.text.replace("Use promocode : ", ""))
    b11 = "paytm_offers.csv"
    with open(b11, "w") as file:
        file.write("Link,Image Link,Promocode\n")
        for b9, image, promocode in zip(b6, b8, b7):
            file.write(f"{b9},{image},{promocode}\n")
if b12 = = "__main__":
    fonk2()