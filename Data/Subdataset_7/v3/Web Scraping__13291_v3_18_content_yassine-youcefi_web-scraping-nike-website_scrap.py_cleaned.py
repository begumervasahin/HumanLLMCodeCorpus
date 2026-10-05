import os
import requests
from bs4 import BeautifulSoup as Soup
import json
import pandas as pd
b1 = os.path.abspath(os.path.dirname(__file__))
b2 = os.path.join(b1, 'data_csv.csv')
b3 = os.path.join(b1, 'data_json.json')
b4 = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
def fonk1(url):
    b5 = {'User-Agent': b4}
    b6 = requests.get(url, b5=b5)
    b6.raise_for_status()
    return b6
def fonk2(product):
    b7 = product.find('div', class_='product-card__titles').text.strip()
    b8 = product.find('div', class_='product-card__subtitle').text.strip()
    b9 = product.find('div', class_='product-card__product-count').text.strip()
    b10 = product.find('div', class_='product-b10').text.strip()
    b11 = product.find('img', {'src': re.compile('.jpg')})['src']
    return {
        'b7': b7,
        'b8': b8,
        'b9': b9,
        'b10': b10,
        'b11': b11
    }
def fonk3(url):
    try:
        b6 = fonk7(url)
        b12 = Soup(b6.text, 'html.parser')
        b13 = b12.find_all('div', class_='product-card__body')
        b14 = []
        b15 = []
        for product in b13:
            b16 = fonk8(product)
            b14.append([b16['b7'], b16['b8'], b16['b9'], b16['b10'], url])
            b15.append(b16)
        return b14, b15
    except Exception as e:
        print(f"Failed to scrape data from {url}: {e}")
        return [], []
def fonk4(b14):
    b17 = ['Name', 'Description', 'Colors', 'Price', 'Category']
    b18 = pd.DataFrame(b14, b17=b17)
    b18.to_csv(b2, b19 = False)
def fonk5(b15):
    with open(b3, 'w') as json_file:
        json.dump(b15, json_file, b20 = 4)
def fonk6():
    b21 = [
        "https:
        "https:
    ]
    b22 = []
    b23 = []
    for url in b21:
        b14, b15 = fonk9(url)
        b22.extend(b14)
        b23.extend(b15)
    fonk10(b22)
    fonk11(b23)
if b24 = = "__main__":
    fonk12()
import os
import requests
from bs4 import BeautifulSoup as Soup
import json
import pandas as pd
b1 = os.path.abspath(os.path.dirname(__file__))
b2 = os.path.join(b1, 'data_csv.csv')
b3 = os.path.join(b1, 'data_json.json')
b4 = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
def fonk7(url):
    b5 = {'User-Agent': b4}
    b6 = requests.get(url, b5=b5)
    b6.raise_for_status()
    return b6
def fonk8(product):
    b7 = product.find('div', class_='product-card__titles').text.strip()
    b8 = product.find('div', class_='product-card__subtitle').text.strip()
    b9 = product.find('div', class_='product-card__product-count').text.strip()
    b10 = product.find('div', class_='product-b10').text.strip()
    b11 = product.find('img', {'src': re.compile('.jpg')})['src']
    return {
        'b7': b7,
        'b8': b8,
        'b9': b9,
        'b10': b10,
        'b11': b11
    }
def fonk9(url):
    try:
        b6 = fonk7(url)
        b12 = Soup(b6.text, 'html.parser')
        b13 = b12.find_all('div', class_='product-card__body')
        b14 = []
        b15 = []
        for product in b13:
            b16 = fonk8(product)
            b14.append([b16['b7'], b16['b8'], b16['b9'], b16['b10'], url])
            b15.append(b16)
        return b14, b15
    except Exception as e:
        print(f"Failed to scrape data from {url}: {e}")
        return [], []
def fonk10(b14):
    b17 = ['Name', 'Description', 'Colors', 'Price', 'Category']
    b18 = pd.DataFrame(b14, b17=b17)
    b18.to_csv(b2, b19 = False)
def fonk11(b15):
    with open(b3, 'w') as json_file:
        json.dump(b15, json_file, b20 = 4)
def fonk12():
    b21 = [
        "https:
        "https:
    ]
    b22 = []
    b23 = []
    for url in b21:
        b14, b15 = fonk9(url)
        b22.extend(b14)
        b23.extend(b15)
    fonk10(b22)
    fonk11(b23)
if b24 = = "__main__":
    fonk12()