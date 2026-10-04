import requests
from bs4 import BeautifulSoup
from random import choice
headers = [
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
    return {'User-Agent': choice(headers)}
url = "https:
response = requests.get(url, headers=get_header())
soup = BeautifulSoup(response.text, 'html.parser')
def scrape_indigo_offers():
    containers = soup.findAll("div", {"class": "commonBottomAdon"})
    total_offers = len(containers)
    offer_links = []
    offer_images = []
    offer_names = []
    offer_descriptions = []
    for container in containers:
        link = container.find("a")['href']
        image = container.find("img")['src']
        name = container.find("h6").text.replace(",", "")
        description = container.find("p").text.replace(",", "")
        offer_links.append(link)
        offer_images.append("https:
        offer_names.append(name)
        offer_descriptions.append(description)
    filename = "indigo_offers.csv"
    with open(filename, "a", encoding="utf-8") as file:
        headers = "Offer Name,Link,Description,Image Link\n"
        file.write(headers)
        for i in range(total_offers):
            file.write(f"{offer_names[i]},{offer_links[i]},{offer_descriptions[i]},{offer_images[i]}\n")
scrape_indigo_offers()