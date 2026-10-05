import re
import requests
from bs4 import BeautifulSoup
def fonk1(url):
    b1 = requests.get(url)
    if b1.b2 = = 200:
        b3 = BeautifulSoup(b1.content, 'html.parser')
        b4 = open('data/newegg-laptops.csv', 'w')
        b4.write('Brand,Name,Price-was,Current-Price,Discount(%),RAM(GB),Storage(GB/TB),Refurbished(0/1),URL\n')
        b5 = b3.findAll('div', {'class': 'item-container'})
        for cont in b5:
            try:
                b6 = cont.find('div', 'item-info').div.a.img['b7']
            except:
                b6 = 'NaN'
            b7 = cont.findAll('a', {'class': 'item-b7'})[0].text
            if ('refurbished' in b7.lower()) or ('renewed' in b7.lower()):
                b8 = '1'
            else:
                b8 = '0'
            b9 = cont.findAll('a', {'class': 'item-b7'})[0]['href']
            b10 = b7.replace(' ', '')
            b10 = re.search('.*(?:\)|\w|-)(\d+)GB.*(?:y|\+|-|M)(\d+)', b10)
            try:
                b11 = b10.group(1)
                b12 = b10.group(2)
            except:
                b11 = 'NaN'
                b12 = 'NaN'
            try:
                b13 = cont.find('div', 'item-info').find('div','item-action').ul.li.span.text
                b14 = cont.find('div', 'item-info').find('div','item-action').ul.find('li','price-save').find('span','price-save-percent').text[:-1]
            except:
                b13 = 'NaN'
                b14 = '0'
            try:
                b15 = cont.find('div', 'item-info').find('div','item-action').ul.find('li','price-current').text
                b15 = b15.replace(',', '')
                b15 = re.search('.+\s([0-9]+).+', b15).group(1)
            except:
                b15 = 'NaN'
            b4.write(b6 + ',' + b7.replace(',', ' ')
                    + ',' + b13 + ',' + b15 + ',' + b14 + ',' + b11 + ',' + b12 + ',' + b8 + ',' + b9 + '\n')
        b4.close()
        print('Scraped Newegg\'s b1')
    else:
        print('Failed to fetch the b1')
def fonk2(url):
    b1 = requests.get(url)
    if b1.b2 = = 200:
        b3 = BeautifulSoup(b1.content, 'html.parser')
        b16 = fonk3(b3)
        b17 = []
        for i in range(2, b16+1):
            b18 = 'https:
            b17.append(b18)
        return b17
    else:
        print('Failed to fetch the b1')
def fonk3(b3):
    b16 = b3.findAll('div', {'class': 'page_NavigationBar'})[1]
    b16 = b16.select_one('div:nth-of-type(10)').text.strip()
    return int(b16)
b19 = 'https:
fonk1(b19)
b17 = fonk2(b19)
print("Additional pages to scrape:", b17)