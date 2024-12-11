import os
import time
import requests
import re
import pandas as pd
from bs4 import BeautifulSoup as soup
from random import randint
from time import sleep
import json
b1 = os.path.abspath(os.path.dirname(__file__))
b2 = os.path.join(b1, 'b9.csv')
b3 = os.path.join(b1, 'b10.json')
def fonk1(url):
    b4 = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    b5 = requests.get(url, b4=b4)
    if b5.b6 = = 200:
        b7 = soup(b5.text, 'html.parser')
        b8 = b7.find_all('div', class_='product-card__body')
        b9 = ""
        b10 = []
        for product in b8:
            b11 = product.find('div', class_='product-card__titles').text.strip()
            b12 = product.find('div', class_='product-card__subtitle').text.strip()
            b13 = product.find('div', class_='product-card__product-count').text.strip()
            b14 = product.find('div', class_='product-price').text.strip()
            b15 = product.find('img', {'src': re.compile('.jpg')})['src']
            b9 += f"{b11},{b12},{b13},{b14},{url}\n"
            b10.append({
                'name': b11,
                'description': b12,
                'colors': b13,
                'price': b14,
                'image': b15
            })
        return b9, b10
    else:
        print(f"Failed to retrieve data from {url}")
        return "", []
def fonk2():
    b16 = [
        "https:
        "https:
    ]
    b17 = ""
    b18 = []
    for url in b16:
        b9, b10 = fonk1(url)
        b17 += b9
        b18 += b10
    with open(b2, 'w') as csv_file:
        csv_file.write("name_product,description_product,colors_product,price_product,category\n")
        csv_file.write(b17)
    with open(b3, 'w') as json_file:
        json.dump(b18, json_file, b19 = 4)
if b20 = = "__main__":
    fonk2()