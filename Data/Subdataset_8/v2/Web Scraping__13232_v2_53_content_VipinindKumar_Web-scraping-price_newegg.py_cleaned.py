import re
import requests
from bs4 import BeautifulSoup
def scrape_newegg_laptops(url):
    response = requests.get(url)
    if response.status_code == 200:
        page_soup = BeautifulSoup(response.content, 'html.parser')
        with open('data/newegg-laptops.csv', 'w') as file:
            file.write('Brand,Name,Price-was,Current-Price,Discount(%),RAM(GB),Storage(GB/TB),Refurbished(0/1),URL\n')
            laptops = page_soup.findAll('div', {'class': 'item-container'})
            for laptop in laptops:
                try:
                    brand = laptop.find('div', 'item-info').div.a.img['title']
                except:
                    brand = 'NaN'
                title = laptop.findAll('a', {'class': 'item-title'})[0].text
                if ('refurbished' in title.lower()) or ('renewed' in title.lower()):
                    refurbished = '1'
                else:
                    refurbished = '0'
                link = laptop.findAll('a', {'class': 'item-title'})[0]['href']
                features = title.replace(' ', '')
                features = re.search('.*(?:\)|\w|-)(\d+)GB.*(?:y|\+|-|M)(\d+)', features)
                try:
                    ram = features.group(1)
                    storage = features.group(2)
                except:
                    ram = 'NaN'
                    storage = 'NaN'
                try:
                    price_was = laptop.find('div', 'item-info').find('div', 'item-action').ul.li.span.text
                    discount = laptop.find('div', 'item-info').find('div', 'item-action').ul.find('li', 'price-save').find('span', 'price-save-percent').text[:-1]
                except:
                    price_was = 'NaN'
                    discount = '0'
                try:
                    current_price = laptop.find('div', 'item-info').find('div', 'item-action').ul.find('li', 'price-current').text
                    current_price = current_price.replace(',', '')
                    current_price = re.search('.+\s([0-9]+).+', current_price).group(1)
                except:
                    current_price = 'NaN'
                file.write(f"{brand},{title.replace(',', ' ')},{price_was},{current_price},{discount},{ram},{storage},{refurbished},{link}\n")
        print('Scraped Newegg\'s page')
    else:
        print('Failed to fetch the page')
def egg_urls(url):
    response = requests.get(url)
    if response.status_code == 200:
        page_soup = BeautifulSoup(response.content, 'html.parser')
        last_page = egg_last(page_soup)
        urls = [f'https:
        return urls
    else:
        print('Failed to fetch the page')
def egg_last(page_soup):
    last_page_element = page_soup.find_all('div', {'class': 'page_NavigationBar'})[1].select_one('div:nth-of-type(10)').text.strip()
    return int(last_page_element)
starting_url = 'https:
scrape_newegg_laptops(starting_url)
additional_urls = egg_urls(starting_url)
print("Additional pages to scrape:", additional_urls)