import re
import requests
from bs4 import BeautifulSoup
def scrape_newegg_laptops(url):
    response = requests.get(url)
    if response.status_code == 200:
        page_soup = BeautifulSoup(response.content, 'html.parser')
        with open('data/newegg-laptops.csv', 'w') as file:
            file.write('Brand,Name,Price-was,Current-Price,Discount(%),RAM(GB),Storage(GB/TB),Refurbished(0/1),URL\n')
            laptops = page_soup.find_all('div', {'class': 'item-container'})
            for laptop in laptops:
                brand = laptop.find('div', 'item-info').div.a.img.get('title', 'NaN')
                title = laptop.find('a', {'class': 'item-title'}).text
                refurbished = '1' if 'refurbished' in title.lower() or 'renewed' in title.lower() else '0'
                link = laptop.find('a', {'class': 'item-title'})['href']
                features = re.search('.*(?:\)|\w|-)(\d+)GB.*(?:y|\+|-|M)(\d+)', title.replace(' ', ''))
                ram, storage = features.groups() if features else ('NaN', 'NaN')
                try:
                    price_was = laptop.find('li', 'price-save').span.text
                    discount = laptop.find('span', 'price-save-percent').text[:-1]
                except AttributeError:
                    price_was, discount = 'NaN', '0'
                try:
                    current_price = re.search('.+\s([0-9]+).+', laptop.find('li', 'price-current').text.replace(',', '')).group(1)
                except AttributeError:
                    current_price = 'NaN'
                file.write(f"{brand},{title.replace(',', ' ')},{price_was},{current_price},{discount},{ram},{storage},{refurbished},{link}\n")
        print('Scraped Newegg\'s page')
    else:
        print('Failed to fetch the page')
def egg_urls(url):
    response = requests.get(url)
    if response.status_code == 200:
        page_soup = BeautifulSoup(response.content, 'html.parser')
        last_page = int(page_soup.find_all('div', {'class': 'page_NavigationBar'})[1].select_one('div:nth-of-type(10)').text.strip())
        return [f'https:
    else:
        print('Failed to fetch the page')
starting_url = 'https:
scrape_newegg_laptops(starting_url)
additional_urls = egg_urls(starting_url)
print("Additional pages to scrape:", additional_urls)