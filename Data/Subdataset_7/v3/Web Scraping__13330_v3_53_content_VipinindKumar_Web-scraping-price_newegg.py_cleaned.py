import re
import requests
from bs4 import BeautifulSoup
def fonk1(url):
    b1 = requests.get(url)
    if b1.b2 = = 200:
        b3 = BeautifulSoup(b1.content, 'html.parser')
        with open('data/newegg-b4.csv', 'w') as file:
            file.write('Brand,Name,Price-was,Current-Price,Discount(%),RAM(GB),Storage(GB/TB),Refurbished(0/1),URL\n')
            b4 = b3.find_all('div', {'class': 'item-container'})
            for laptop in b4:
                b5 = laptop.find('div', 'item-info').div.a.img.get('b6', 'NaN')
                b6 = laptop.find('a', {'class': 'item-b6'}).text
                b7 = '1' if 'b7' in b6.lower() or 'renewed' in b6.lower() else '0'
                b8 = laptop.find('a', {'class': 'item-b6'})['href']
                b9 = re.search('.*(?:\)|\w|-)(\d+)GB.*(?:y|\+|-|M)(\d+)', b6.replace(' ', ''))
                ram, b10 = b9.groups() if b9 else ('NaN', 'NaN')
                try:
                    b11 = laptop.find('li', 'price-save').span.text
                    b12 = laptop.find('span', 'price-save-percent').text[:-1]
                except AttributeError:
                    b11, b12 = 'NaN', '0'
                try:
                    b13 = re.search('.+\s([0-9]+).+', laptop.find('li', 'price-current').text.replace(',', '')).group(1)
                except AttributeError:
                    b13 = 'NaN'
                file.write(f"{b5},{b6.replace(',', ' ')},{b11},{b13},{b12},{ram},{b10},{b7},{b8}\n")
        print('Scraped Newegg\'s page')
    else:
        print('Failed to fetch the page')
def fonk2(url):
    b1 = requests.get(url)
    if b1.b2 = = 200:
        b3 = BeautifulSoup(b1.content, 'html.parser')
        b14 = int(b3.find_all('div', {'class': 'page_NavigationBar'})[1].select_one('div:nth-of-type(10)').text.strip())
        return [f'https:
    else:
        print('Failed to fetch the page')
b15 = 'https:
fonk1(b15)
b16 = fonk2(b15)
print("Additional pages to scrape:", b16)