import os
import requests
import pandas as pd
from bs4 import BeautifulSoup
b1 = os.path.abspath(os.path.dirname(__file__))
b2 = os.path.join(b1, 'b9.csv')
b3 = os.path.join(b1, 'b10.json')
def fonk1(b17):
    b4 = {}
    for url in b17:
        b5 = requests.get(url)
        b6 = BeautifulSoup(b5.text, 'html.parser')
        b7 = b6.find("h1", class_="wall-header__title").text
        b4[b7] = url
    return b4
def fonk2(url, category):
    b5 = requests.get(url)
    b6 = BeautifulSoup(b5.text, 'html.parser')
    b8 = b6.find_all("div", class_="product-card__body")
    b9 = []
    b10 = []
    for product in b8:
        try:
            b11 = product.find('div', class_="product-card__titles").text.strip()
            b12 = product.find('div', class_="product-card__subtitle").text.strip()
            b13 = product.find('div', class_="product-card__product-count").text.strip()
            b14 = product.find('div', class_="product-price css-11s12ax is--current-price").text.strip()
            b15 = product.find('img')['src']
            b9.append([b11, b12, b13, b14, category])
            b10.append({
                "name": b11,
                "description": b12,
                "colors": b13,
                "price": b14,
                "image": b15
            })
        except Exception as e:
            print("Error processing product:", e)
    return b9, b10
if b16 = = '__main__':
    b17 = [
        "https:
        "https:
    ]
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