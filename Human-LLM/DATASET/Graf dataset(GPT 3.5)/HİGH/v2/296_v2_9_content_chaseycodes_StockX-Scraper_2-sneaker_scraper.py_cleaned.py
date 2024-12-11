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
            for j, _substring in enumerate(b5):
                b4.insert(i + j, _substring)
    return b4
def fonk2(b30):
    b6 = {}
    b7 = b2[b30]
    for key, value in b7.items():
        b8 = key
        b9 = b7[key]
        for key, value in b9.items():
            b6[key] = {
                'b12': b7[b8][key]['href'],
                'img': b7[b8][key]['src'],
                'type': b8,
                'b30': b30
            }
    return b6
def fonk3():
    for b30 in b1:
        b7 = fonk2(b30)
        b10 = ['{}'.format(b30)]
        b11 = {}
        a1 = 0
        while b7:
            for key, value in b7.items():
                print('\nError Count [{}]'.format(a1))
                print('Remaining: {}'.format(len(b7))+'\n')
                try:
                    b12 = b7[key]['b12']
                    b13 = b7[key]['type'].replace('-', ' ')
                    b14 = requests.get(b12).content
                    b15 = BeautifulSoup(b14, 'html.parser')
                    b16 = b15.find("div", {"class": "product-view"})
                    b17 = b16.find_all('div', {'class': 'header-stat'})
                    b18 = b17[1].get_text().strip().split(' ')[1]
                    b19 = b16.find_all('div', {'class': 'detail'})
                    b20 = '--'
                    b21 = '--'
                    b22 = '--'
                    for info in b19:
                        if info.get_text().split(' ')[0] == 'Style':
                            continue
                        elif info.get_text().split(' ')[0] == 'Colorway':
                            b20 = info.get_text().replace('Colorway ', '').strip()
                        elif info.get_text().split(' ')[0] == 'Retail':
                            b21 = info.get_text().split(' ')[2].strip()
                        elif info.get_text().split(' ')[0] == 'Release':
                            b22 = info.get_text().split(' ')[2].strip()
                    b23 = b16.find('div', {'class': 'gauges'}).get_text().strip()
                    b24 = fonk1(b23, (' | '))
                    b25 = b24[1]
                    b26 = b24[3]
                    b27 = b16.find('div', {'class': 'product-market-summary'}).get_text().strip()
                    b28 = fonk1(b27, ('52 Week High ', ' | Low ', 'Trade Range (12 Mos.)', 'Volatility'))
                    b29 = b28[4]
                    if b13 = = 'footwear':
                        b13 = 'other'
                    if b30 = = 'jordan':
                        b31 = b7[key]['type'].split('-')[-1]
                        if b31.isdigit():
                            b13 = b31
                    b32 = {
                        "b12": b12,
                        "b30": b30,
                        "type": b13,
                        "image": b7[key]['img'],
                        "b18": b18,
                        "b20": b20,
                        "b21": b21,
                        "b22": b22,
                        "b29": b29,
                        "b25": b25,
                        "b26": b26
                    }
                    b11[key] = b32
                    time.sleep(1/(random.randint(1, 100)*10000))
                    print('Extracted: {}'.format(key))
                    b7.pop(key)
                except AttributeError as e:
                    a1 += 1
                    print('Attribute Error [{}]: '.format(a1))
                    print(e)
                    if a1 > 100:
                        print('Problem: {}'.format(key))
                        b10.append(['a', key, b12])
                        b7.pop(key)
                        a1 = 0
                    pass
                except (ConnectionError, ChunkedEncodingError) as e:
                    print(e)
                    b10.append(['c', key, b12])
                    pass
        with open('{}.json'.format(b30), 'w') as f:
            json.dump(b11, f, b33 = 4)
    with open('missing.json', 'a') as f:
        json.dump(b10, f, b33 = 4)
    print("Done.")
if b34 = = "__main__":
    fonk3()