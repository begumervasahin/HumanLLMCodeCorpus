import csv
import random
import requests
import schedule
import time
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
    return {'User-Agent': random.choice(b1)}
def fonk2():
    b2 = "https:
    b3 = requests.get(b2, headers=fonk1())
    b4 = BeautifulSoup(b3.text, "html.parser")
    b5 = fonk3(b4)
    b9, b10, b6 = fonk4(b4)
    fonk5(b5, b9, b10, b6)
def fonk3(b4):
    b7 = b4.find_all("div", {"class": "bot-section"})
    return [offer.p.text.replace(",", "") for offer in b7]
def fonk4(b4):
    b8 = b4.find_all("div", {"class": "back-content"})
    b9 = ["https:
    b10 = []
    b6 = []
    for section in b8:
        b10 += [promo.text for promo in section.find_all("div", {"class": "promocode"})]
        b6 += [terms.li.text.replace(",", "") for terms in section.find_all("div", {"class": "tnc-section"})]
    return b9, b10, b6
def fonk5(b5, b9, b10, b6):
    b11 = "goibibo_offers.csv"
    with open(b11, "a", b12 = '') as file:
        b13 = csv.b13(file)
        b13.writerow(["Offer Name", "Link", "Promocode", "Description", "Booking Channel"])
        for offer, link, promo, term in zip(b5, b9, b10, b6):
            b13.writerow([offer, link, promo, term])
schedule.every().day.at("10:00").do(fetch_offers)
while True:
    schedule.run_pending()
    time.sleep(1)