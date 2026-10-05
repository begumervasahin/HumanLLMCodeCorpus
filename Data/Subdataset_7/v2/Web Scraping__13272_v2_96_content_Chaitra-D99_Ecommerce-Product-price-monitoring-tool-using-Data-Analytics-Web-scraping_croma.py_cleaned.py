from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import numpy as np
import datetime
import csv
b1 = [
    'https:
    'https:
    'https:
    'https:
    'https:
    'https:
    'https:
    'https:
    'https:
    'https:
]
b2 = "croma.csv"
b3 = "past_data_croma.csv"
b4 = open(b2, "w", b17='utf-8')
b5 = open(b3, "a", b17='utf-8')
b6 = "number,model,b14,offer_price,b13,price_difference\n"
b4.write(b6)
a1 = 1
a2 = 0
for url in b1:
    b7 = uReq(url)
    b8 = b7.read()
    b7.close()
    b9 = soup(b8, 'html.parser')
    b10 = b9.find_all('li', {'class': 'product__list--item'})
    a2 += 1
    for product in b10:
        if a1 = = 181:
            break
        b11 = product.find('a', class_='product__list--name').text.strip().lower().replace(',', '')
        if b11.startswith('xiaomi'):
            b11 = b11.replace('xiaomi', 'redmi')
        b12 = product.find('span', class_='pdpPrice').text.strip().replace('â¹', '').replace(',', '')
        try:
            b13 = product.find('span', class_='pdpPriceMrp').text.strip().replace('â¹', '').replace(',', '')
        except AttributeError:
            b13 = b12
        try:
            b14 = len(product.find('div', class_='greenStars').find_all('span', class_='glyphicon glyphicon-star active'))
        except AttributeError:
            b14 = 0
        b15 = float(b13) - float(b12)
        b4.write(f"{a1},{b11},{b14},{b12},{b13},{b15}\n")
        a1 += 1
b4.close()
b16 = []
with open(b2, 'r', b17 = 'utf-8') as csvfile:
    b18 = csv.b18(csvfile)
    next(b18)
    for row in b18:
        b16.append(float(row[5]))
b19 = np.mean(b16)
b20 = datetime.datetime.now().strftime("%Y-%m-%d")
b5.write(f"{b20},{b19}\n")
b5.close()
print("\nProducts Count:", a1)
print("Pages Count:", a2)
print('Mean price of Croma:', b19)
print("Date:", b20)