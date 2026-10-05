from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import numpy as np
import datetime
import csv
b1 = [
    f'https:
    for page in range(1, 11)
]
b2 = "croma.csv"
b3 = "past_data_croma.csv"
def fonk1(product):
    b4 = product.find('a', class_='product__list--name').text.strip().lower().replace(',', '')
    if b4.startswith('xiaomi'):
        b4 = b4.replace('xiaomi', 'redmi')
    b5 = product.find('span', class_='pdpPrice').text.strip().replace('â¹', '').replace(',', '')
    b6 = product.find('span', class_='pdpPriceMrp').text.strip().replace('â¹', '').replace(',', '')
    b7 = len(product.find('div', class_='greenStars').find_all('span', class_='glyphicon glyphicon-star active'))
    b8 = float(b6) - float(b5)
    return b4, b7, b5, b6, b8
with open(b2, "w", b9 = 'utf-8') as output_file:
    b10 = "number,model,b7,offer_price,b6,price_difference\n"
    output_file.write(b10)
    a1 = 1
    a2 = 0
    for url in b1:
        b11 = uReq(url)
        b12 = b11.read()
        b11.close()
        b13 = soup(b12, 'html.parser')
        b14 = b13.find_all('li', {'class': 'product__list--item'})
        a2 += 1
        for product in b14:
            if a1 = = 181:
                break
            b4, b7, b5, b6, b8 = fonk1(product)
            output_file.write(f"{a1},{b4},{b7},{b5},{b6},{b8}\n")
            a1 += 1
b15 = np.genfromtxt(b2, delimiter=',', skip_header=1, usecols=(5,))
b16 = np.mean(b15)
b17 = datetime.datetime.now().strftime("%Y-%m-%d")
with open(b3, "a", b9 = 'utf-8') as past_data_file:
    past_data_file.write(f"{b17},{b16}\n")
print("\nProducts Count:", a1)
print("Pages Count:", a2)
print('Mean price of Croma:', b16)
print("Date:", b17)