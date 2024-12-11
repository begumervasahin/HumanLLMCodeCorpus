import os
import time
import requests
import re
import pandas as pd
from bs4 import BeautifulSoup
from random import randint
from time import sleep
b1 = os.path.abspath(os.path.dirname(__file__))
b2 = os.path.join(b1, 'b10.csv')
b3 = os.path.join(b1, 'b9.json')
def fonk1(url_list):
    b4 = {}
    for url in url_list:
        b5 = requests.get(url)
        b6 = BeautifulSoup(b5.text, 'html.parser')
        b7 = b6.find("h1", {"class": "wall-header__title"}).text
        b4[b7] = url
    return b4
def fonk2(url, category):
    b5 = requests.get(url)
    b6 = BeautifulSoup(b5.text, 'html.parser')
    b8 = b6.find_all("div", {"class": "product-card__body"})
    b9 = []
    b10 = []
    for product in b8:
        try:
            b11 = product.find('div', {"class": "product-card__titles"}).text.strip()
            b12 = product.find('div', {"class": "product-card__subtitle"}).text.strip()
            b13 = product.find('div', {"class": "product-card__product-count"}).text.strip()
            b14 = product.find('div', {"class": "product-price css-11s12ax is--current-price"}).text.strip()
            b15 = product.find('img')['src']
            b10.append([b11, b12, b13, b14, category])
            b9.append({"name": b11, "description": b12, "colors": b13, "price": b14, "image": b15})
        except Exception as e:
            print("Error processing product:", e)
    return b10, b9
if b16 = = '__main__':
    b17 = ["https:
            "https:
    b4 = fonk1(b17)
    b18 = []
    b19 = []
    for category, url in b4.items():
        csv_data, b20 = fonk2(url, category)
        b18.extend(csv_data)
        b19.extend(b20)
    b21 = pd.DataFrame(b18, columns=["Name", "Description", "Colors", "Price", "Category"])
    b21.to_csv(b2, b22 = False)
    with open(b3, 'w') as json_f:
        json_f.write(json.dumps(b19, b23 = 4))