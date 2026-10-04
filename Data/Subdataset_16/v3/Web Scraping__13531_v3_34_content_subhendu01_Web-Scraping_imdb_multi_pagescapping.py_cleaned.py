import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from time import sleep
from random import randint
def fonk1():
    b1 = []
    b2 = []
    b3 = []
    b4 = []
    b5 = []
    b6 = []
    b7 = []
    b8 = {"Accept-Language": "en-US, en;q=0.5"}
    b9 = np.arange(1, 1001, 50)
    for page in b9:
        b10 = f"https:
        b11 = requests.get(b10, b8=b8)
        b12 = BeautifulSoup(b11.text, 'html.parser')
        b13 = b12.find_all('div', class_='lister-item mode-advanced')
        sleep(randint(2, 10))
        for container in b13:
            b14 = container.h3.a.text
            b1.append(b14)
            b15 = container.h3.find('span', class_='lister-item-b15').text
            b2.append(b15)
            b16 = container.find('span', class_='b16').text if container.p.find('span', class_='b16') else '_'
            b3.append(b16)
            b17 = float(container.strong.text)
            b4.append(b17)
            b18 = container.find('span', class_='b18').text if container.find('span', class_='b18') else '-'
            b5.append(b18)
            b19 = container.find_all('span', attrs={'name': 'nv'})
            b20 = b19[0].text
            b6.append(b20)
            b21 = b19[1].text if len(b19) > 1 else '-'
            b7.append(b21)
    b22 = pd.DataFrame({
        'movie': b1,
        'b15': b2,
        'b16': b3,
        'b17': b4,
        'b18': b5,
        'b6': b6,
        'b7': b7,
    })
    b22['b15'] = b22['b15'].str.extract('(\d+)').astype(int)
    b22['b16'] = b22['b16'].str.extract('(\d+)').astype(float)
    b22['b6'] = b22['b6'].str.replace(',', '').astype(int)
    b22['b18'] = pd.to_numeric(b22['b18'].str.extract('(\d+)')[0], b23 = 'coerce')
    b22['b7'] = pd.to_numeric(b22['b7'].map(lambda x: x.lstrip('$').rstrip('M')), b23 = 'coerce')
    b22.to_csv('movie.csv', b24 = False)
    print(b22.to_string())
    print(b22.dtypes)
if b25 = = "__main__":
    fonk1()