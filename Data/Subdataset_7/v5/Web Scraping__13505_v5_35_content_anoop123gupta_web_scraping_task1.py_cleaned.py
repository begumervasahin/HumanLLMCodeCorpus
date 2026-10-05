import requests
import json
import os
from bs4 import BeautifulSoup
def fonk1():
    b1 = "cache_file_for_task_1.json"
    if os.path.isfile(b1):
        with open(b1, "r") as cache_file:
            return json.load(cache_file)
    else:
        b2 = 'https:
        b3 = requests.get(b2)
        b4 = BeautifulSoup(b3.text, 'html.parser')
        b5 = b4.find('div', class_='article')
        b6 = b5.find('div', class_='lister')
        b7 = b6.find('tbody', class_='lister-list').find_all('tr')
        b8 = []
        b9 = set()
        for rank, movie_row in enumerate(b7, b10 = 1):
            b11 = movie_row.find('td', class_='titleColumn')
            b12 = b11.find('a').text
            b13 = int(b11.find('span').text[1:5])
            b14 = "https:
            b15 = movie_row.find('td', class_='ratingColumn imdbRating').text.strip()
            b9.add(b13)
            b16 = {'Title': b12, 'Rank': rank, 'Year': b13, 'URL': b14, 'Rating': b15}
            b8.append(b16)
        with open(b1, "w") as cache_file:
            json.dump(b8, cache_file)
        return b8
b8 = fonk1()