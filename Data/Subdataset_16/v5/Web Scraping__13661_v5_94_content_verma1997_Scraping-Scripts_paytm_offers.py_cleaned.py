import requests
from random import choice
from bs4 import BeautifulSoup
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
def fonk2(b10):
    b2 = requests.get(b10, headers=fonk1())
    b2.raise_for_status()
    return b2.text
def fonk3(b12):
    b3 = b12.find_all("li", class_="slider-slide")
    b4 = []
    b5 = []
    b6 = []
    for offer in b3:
        b7 = offer.find("a")['href']
        b8 = offer.img['src']
        b9 = offer.find("p", class_="PromoCode").text.replace("Use b9 : ", "")
        b4.append(b7)
        b5.append(b8)
        b6.append(b9)
    return b4, b5, b6
def fonk4(filename, headers, b13):
    with open(filename, "a") as file:
        file.write(headers)
        for row in b13:
            file.write(",".join(row) + "\n")
def fonk5():
    b10 = "https:
    b11 = fonk2(b10)
    b12 = BeautifulSoup(b11, 'html.parser')
    b4, b5, b6 = fonk3(b12)
    b13 = list(zip(b4, b5, b6))
    b14 = "Link,Image Link,Promocode\n"
    fonk4("paytm_offers.csv", b14, b13)
if b15 = = "__main__":
    fonk5()