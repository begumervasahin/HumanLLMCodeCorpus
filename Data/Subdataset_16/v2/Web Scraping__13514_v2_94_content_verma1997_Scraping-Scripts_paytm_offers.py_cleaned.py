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
def fonk2(b12):
    b2 = requests.get(b12, headers=fonk1())
    b3 = BeautifulSoup(b2.text, 'html.parser')
    return b3.findAll("li", {"class": "slider-slide"})
def fonk3(container):
    b4 = []
    b5 = []
    b6 = []
    for item in container:
        b7 = item.find("a")
        if b7 and b7.has_attr('href'):
            b4.append(b7['href'])
        b8 = item.find("img")
        if b8 and b8.has_attr('src'):
            b5.append(b8['src'])
        b9 = item.find("p", {"class": "PromoCode"})
        if b9:
            b6.append(b9.text.replace("Use promocode: ", ""))
    return b4, b5, b6
def fonk4(filename, b4, b5, b6):
    with open(filename, b10 = 'w', newline='') as file:
        b11 = csv.b11(file)
        b11.writerow(["Link", "Image Link", "Promocode"])
        for b7, b8, b9 in zip(b4, b5, b6):
            b11.writerow([b7, b8, b9])
def fonk5():
    b12 = "https:
    b13 = fonk2(b12)
    b4, b5, b6 = fonk3(b13)
    fonk4("paytm_offers.csv", b4, b5, b6)
if b14 = = "__main__":
    fonk5()