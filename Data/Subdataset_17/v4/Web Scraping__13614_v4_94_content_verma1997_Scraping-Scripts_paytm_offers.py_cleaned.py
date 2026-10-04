import requests
from random import choice
from bs4 import BeautifulSoup
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
def get_random_header():
    return {'User-Agent': choice(HEADERS)}
def fetch_page_content(url):
    response = requests.get(url, headers=get_random_header())
    return response.text
def extract_offer_data(soup):
    offers = soup.find_all("li", class_="slider-slide")
    offer_links = []
    offer_images = []
    offer_promocodes = []
    for offer in offers:
        link = offer.find("a")['href']
        image = offer.img['src']
        promocode = offer.find("p", class_="PromoCode").text.replace("Use promocode : ", "")
        offer_links.append(link)
        offer_images.append(image)
        offer_promocodes.append(promocode)
    return offer_links, offer_images, offer_promocodes
def save_to_csv(filename, headers, data):
    with open(filename, "a") as file:
        file.write(headers)
        for row in data:
            file.write(",".join(row) + "\n")
def main():
    url = "https:
    html_content = fetch_page_content(url)
    soup = BeautifulSoup(html_content, 'html.parser')
    offer_links, offer_images, offer_promocodes = extract_offer_data(soup)
    data = list(zip(offer_links, offer_images, offer_promocodes))
    headers = "Link,Image Link,Promocode\n"
    save_to_csv("paytm_offers.csv", headers, data)
if __name__ == "__main__":
    main()