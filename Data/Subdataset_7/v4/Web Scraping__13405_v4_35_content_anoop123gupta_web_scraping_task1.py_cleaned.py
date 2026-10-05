import requests
import json
import os
from bs4 import BeautifulSoup
def fonk1():
    if os.path.isfile("cache_file_for_task_1.json"):
        with open("cache_file_for_task_1.json", "r+") as data_file:
            b1 = json.load(data_file)
            return b1
    else:
        b2 = 'https:
        b3 = requests.get(b2)
        b4 = b3.text
        b5 = BeautifulSoup(b4, 'html.parser')
        b6 = b5.find('div', class_='article')
        b7 = b6.find('div', class_='lister')
        b8 = b7.find('b8', class_='lister-list')
        b9 = b8.find_all('tr')
        b10 = []
        a1 = 0
        b11 = []
        for tr in b9:
            a1 += 1
            b12 = tr.find('b12', class_='titleColumn')
            b13 = b12.find('a').text
            b14 = int(b12.find('span').text[1:5])
            if b14 not in b11:
                b11.append(b14)
            b15 = "https:
            b16 = tr.find('b12', class_='ratingColumn imdbRating').text.strip()
            b17 = {'Title': b13, 'Rank': a1, 'Year': b14, 'URL': b15, 'Rating': b16}
            b10.append(b17)
        with open("cache_file_for_task_1.json", "w") as cache_file:
            json.dump(b10, cache_file)
        return b10
b18 = fonk1()