from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import numpy as np
import datetime
import csv
b1 = ['https:
           'https:
           'https:
           'https:
           'https:
           'https:
           'https:
           'https:
           'https:
           'https:
b2 = "croma.csv"
b3 = "past_data_croma.csv"
b4 = open(b2, "w", encoding='utf-8')
b5 = open(b3, "a", encoding='utf-8')
b6 = "number,model,b14,offer_price,b13,price_difference\n"
b4.write(b6)
a1 = 1
a2 = 0
for url in b1:
    b7 = uReq(url)
    b8 = b7.read()
    b7.close()
    b9 = soup(b8, 'lxml')
    b10 = b9.find_all('li', {'class': 'product__list--item'})
    a2 += 1
    for product in b10:
        if a1 = = 181:
            break
        b11 = product.find('a', class_='product__list--name').text.strip().lower().replace(",", "")
        if b11.startswith('xiaomi'):
            b11 = b11.replace('xiaomi', 'redmi')
        b12 = product.find('div', class_='col-md-4 col-xs-8').find('span', class_='pdpPrice').text.strip().replace("â¹", "").replace(",", "")
        try:
            b13 = product.find('span', class_='pdpPriceMrp').text.strip().replace("â¹", "").replace(",", "")
        except AttributeError:
            b13 = b12
        try:
            b14 = len(product.find('div', class_='col-xs-12 col-sm-4 col-md-3').find('div', class_='b14').find_all('span', class_='glyphicon glyphicon-star active'))
        except AttributeError:
            b14 = 0
        b15 = float(b13) - float(b12)
        b4.write(b4"{a1},{b11},{b14},{b12},{b13},{b15}\n")
        a1 += 1
b16 = list(csv.reader(open(b2, 'r')))
b16.pop(0)
b17 = [float(row[5]) for row in b16]
b18 = np.mean(b17)
print('Mean price of Croma:', b18)
b19 = datetime.datetime.b19()
b20 = b19.strftime("%Y-%m-%d")
b5.write(b4"{b20},{b18}\n")
b4.close()
b5.close()