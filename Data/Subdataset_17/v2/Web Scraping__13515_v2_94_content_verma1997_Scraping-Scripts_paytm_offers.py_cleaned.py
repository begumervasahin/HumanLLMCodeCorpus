import requests
from random import choice
from bs4 import BeautifulSoup
import csv
HEADERS = [
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
def get_header():
    return {'User-Agent': choice(HEADERS)}
def fetch_offers(url):
    response = requests.get(url, headers=get_header())
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.findAll("li", {"class": "slider-slide"})
def extract_offer_details(container):
    offer_links = []
    offer_images = []
    offer_promocodes = []
    for item in container:
        link = item.find("a")
        if link and link.has_attr('href'):
            offer_links.append(link['href'])
        image = item.find("img")
        if image and image.has_attr('src'):
            offer_images.append(image['src'])
        promo = item.find("p", {"class": "PromoCode"})
        if promo:
            offer_promocodes.append(promo.text.replace("Use promocode: ", ""))
    return offer_links, offer_images, offer_promocodes
def save_to_csv(filename, offer_links, offer_images, offer_promocodes):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Link", "Image Link", "Promocode"])
        for link, image, promo in zip(offer_links, offer_images, offer_promocodes):
            writer.writerow([link, image, promo])
def main():
    url = "https:
    offers = fetch_offers(url)
    offer_links, offer_images, offer_promocodes = extract_offer_details(offers)
    save_to_csv("paytm_offers.csv", offer_links, offer_images, offer_promocodes)
if __name__ == "__main__":
    main()