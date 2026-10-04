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
def fonk2(b7):
    b2 = requests.get(b7, headers=fonk1())
    b2.raise_for_status()
    return BeautifulSoup(b2.text, 'html.parser')
def fonk3(b8):
    b3 = b8.findAll("div", {"class": "commonBottomAdon"})
    b4 = []
    for container in b3:
        b5 = {
            "name": container.find("h6").text.replace(",", ""),
            "link": container.find("a")['href'],
            "description": container.find("p").text.replace(",", ""),
            "image_link": "https:
        }
        b4.append(b5)
    return b4
def fonk4(b4, filename):
    with open(filename, "a", b6 = "utf-8") as file:
        file.write("Offer Name,Link,Description,Image Link\n")
        for b5 in b4:
            file.write(f"{b5['name']},{b5['link']},{b5['description']},{b5['image_link']}\n")
def fonk5():
    b7 = "https:
    b8 = fonk2(b7)
    b4 = fonk3(b8)
    fonk4(b4, "indigo_offers.csv")
if b9 = = "__main__":
    fonk5()