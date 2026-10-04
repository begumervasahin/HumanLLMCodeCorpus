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
def fonk2(b11):
    b2 = requests.get(b11, b9=fonk1())
    return BeautifulSoup(b2.text, 'html.parser')
def fonk3(b12):
    b3 = b12.find_all("div", {"class": ["deals-cntent-left", "deals-cntent-center", "deals-cntent-right"]})
    b4 = []
    for container in b3:
        b5 = container.find("img")['src']
        b6 = container.find("div", {"class": "deals-cntent-name"}).text.strip()
        b7 = container.find("div", {"class": "deals-cntent-disc"}).text.strip()
        b8 = container.find("div", {"class": "deals-box-ftr-left"}).text.strip()
        b4.append({
            'name': b6,
            'b5': b5,
            'b7': b7,
            'b8': b8
        })
    return b4
def fonk4(b4, filename):
    with open(filename, 'w') as f:
        b9 = "Offer Name,Image Link,Description,Validity\n"
        f.write(b9)
        for offer in b4:
            b10 = f"{offer['name']},{offer['b5']},{offer['b7']},{offer['b8']}\n"
            f.write(b10)
def fonk5():
    b11 = "https:
    b12 = fonk2(b11)
    b4 = fonk3(b12)
    fonk4(b4, "akbartravels_offers.csv")
if b13 = = "__main__":
    fonk5()