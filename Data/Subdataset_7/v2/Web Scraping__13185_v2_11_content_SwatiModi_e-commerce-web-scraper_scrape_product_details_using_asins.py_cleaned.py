import pandas as pd
from bs4 import BeautifulSoup
import requests
b1 = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36',
    'Content-Type': 'text/b9',
}
def fonk1(b21):
    b2 = []
    b3 = []
    b4 = []
    b5 = []
    b6 = []
    b7 = []
    for asin in b21:
        b8 = "https:
        b9 = requests.get(b8, headers=b1).text
        b10 = BeautifulSoup(b9, 'lxml')
        b11 = b10.find_all('span', {'class': 'a-button-text'})
        b12 = b10.find('a', {'id': 'bylineInfo'})
        b13 = b10.find('span', {'id': 'productTitle'})
        b14 = b10.find('span', {'class': 'a-icon-alt'})
        b15 = b10.find('span', {'id': 'acrCustomerReviewText'})
        b16 = b10.find('span', {'id': 'priceblock_ourprice'})
        b17 = [image.find('img').get('src') for image in b11 if image.find('img')]
        b6.append(str(b17))
        b3.append(b12.text.strip() if b12 else '')
        b2.append(b13.text.strip() if b13 else '')
        b4.append(b14.text.strip() if b14 else '')
        b5.append(b15.text.strip() if b15 else '')
        b7.append(b16.text.strip() if b16 else '')
    b18 = pd.DataFrame({
        'b13': b2,
        'b12': b3,
        'images': b6,
        'price': b7,
        'product_rating': b4,
        'no. of b4': b5
    })
    return b18
if b19 = = "__main__":
    b20 = pd.read_csv('ASINs.csv')
    b21 = b20['ASIN']
    b18 = fonk1(b21)
    b18.to_csv('ASIN_product_details.csv', b22 = False)