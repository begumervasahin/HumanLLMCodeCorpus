import csv
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
def fonk2(b14):
    b2 = requests.get(b14, b11=fonk1())
    return BeautifulSoup(b2.text, "html.parser")
def fonk3(b15):
    b3 = b15.findAll("div", {"class": "bot-section"})
    b4 = b15.findAll("div", {"class": "back-content"})
    b5 = [offer.p.text.replace(",", "") for offer in b3]
    b6 = ["https:
    promos, b7 = [], []
    for content in b4:
        b8 = content.find_all("div", {"class": "back-content-top-inner"})
        b9 = content.find_all("div", {"class": "tnc-section"})
        for term in b9:
            b7.append(term.li.text.replace(",", ""))
        for promo in b8:
            b10 = promo.find_all("div", {"class": "promocode"})
            for promo_text in b10:
                promos.append(promo_text.text)
    return b5, b6, promos, b7
def fonk4(filename, b16):
    b11 = ["Offer Name", "Link", "Promocode", "Description", "Booking Channel"]
    with open(filename, "a", b12 = '') as file:
        b13 = csv.b13(file)
        b13.writerow(b11)
        for row in b16:
            b13.writerow(row)
def fonk5():
    b14 = "https:
    b15 = fonk2(b14)
    b5, b6, promos, b7 = fonk3(b15)
    b16 = [
        [b5[i], b6[0], promos[i], b7[i], "Booking Channel"]
        for i in range(len(b5))
    ]
    fonk4("goibibo_offers.csv", b16)
def fonk6():
    fonk5()
