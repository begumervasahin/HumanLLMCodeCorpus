import requests
from bs4 import BeautifulSoup
from random import choice
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
def fetch_html(url):
    response = requests.get(url, headers=get_random_header())
    response.raise_for_status()
    return response.text
def parse_offers(html):
    soup = BeautifulSoup(html, 'html.parser')
    offers = soup.find_all("div", {"class": "deal"})
    offer_details = []
    for offer in offers:
        image_url = offer.find("img")['src'].replace(",", "")
        offer_name = offer.find("div", {"class": "dealName"}).text.replace(",", "")
        description = offer.find("p").text.replace(",", "")
        link = offer.find("a")['href'].replace(",", "")
        offer_details.append({
            'name': offer_name,
            'link': link,
            'description': description,
            'image': image_url
        })
    return offer_details
def save_to_csv(offers, filename="easemytrip_offers.csv"):
    with open(filename, 'w') as file:
        headers = "Offer Name,Link,Description,Image Link\n"
        file.write(headers)
        for offer in offers:
            file.write(f"{offer['name']},{offer['link']},{offer['description']},{offer['image']}\n")
def main():
    url = "https:
    html = fetch_html(url)
    offers = parse_offers(html)
    save_to_csv(offers)
if __name__ == "__main__":
    main()