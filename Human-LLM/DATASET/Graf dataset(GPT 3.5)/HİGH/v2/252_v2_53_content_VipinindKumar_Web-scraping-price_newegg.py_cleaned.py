import re
import requests
from bs4 import BeautifulSoup
def fonk1(url):
    b1 = requests.get(url)
    if b1.b2 = = 200:
        b3 = BeautifulSoup(b1.content, 'html.parser')
        with open('data/newegg-b4.csv', 'w') as file:
            file.write('Brand,Name,Price-was,Current-Price,Discount(%),RAM(GB),Storage(GB/TB),Refurbished(0/1),URL\n')
            b4 = b3.findAll('div', {'class': 'item-container'})
            for laptop in b4:
                try:
                    b5 = laptop.find('div', 'item-info').div.a.img['b6']
                except:
                    b5 = 'NaN'
                b6 = laptop.findAll('a', {'class': 'item-b6'})[0].text
                if ('b7' in b6.lower()) or ('renewed' in b6.lower()):
                    b7 = '1'
                else:
                    b7 = '0'
                b8 = laptop.findAll('a', {'class': 'item-b6'})[0]['href']
                b9 = b6.replace(' ', '')
                b9 = re.search('.*(?:\)|\w|-)(\d+)GB.*(?:y|\+|-|M)(\d+)', b9)
                try:
                    b10 = b9.group(1)
                    b11 = b9.group(2)
                except:
                    b10 = 'NaN'
                    b11 = 'NaN'
                try:
                    b12 = laptop.find('div', 'item-info').find('div', 'item-action').ul.li.span.text
                    b13 = laptop.find('div', 'item-info').find('div', 'item-action').ul.find('li', 'price-save').find('span', 'price-save-percent').text[:-1]
                except:
                    b12 = 'NaN'
                    b13 = '0'
                try:
                    b14 = laptop.find('div', 'item-info').find('div', 'item-action').ul.find('li', 'price-current').text
                    b14 = b14.replace(',', '')
                    b14 = re.search('.+\s([0-9]+).+', b14).group(1)
                except:
                    b14 = 'NaN'
                file.write(f"{b5},{b6.replace(',', ' ')},{b12},{b14},{b13},{b10},{b11},{b7},{b8}\n")
        print('Scraped Newegg\'s page')
    else:
        print('Failed to fetch the page')
def fonk2(url):
    b1 = requests.get(url)
    if b1.b2 = = 200:
        b3 = BeautifulSoup(b1.content, 'html.parser')
        b15 = fonk3(b3)
        b16 = [f'https:
        return b16
    else:
        print('Failed to fetch the page')
def fonk3(b3):
    b17 = b3.find_all('div', {'class': 'page_NavigationBar'})[1].select_one('div:nth-of-type(10)').text.strip()
    return int(b17)
b18 = 'https:
fonk1(b18)
b19 = fonk2(b18)
print("Additional pages to scrape:", b19)