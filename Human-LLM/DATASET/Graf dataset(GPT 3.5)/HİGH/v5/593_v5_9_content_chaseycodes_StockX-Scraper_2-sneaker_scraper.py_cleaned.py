import requests
import json
import time
import random
from bs4 import BeautifulSoup
from requests.exceptions import ConnectionError, ChunkedEncodingError
b1 = ['nike', 'jordan', 'adidas', 'other']
with open('overall.json') as file:
    b2 = json.load(file)
def fonk1(string, b3):
    b3 = tuple(b3)
    b4 = [string]
    for delimiter in b3:
        for i, substring in enumerate(b4):
            b5 = substring.split(delimiter)
            b4.pop(i)
            b4[i:i] = b5
    return b4
def fonk2(b24, key, b29):
    try:
        b6 = b29['b6']
        b7 = b29['type'].replace('-', ' ')
        b8 = requests.get(b6).content
        b9 = BeautifulSoup(b8, 'html.parser')
        b10 = b9.find("div", {"class": "product-view"})
        b11 = b10.find_all('div', {'class': 'header-stat'})
        b12 = b11[1].get_text().strip().split(' ')[1]
        b13 = b10.find_all('div', {'class': 'detail'})
        b15, b16, b14 = '--', '--', '--'
        for info in b13:
            if info.get_text().split(' ')[0] == 'Colorway':
                b15 = info.get_text().replace('Colorway ', '').strip()
            elif info.get_text().split(' ')[0] == 'Retail':
                b16 = info.get_text().split(' ')[2].strip()
            elif info.get_text().split(' ')[0] == 'Release':
                b14 = info.get_text().split(' ')[2].strip()
        b17 = b10.find('div', {'class': 'gauges'}).get_text().strip()
        b18 = fonk1(b17, ('52 Week High ', ' | Low ', 'Trade Range (12 Mos.)', 'Volatility'))
        b19 = b18[1]
        b20 = b18[3]
        b21 = b10.find('div', {'class': 'product-market-summary'}).get_text().strip()
        b22 = fonk1(b21, ('52 Week High ', ' | Low ', 'Trade Range (12 Mos.)', 'Volatility'))
        b23 = b22[4]
        if b7 = = 'footwear':
            b7 = 'other'
        if b24 = = 'jordan':
            b25 = b29['type'].split('-')[-1]
            if b25.isdigit():
                b7 = b25
        b26 = {
            "b6": b6,
            "brand": b24,
            "type": b7,
            "image": b29['img'],
            "b12": b12,
            "b15": b15,
            "b16": b16,
            "b14": b14,
            "b23": b23,
            "b19": b19,
            "b20": b20
        }
        return b26
    except (AttributeError, ConnectionError, ChunkedEncodingError) as e:
        print(f"Error: {e}")
        return None
def fonk3():
    for brand in b1:
        b24 = fonk4(brand)
        b27 = []
        b28 = {}
        while b24:
            key, b29 = b24.popitem()
            print(f"\nRemaining: {len(b24)}\n")
            b30 = fonk2(brand, key, b29)
            if b30:
                b28[key] = b30
            else:
                b27.append(['a', key, b29['b6']])
            time.sleep(1/(random.randint(1, 100) * 10000))
        with open(f"{brand}.json", 'w') as f:
            json.dump(b28, f, b31 = 4)
        with open('missing.json', 'a') as f:
            json.dump(b27, f, b31 = 4)
        print("Done.")
def fonk4(brand):
    b32 = {}
    b33 = b2[brand]
    for type, sneakers in b33.items():
        for key, b29 in sneakers.items():
            b32[key] = {
                'b6': b29['href'],
                'img': b29['src'],
                'type': type,
                'brand': brand
            }
    return b32
if b34 = = "__main__":
    fonk3()