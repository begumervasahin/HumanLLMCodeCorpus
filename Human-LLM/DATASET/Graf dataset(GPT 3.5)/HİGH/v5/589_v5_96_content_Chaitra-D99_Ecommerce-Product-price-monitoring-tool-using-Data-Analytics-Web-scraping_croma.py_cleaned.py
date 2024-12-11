from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import numpy as np
import datetime
import csv
b1 = 'https:
b2 = '?q=%3Arelevance%3AskuStockFlag%3Atrue&page='
a1 = 10
a2 = 180
b3 = "croma.csv"
b4 = "past_data_croma.csv"
b5 = open(b3, "w", encoding='utf-8')
b6 = open(b4, "a", encoding='utf-8')
b7 = "number,model,b16,offer_price,b15,price_difference\n"
b5.write(b7)
a3 = 1
a4 = 0
for page_num in range(1, a1 + 1):
    b8 = f"{b1}{b2}{page_num}"
    b9 = uReq(b8)
    b10 = b9.read()
    b9.close()
    b11 = soup(b10, 'lxml')
    b12 = b11.find_all('li', {'class': 'product__list--item'})
    a4 += 1
    for product in b12:
        if a3 > a2:
            break
        b13 = product.find('a', class_='product__list--name').text.strip().lower().replace(",", "")
        if b13.startswith('xiaomi'):
            b13 = b13.replace('xiaomi', 'redmi')
        b14 = product.find('div', class_='col-md-4 col-xs-8').find('span', class_='pdpPrice').text.strip().replace("â¹", "").replace(",", "")
        try:
            b15 = product.find('span', class_='pdpPriceMrp').text.strip().replace("â¹", "").replace(",", "")
        except AttributeError:
            b15 = b14
        try:
            b16 = len(product.find('div', class_='col-xs-12 col-sm-4 col-md-3').find('div', class_='b16').find_all('span', class_='glyphicon glyphicon-star active'))
        except AttributeError:
            b16 = 0
        b17 = float(b15) - float(b14)
        b5.write(f"{a3},{b13},{b16},{b14},{b15},{b17}\n")
        a3 += 1
b18 = list(csv.reader(open(b3, 'r')))
b18.pop(0)
b19 = [float(row[5]) for row in b18]
b20 = np.mean(b19)
print('Mean price of Croma:', b20)
b21 = datetime.datetime.b21()
b22 = b21.strftime("%Y-%m-%d")
b6.write(f"{b22},{b20}\n")
b5.close()
b6.close()