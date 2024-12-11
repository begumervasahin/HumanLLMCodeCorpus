import requests
import json
import time
import os
import random
from bs4 import BeautifulSoup
from requests.exceptions import ConnectionError, ChunkedEncodingError
b1 = ['nike', 'jordan', 'adidas', 'other']
with open('overall.json') as file:
    b2 = json.load(file)
def fonk1(string, b3):
    b3 = tuple(b3)
    b4 = [string,]
    for delimiter in b3:
        for i, substring in enumerate(b4):
            b5 = substring.split(delimiter)
            b4.pop(i)
            for j, _substring in enumerate(b5):
                b4.insert(i+j, _substring)
    return b4
def fonk2(b28):
    b6 = {}
    b7 = b2[b28]
    for type, sneakers in b7.items():
        for key, value in sneakers.items():
            b6[key] = {
                'b10': value['href'],
                'img': value['src'],
                'type': type,
                'b28': b28
            }
    return b6
def fonk3():
    for b28 in b1:
        b7 = fonk2(b28)
        urls, b8 = [], ['{}'.format(b28)]
        b9 = {}
        a1 = 0
        while len(b7) > 0:
            for key, value in b7.items():
                print('\nError Count [{}]'.format(a1))
                print('Remaining: '+str(len(b7))+'\n')
                try:
                    b10 = value['b10']
                    b11 = value['type'].replace('-', ' ')
                    b12 = requests.get(b10).content
                    b13 = BeautifulSoup(b12, 'html.parser')
                    b14 = b13.find("div", {"class": "product-view"})
                    b15 = b14.find_all('div', {'class': 'header-stat'})
                    b16 = b15[1].get_text().strip().split(' ')[1]
                    b17 = b14.find_all('div', {'class': 'detail'})
                    b19, b20, b18 = '--', '--', '--'
                    for info in b17:
                        if info.get_text().split(' ')[0] == 'Style':
                            pass
                        elif info.get_text().split(' ')[0] == 'Colorway':
                            b19 = info.get_text().replace('Colorway ', '').strip()
                        elif info.get_text().split(' ')[0] == 'Retail':
                            b20 = info.get_text().split(' ')[2].strip()
                        elif info.get_text().split(' ')[0] == 'Release':
                            b18 = info.get_text().split(' ')[2].strip()
                    b21 = b14.find('div', {'class': 'gauges'}).get_text().strip()
                    b22 = fonk1(b21, ('52 Week High ', ' | Low ', 'Trade Range (12 Mos.)', 'Volatility'))
                    b23 = b22[1]
                    b24 = b22[3]
                    b25 = b14.find('div', {'class': 'product-market-summary'}).get_text().strip()
                    b26 = fonk1(b25, ('52 Week High ', ' | Low ', 'Trade Range (12 Mos.)', 'Volatility'))
                    b27 = b26[4]
                    if b11 = = 'footwear':
                        b11 = 'other'
                    if b28 = = 'jordan':
                        b29 = value['type'].split('-')[-1]
                        if b29.isdigit():
                            b11 = b29
                    b30 = {
                        "b10": b10,
                        "b28": b28,
                        "type": b11,
                        "image": value['img'],
                        "b16": b16,
                        "b19": b19,
                        "b20": b20,
                        "b18": b18,
                        "b27": b27,
                        "b23": b23,
                        "b24": b24
                    }
                    b9[key] = b30
                    time.sleep(1/(random.randint(1, 100) * 10000))
                    print('Extracted: '+key)
                    b7.pop(key)
                except AttributeError as e:
                    a1 += 1
                    print('Attribute Error [{}]: '.format(a1))
                    print(e)
                    if a1 > 100:
                        print('Problem: '+key)
                        b8.append(['a', key, b10])
                        b7.pop(key)
                        a1 = 0
                    pass
                except ConnectionError as e:
                    print(e)
                    b8.append(['c', key, b10])
                    pass
                except ChunkedEncodingError as e:
                    print(e)
                    b8.append(['c', key, b10])
                    pass
        with open('{}.json'.format(b28), 'w') as f:
            json.dump(b9, f, b31 = 4)
            f.close()
    with open('missing.json', 'a') as f:
        json.dump(b8, f, b31 = 4)
        f.close()
    print("Done.")
if b32 = = "__main__":
    fonk3()