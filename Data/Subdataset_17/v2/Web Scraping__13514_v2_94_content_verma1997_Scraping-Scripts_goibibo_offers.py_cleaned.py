import csv
import random
import requests
import schedule
import time
from bs4 import BeautifulSoup
USER_AGENTS = [
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
def get_random_header():
    return {'User-Agent': random.choice(USER_AGENTS)}
def fetch_offers():
    url = "https:
    response = requests.get(url, headers=get_random_header())
    page_soup = BeautifulSoup(response.text, "html.parser")
    offers = [offer.p.text.replace(",", "") for offer in page_soup.find_all("div", {"class": "bot-section"})]
    links = ["https:
    promos = [promo.text for promo in page_soup.find_all("div", {"class": "promocode"})]
    terms_conditions = [terms.li.text.replace(",", "") for terms in page_soup.find_all("div", {"class": "tnc-section"})]
    save_to_csv(offers, links, promos, terms_conditions)
def save_to_csv(offers, links, promos, terms_conditions):
    filename = "goibibo_offers.csv"
    with open(filename, "a", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Offer Name", "Link", "Promocode", "Description", "Booking Channel"])
        for offer, link, promo, term in zip(offers, links, promos, terms_conditions):
            writer.writerow([offer, link, promo, term])
schedule.every().day.at("10:00").do(fetch_offers)
while True:
    schedule.run_pending()
    time.sleep(1)