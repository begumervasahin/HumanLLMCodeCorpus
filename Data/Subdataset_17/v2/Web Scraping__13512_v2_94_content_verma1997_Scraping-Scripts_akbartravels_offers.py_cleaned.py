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
def get_header():
    return {'User-Agent': choice(USER_AGENTS)}
URL = "https:
response = requests.get(URL, headers=get_header())
soup = BeautifulSoup(response.text, 'html.parser')
def extract_offers(soup):
    containers = soup.find_all("div", class_=["deals-cntent-left", "deals-cntent-center", "deals-cntent-right"])
    offers = []
    for container in containers:
        image = container.find("img")['src']
        title = container.find("div", class_="deals-cntent-name").text.strip()
        description = container.find("div", class_="deals-cntent-disc").text.strip()
        validity = container.find("div", class_="deals-box-ftr-left").text.strip()
        offers.append({
            "Offer Name": title.replace(",", ""),
            "Image Link": image,
            "Description": description.replace(",", ""),
            "Validity": validity
        })
    return offers
def save_offers_to_csv(offers, filename="akbartravels_offers.csv"):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["Offer Name", "Image Link", "Description", "Validity"])
        writer.writeheader()
        for offer in offers:
            writer.writerow(offer)
if __name__ == "__main__":
    offers = extract_offers(soup)
    save_offers_to_csv(offers)
    print("Offers have been successfully saved to akbartravels_offers.csv")