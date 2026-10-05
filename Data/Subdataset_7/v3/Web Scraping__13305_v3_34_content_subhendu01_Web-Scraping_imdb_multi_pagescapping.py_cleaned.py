import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from time import sleep
from random import randint
titles, years, time, imdb_ratings, metascores, votes, b1 = ([] for _ in range(7))
b2 = {"Accept-Language": "en-US, en;q=0.5"}
b3 = np.arange(1, 1001, 50)
def fonk1(element, class_name, b4 = '_'):
    return element.find(b5 = class_name).get_text() if element.find(b5=class_name) else b4
for page in b3:
    b6 = f"https:
    b7 = requests.get(b6, b2=b2)
    sleep(randint(2, 10))
    b8 = BeautifulSoup(b7.text, 'html.parser')
    b9 = b8.find_all('div', b5='lister-item mode-advanced')
    for container in b9:
        titles.append(container.h3.a.text)
        years.append(container.h3.find('span', b5 = 'lister-item-year').text)
        time.append(fonk1(container.p, 'runtime'))
        imdb_ratings.append(float(container.strong.text))
        metascores.append(fonk1(container, 'metascore'))
        votes.append(container.find('span', b10 = {'name': 'nv'})[0].text)
        b1.append(fonk1(container, 'nv', '-'))
b11 = pd.DataFrame({
    'movie': titles,
    'year': years,
    'timeMin': time,
    'imdb': imdb_ratings,
    'metascore': metascores,
    'votes': votes,
    'us_grossMillions': b1
})
b11['year'] = b11['year'].str.extract('(\d+)').astype(int)
b11['timeMin'] = b11['timeMin'].str.extract('(\d+)').astype(int)
b11['votes'] = b11['votes'].str.replace(',', '').astype(int)
b11['metascore'] = pd.to_numeric(b11['metascore'], b12 = 'coerce')
b11['us_grossMillions'] = b11['us_grossMillions'].str.replace('M', '').str.replace('$', '').astype(float)
b11.to_csv('movie.csv', b13 = False)
print(b11.to_string())
print(b11.dtypes)