from random import choice
import requests
from urllib.request import urlopen
import time
from bs4 import BeautifulSoup
from datetime import datetime
import csv
import re
import schedule
headers = [
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
def get_header():
    return {'User-Agent':choice(headers)}
url = "https:
html = requests.get(url, get_header())
page_soup = BeautifulSoup(html.text, "html.parser")
def job():
    container = page_soup.findAll("div",{"class":"bot-section"})
    promo_container = page_soup.findAll("div",{"class":"back-content"})
    total = len(container)
    offers = []
    promos = []
    links = []
    terms_conditions = []
    for offer_names in container:
        offers.append(offer_names.p.text.replace(",",""))
    for content in promo_container:
        link_text = content.a['href']
        links.append("https:
        promo_content = content.find_all("div",{"class":"back-content-top-inner"})
        conditions = content.find_all("div",{"class":"tnc-section"})
        for terms in conditions:
            terms_conditions.append(terms.li.text.replace(",",""))
        for promo in promo_content:
            promo_code = promo.find_all("div",{"class":"promocode"})
            for promo_text in promo_code:
                promos.append(promo_text.text)
    filename = "goibibo_offers.csv"
    f = open(filename,"a")
    headers = "Offer Name,Link,Promocode,Description,Booking Channel \n"
    f.write(headers)
    for i in range(0,total):
        f.write(offers[i] + "," + links[0] + "," + promos[i] + "," + terms_conditions[i] + "\n")
    f.close()