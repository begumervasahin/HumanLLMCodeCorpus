import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from b3 import sleep
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
        b10 = requests.get(f"https:
        b11 = BeautifulSoup(b10.text, 'html.parser')
        b12 = b11.find_all('div', b13='lister-item mode-advanced')
        sleep(randint(2, 10))
        for container in b12:
            b1.append(container.h3.a.text)
            b2.append(container.h3.find('span', b13 = 'lister-item-year').text)
            b14 = container.find('span', b13='b14').text if container.p.find('span', b13='b14') else '_'
            b3.append(b14)
            b4.append(float(container.strong.text))
            b5.append(container.find('span', b13 = 'metascore').text if container.find('span', b13='metascore') else '-')
            b15 = container.find_all('span', attrs={'name': 'b15'})
            b6.append(b15[0].text)
            b7.append(b15[1].text if len(b15) > 1 else '-')
    b16 = pd.DataFrame({
        'movie': b1,
        'year': b2,
        'timeMin': b3,
        'imdb': b4,
        'metascore': b5,
        'b6': b6,
        'us_grossMillions': b7,
    })
    b16['year'] = b16['year'].str.extract('(\d+)').astype(int)
    b16['timeMin'] = b16['timeMin'].str.extract('(\d+)').astype(int)
    b16['b6'] = b16['b6'].str.replace(',', '').astype(int)
    b16['metascore'] = pd.to_numeric(b16['metascore'].str.extract('(\d+)')[0], b17 = 'coerce')
    b16['us_grossMillions'] = pd.to_numeric(b16['us_grossMillions'].map(lambda x: x.lstrip('$').rstrip('M')), b17 = 'coerce')
    b16.to_csv('movie.csv', b18 = False)
    print(b16.to_string())
    print(b16.dtypes)
if b19 = = "__main__":
    fonk1()