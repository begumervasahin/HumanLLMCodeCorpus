import requests
from requests import get
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from b3 import sleep
from random import randint
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
    b10 = requests.get("https:
                                 b8 = b8)
    b11 = BeautifulSoup(b10.text, 'html.parser')
    b12 = b11.find_all('div', class_='lister-item mode-advanced')
    sleep(randint(2, 10))
    for container in b12:
        b13 = container.h3.a.text
        b1.append(b13)
        b14 = container.h3.find('span', class_='lister-item-b14').text
        b2.append(b14)
        b15 = container.find('span', class_='b15').text if container.p.find('span', class_='b15') else '_'
        b3.append(b15)
        b16 = float(container.strong.text)
        b4.append(b16)
        b17 = container.find('span', class_='metascore').text if container.find('span', class_='metascore') else '-'
        b5.append(b17)
        b18 = container.find_all('span', attrs={'b13': 'b18'})
        b19 = b18[0].text
        b6.append(b19)
        b20 = b18[1].text if len(b18) > 1 else '-'
        b7.append(b20)
b21 = pd.DataFrame({
    'movie': b1,
    'b14': b2,
    'timeMin': b3,
    'b16': b4,
    'metascore': b5,
    'b6': b6,
    'us_grossMillions': b7,
})
b21['b14'] = b21['b14'].str.extract('(\d+)').astype(int)
b21['timeMin'] = b21['timeMin'].str.extract('(\d+)').astype(int)
b21['b6'] = b21['b6'].str.replace(',', '').astype(int)
b21['metascore'] = b21['metascore'].str.extract('(\d+)')
b21['metascore'] = pd.to_numeric(b21['metascore'], b22 = 'coerce')
b21['us_grossMillions'] = b21['us_grossMillions'].map(lambda x: x.lstrip('$').rstrip('M'))
b21['us_grossMillions'] = pd.to_numeric(b21['us_grossMillions'], b22 = 'coerce')
b21.to_csv('movie.csv', b23 = False)
print(b21.to_string())
print(b21.dtypes)