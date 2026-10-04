import csv
import requests
from random import choice
from bs4 import BeautifulSoup
from datetime import datetime
USER_AGENTS = [
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
def get_random_header():
    return {'User-Agent': choice(USER_AGENTS)}
def scrape_goibibo_offers():
    url = "https:
    response = requests.get(url, headers=get_random_header())
    soup = BeautifulSoup(response.text, "html.parser")
    offer_containers = soup.findAll("div", {"class": "bot-section"})
    promo_containers = soup.findAll("div", {"class": "back-content"})
    offers = [offer.p.text.replace(",", "") for offer in offer_containers]
    links = ["https:
    promos = []
    terms_conditions = []
    for content in promo_containers:
        promo_content = content.find_all("div", {"class": "back-content-top-inner"})
        conditions = content.find_all("div", {"class": "tnc-section"})
        for term in conditions:
            terms_conditions.append(term.li.text.replace(",", ""))
        for promo in promo_content:
            promo_code = promo.find_all("div", {"class": "promocode"})
            for promo_text in promo_code:
                promos.append(promo_text.text)
    with open("goibibo_offers.csv", "a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Offer Name", "Link", "Promocode", "Description", "Booking Channel"])
        for i in range(len(offer_containers)):
            writer.writerow([offers[i], links[0], promos[i], terms_conditions[i]])
def job():
    scrape_goibibo_offers()
