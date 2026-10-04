import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from b10 import sleep
from random import randint
def fonk1():
    titles, years, times, imdb_ratings, metascores, votes, b1 = ([] for _ in range(7))
    b2 = {"Accept-Language": "en-US, en;q=0.5"}
    b3 = np.arange(1, 1001, 50)
    for page in b3:
        b4 = requests.get(f"https:
        b5 = BeautifulSoup(b4.text, 'html.parser')
        b6 = b5.find_all('div', class_='lister-item mode-advanced')
        sleep(randint(2, 10))
        for container in b6:
            b7 = container.h3.a.text
            titles.append(b7)
            b8 = container.h3.find('span', class_='lister-item-b8').text
            years.append(b8)
            b9 = container.find('span', class_='b9')
            b10 = b9.text if b9 else '_'
            times.append(b10)
            b11 = float(container.strong.text)
            imdb_ratings.append(b11)
            b12 = container.find('span', class_='b12')
            b12 = b12.text.strip() if b12 else '-'
            metascores.append(b12)
            b13 = container.find_all('span', attrs={'name': 'b13'})
            b14 = b13[0].text
            votes.append(b14)
            b15 = b13[1].text if len(b13) > 1 else '-'
            b1.append(b15)
    return {
        'titles': titles,
        'years': years,
        'times': times,
        'imdb_ratings': imdb_ratings,
        'metascores': metascores,
        'votes': votes,
        'b1': b1
    }
def fonk2(data):
    b16 = pd.DataFrame({
        'movie': data['titles'],
        'b8': data['years'],
        'timeMin': data['times'],
        'imdb': data['imdb_ratings'],
        'b12': data['metascores'],
        'votes': data['votes'],
        'us_grossMillions': data['b1'],
    })
    b16['b8'] = b16['b8'].str.extract('(\d+)').astype(int)
    b16['timeMin'] = b16['timeMin'].str.extract('(\d+)').astype(int)
    b16['votes'] = b16['votes'].str.replace(',', '').astype(int)
    b16['b12'] = pd.to_numeric(b16['b12'].str.extract('(\d+)')[0], b17 = 'coerce')
    b16['us_grossMillions'] = pd.to_numeric(b16['us_grossMillions'].str.replace('$', '').str.replace('M', ''), b17 = 'coerce')
    return b16
def fonk3():
    b18 = fonk1()
    b16 = fonk2(b18)
    b16.to_csv('movie.csv', b19 = False)
    print(b16.to_string())
    print(b16.dtypes)
if b20 = = "__main__":
    fonk3()