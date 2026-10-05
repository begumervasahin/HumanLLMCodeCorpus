import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from b3 import sleep
from random import randint
def fonk1(b15, b14):
    b1 = []
    b2 = []
    b3 = []
    b4 = []
    b5 = []
    b6 = []
    b7 = []
    b8 = np.arange(1, 1001, 50)
    for page in b8:
        b9 = requests.get(b15.format(page), b14=b14)
        b10 = BeautifulSoup(b9.text, 'html.parser')
        b11 = b10.find_all('div', b12='lister-item mode-advanced')
        for container in b11:
            b1.append(container.h3.a.text)
            b2.append(container.h3.find('span', b12 = 'lister-item-year').text)
            b3.append(container.find('span', b12 = 'runtime').text if container.p.find('span', b12='runtime') else '_')
            b4.append(float(container.strong.text))
            b5.append(container.find('span', b12 = 'metascore').text if container.find('span', b12='metascore') else '-')
            b13 = container.find_all('span', attrs={'name': 'b13'})
            b6.append(b13[0].text)
            b7.append(b13[1].text if len(b13) > 1 else '-')
        sleep(randint(2, 10))
    return b1, b2, b3, b4, b5, b6, b7
def fonk2():
    b14 = {"Accept-Language": "en-US, en;q=0.5"}
    b15 = "https:
    b1, b2, b3, b4, b5, b6, b7 = fonk1(b15, b14)
    b16 = {
        'movie': b1,
        'year': b2,
        'timeMin': b3,
        'imdb': b4,
        'metascore': b5,
        'b6': b6,
        'us_grossMillions': b7,
    }
    b17 = pd.DataFrame(b16)
    b17['year'] = b17['year'].str.extract('(\d+)').astype(int)
    b17['timeMin'] = b17['timeMin'].str.extract('(\d+)').astype(int)
    b17['b6'] = b17['b6'].str.replace(',', '').astype(int)
    b17['metascore'] = b17['metascore'].str.extract('(\d+)')
    b17['metascore'] = pd.to_numeric(b17['metascore'], b18 = 'coerce')
    b17['us_grossMillions'] = b17['us_grossMillions'].str.replace('$', '').str.replace('M', '').astype(float)
    b17.to_csv('movie.csv', b19 = False)
    print(b17.to_string())
    print(b17.dtypes)
if b20 = = "__main__":
    fonk2()