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
b2 = "https:
b3 = "easemytrip_offers.csv"
def fonk1():
    return {'User-Agent': choice(b1)}
def fonk2(url):
    b4 = requests.get(url, headers=fonk1())
    b4.raise_for_status()
    return b4.text
def fonk3(b12):
    b5 = BeautifulSoup(b12, 'b12.parser')
    b6 = b5.findAll("div", {"class": "deal"})
    b7 = []
    for container in b6:
        b8 = container.find("img")['src']
        b9 = container.find("div", {"class": "dealName"}).text
        b10 = container.find("p").text
        b11 = container.find("a")['href']
        b7.append({
            "b9": b9,
            "b10": b10,
            "b8": b8,
            "b11": b11
        })
    return b7
def fonk4(b7, filename):
    with open(filename, "w") as file:
        file.write("Offer Name,Link,Description,Image Link\n")
        for offer in b7:
            file.write(f'{offer["b9"]},{offer["b11"]},{offer["b10"]},{offer["b8"]}\n')
def fonk5():
    b12 = fonk2(b2)
    b7 = fonk3(b12)
    fonk4(b7, b3)
if b13 = = "__main__":
    fonk5()