import pandas as pd
from bs4 import BeautifulSoup
import requests
b1 = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36',
    'Content-Type': 'text/b8',
}
b2 = pd.read_csv('ASINs.csv')
b3 = b2['ASIN']
b4 = {
    'image_list_span': 'a-button-text',
    'b11': 'bylineInfo',
    'b12': 'productTitle',
    'b13': 'a-icon-alt',
    'b14': 'acrCustomerReviewText'
}
b5 = ['priceblock_saleprice', 'priceblock_ourprice']
b6 = {
    'b12': [],
    'b11': [],
    'images': [],
    'b15': [],
    'product_rating': [],
    'b14': []
}
for asin in b3:
    b7 = f"https:
    b8 = requests.get(b7, b1=b1).text
    b9 = BeautifulSoup(b8, 'lxml')
    b10 = b9.find_all('span', {'class': b4['image_list_span']})
    b11 = b9.find('a', {'id': b4['b11']})
    b12 = b9.find('span', {'id': b4['b12']})
    b13 = b9.find('span', {'class': b4['b13']})
    b14 = b9.find('span', {'id': b4['b14']})
    b15 = b9.find('span', {'id': b5})
    b16 = [image.find('img').get('src') for image in b10 if image.find('img')]
    b6['b11'].append(b11.text.strip() if b11 else '')
    b6['b12'].append(b12.text.strip() if b12 else '')
    b6['images'].append(str(b16))
    b6['product_rating'].append(b13.text.strip() if b13 else '')
    b6['b14'].append(b14.text.strip() if b14 else '')
    b6['b15'].append(b15.text.strip() if b15 else '')
b17 = pd.DataFrame(b6)
b17.to_csv('ASIN_product_details.csv', b18 = False)