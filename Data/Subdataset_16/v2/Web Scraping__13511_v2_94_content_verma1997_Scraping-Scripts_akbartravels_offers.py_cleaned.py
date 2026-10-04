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
b2 = "https:
b3 = requests.get(b2, headers=fonk1())
b4 = BeautifulSoup(b3.text, 'html.parser')
def fonk2(b4):
    b5 = b4.find_all("div", class_=["deals-cntent-left", "deals-cntent-center", "deals-cntent-right"])
    b6 = []
    for container in b5:
        b7 = container.find("img")['src']
        b8 = container.find("div", class_="deals-cntent-name").text.strip()
        b9 = container.find("div", class_="deals-cntent-disc").text.strip()
        b10 = container.find("div", class_="deals-box-ftr-left").text.strip()
        b6.append({
            "Offer Name": b8.replace(",", ""),
            "Image Link": b7,
            "Description": b9.replace(",", ""),
            "Validity": b10
        })
    return b6
def fonk3(b6, b11 = "akbartravels_offers.csv"):
    with open(b11, b12 = 'w', newline='', encoding='utf-8') as file:
        b13 = csv.DictWriter(file, fieldnames=["Offer Name", "Image Link", "Description", "Validity"])
        b13.writeheader()
        for offer in b6:
            b13.writerow(offer)
if b14 = = "__main__":
    b6 = fonk2(b4)
    fonk3(b6)
    print("Offers have been successfully saved to akbartravels_offers.csv")