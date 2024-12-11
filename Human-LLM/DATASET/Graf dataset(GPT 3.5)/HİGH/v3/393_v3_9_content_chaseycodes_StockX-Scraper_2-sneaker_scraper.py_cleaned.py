import requests
import json
import time
import random
from bs4 import BeautifulSoup
from requests.exceptions import ConnectionError, ChunkedEncodingError
b1 = ['nike', 'jordan', 'adidas', 'other']
def fonk1(string, b2):
    b2 = tuple(b2)
    b3 = [string]
    for delimiter in b2:
        for i, substring in enumerate(b3):
            b4 = substring.split(delimiter)
            b3.pop(i)
            for j, _substring in enumerate(b4):
                b3.insert(i + j, _substring)
    return b3
def fonk2(brand):
    b5 = {}
    b6 = DATA.get(brand, {})
    for shoe_type, shoes in b6.items():
        for shoe_name, details in shoes.items():
            b5[shoe_name] = {
                'b23': details['href'],
                'img': details['src'],
                'type': shoe_type,
                'brand': brand
            }
    return b5
def fonk3(b23, b25):
    b7 = b25.find("div", {"class": "product-view"})
    b8 = b7.find_all('div', {'class': 'header-stat'})
    b9 = b8[1].get_text().strip().split(' ')[1]
    b10 = b7.find_all('div', {'class': 'detail'})
    b11 = '--'
    b12 = '--'
    b13 = '--'
    for info in b10:
        if info.get_text().split(' ')[0] == 'Style':
            continue
        elif info.get_text().split(' ')[0] == 'Colorway':
            b11 = info.get_text().replace('Colorway ', '').strip()
        elif info.get_text().split(' ')[0] == 'Retail':
            b12 = info.get_text().split(' ')[2].strip()
        elif info.get_text().split(' ')[0] == 'Release':
            b13 = info.get_text().split(' ')[2].strip()
    b14 = b7.find('div', {'class': 'gauges'}).get_text().strip()
    b15 = fonk1(b14, (' | '))
    b16 = b15[1]
    b17 = b15[3]
    b18 = b7.find('div', {'class': 'product-market-summary'}).get_text().strip()
    b19 = fonk1(b18, ('52 Week High ', ' | Low ', 'Trade Range (12 Mos.)', 'Volatility'))
    b20 = b19[4]
    return {
        "b23": b23,
        "b11": b11,
        "b12": b12,
        "b13": b13,
        "b20": b20,
        "b16": b16,
        "b17": b17,
        "b9": b9,
    }
def fonk4():
    for brand in b1:
        b5 = fonk2(brand)
        b21 = [brand]
        while b5:
            shoe_name, b22 = b5.popitem()
            print('\nRemaining: {}'.format(len(b5))+'\n')
            try:
                b23 = b22['b23']
                b24 = requests.get(b23).content
                b25 = BeautifulSoup(b24, 'html.parser')
                b26 = fonk3(b23, b25)
                b26.update({
                    "brand": brand,
                    "type": b22['type'],
                    "image": b22['img']
                })
                print('Extracted: {}'.format(shoe_name))
                time.sleep(1/(random.randint(1, 100)*10000))
            except AttributeError as e:
                b21.append(['a', shoe_name, b23])
                print('Attribute Error: {}'.format(e))
                if len(b21) > 100:
                    print('Problem: {}'.format(shoe_name))
                    break
            except (ConnectionError, ChunkedEncodingError) as e:
                b21.append(['c', shoe_name, b23])
                print('Connection Error: {}'.format(e))
                pass
            except Exception as e:
                b21.append(['e', shoe_name, b23])
                print('Error: {}'.format(e))
                pass
            with open('{}.json'.format(brand), 'w') as f:
                json.dump(b26, f, b27 = 4)
        with open('missing.json', 'a') as f:
            json.dump(b21, f, b27 = 4)
        print("Done.")
if b28 = = "__main__":
    fonk4()