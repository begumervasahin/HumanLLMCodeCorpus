import requests
from random import choice
from bs4 import BeautifulSoup
import csv
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
def get_random_user_agent():
    return {'User-Agent': choice(USER_AGENTS)}
def fetch_offers(url):
    response = requests.get(url, headers=get_random_user_agent())
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.find_all("li", class_="slider-slide")
def extract_offer_details(containers):
    offer_links = []
    offer_images = []
    offer_promocodes = []
    for item in containers:
        link_tag = item.find("a")
        if link_tag and link_tag.has_attr('href'):
            offer_links.append(link_tag['href'])
        img_tag = item.find("img")
        if img_tag and img_tag.has_attr('src'):
            offer_images.append(img_tag['src'])
        promo_tag = item.find("p", class_="PromoCode")
        if promo_tag:
            offer_promocodes.append(promo_tag.text.replace("Use promocode: ", ""))
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