import os
import requests
from bs4 import BeautifulSoup as Soup
import json
import pandas as pd
b1 = os.path.abspath(os.path.dirname(__file__))
b2 = os.path.join(b1, 'data_csv.csv')
b3 = os.path.join(b1, 'data_json.json')
b4 = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}
def fonk1(url):
    b5 = requests.get(url, headers=b4)
    if b5.status_code != 200:
        print(f"Failed to retrieve data from {url}")
        return [], []
    b6 = Soup(b5.text, 'html.parser')
    b7 = b6.find_all('div', class_='product-card__body')
    b8 = []
    b9 = []
    for product in b7:
        b10 = product.find('div', class_='product-card__titles').text.strip()
        b11 = product.find('div', class_='product-card__subtitle').text.strip()
        b12 = product.find('div', class_='product-card__product-count').text.strip()
        b13 = product.find('div', class_='product-price').text.strip()
        b14 = product.find('img', {'src': re.compile('.jpg')})['src']
        b8.append([b10, b11, b12, b13, url])
        b9.append({
            'name': b10,
            'description': b11,
            'colors': b12,
            'price': b13,
            'image': b14
        })
    return b8, b9
def fonk2():
    b15 = [
        "https:
        "https:
    ]
    b16 = []
    b17 = []
    for url in b15:
        b8, b9 = fonk1(url)
        b16.extend(b8)
        b17.extend(b9)
    pd.DataFrame(b16, b18 = ['Name', 'Description', 'Colors', 'Price', 'Category']).to_csv(b2, index=False)
    with open(b3, 'w') as json_file:
        json.dump(b17, json_file, b19 = 4)
if b20 = = "__main__":
    fonk2()