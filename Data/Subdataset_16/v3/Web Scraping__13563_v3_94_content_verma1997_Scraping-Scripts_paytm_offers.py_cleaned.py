import requests
from random import choice
from bs4 import BeautifulSoup
import csv
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
    return b3.find_all("li", b4 = "slider-slide")
def fonk3(containers):
    b5 = []
    b6 = []
    b7 = []
    for item in containers:
        b8 = item.find("a")
        if b8 and b8.has_attr('href'):
            b5.append(b8['href'])
        b9 = item.find("img")
        if b9 and b9.has_attr('src'):
            b6.append(b9['src'])
        b10 = item.find("p", b4="PromoCode")
        if b10:
            b7.append(b10.text.replace("Use promocode: ", ""))
    return b5, b6, b7
def fonk4(filename, b5, b6, b7):
    with open(filename, b11 = 'w', newline='') as file:
        b12 = csv.b12(file)
        b12.writerow(["Link", "Image Link", "Promocode"])
        for link, image, promo in zip(b5, b6, b7):
            b12.writerow([link, image, promo])
def fonk5():
    b13 = "https:
    b14 = fonk2(b13)
    b5, b6, b7 = fonk3(b14)
    fonk4("paytm_offers.csv", b5, b6, b7)
if b15 = = "__main__":
    fonk5()