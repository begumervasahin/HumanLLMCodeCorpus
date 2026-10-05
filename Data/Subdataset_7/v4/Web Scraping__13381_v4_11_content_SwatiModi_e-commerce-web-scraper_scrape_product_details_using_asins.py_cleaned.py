import pandas as pd
from bs4 import BeautifulSoup
import requests
b1 = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36',
    'Content-Type': 'text/b18',
}
b2 = pd.read_csv('ASINs.csv')
b3 = b2['ASIN']
b4 = 'a-button-text'
b5 = 'bylineInfo'
b6 = 'productTitle'
b7 = 'a-icon-alt'
b8 = 'acrCustomerReviewText'
b9 = 'priceblock_saleprice'
b10 = 'priceblock_ourprice'
b11 = []
b12 = []
b13 = []
b14 = []
b15 = []
b16 = []
for asin in b3:
    b17 = "https:
    b18 = requests.get(b17, b1=b1).text
    b19 = BeautifulSoup(b18, 'lxml')
    b20 = b19.find_all('span', {'class': b4})
    b21 = b19.find_all('a', {'id': b5})
    b22 = b19.find_all('span', {'id': b6})
    b23 = b19.find_all('span', {'class': b7})
    b24 = b19.find_all('span', {'id': b8})
    b25 = b19.find('span', {'id': b10})
    b26 = []
    for image in b20:
        try:
            b27 = image.find('img').get('src')
            b26.append(b27)
        except:
            pass
    b15.append(str(b26))
    b12.append(b21[0].text.strip() if b21 else '')
    b11.append(b22[0].text.strip() if b22 else '')
    b13.append(b23[0].text.strip() if b23 else '')
    b14.append(b24[0].text.strip() if b24 else '')
    b16.append(b25.text.strip() if b25 else '')
b28 = pd.DataFrame({
    'b22': b11,
    'b21': b12,
    'images': b15,
    'price': b16,
    'product_rating': b13,
    'no. of b13': b14
})
b28.to_csv('ASIN_product_details.csv', b29 = False)