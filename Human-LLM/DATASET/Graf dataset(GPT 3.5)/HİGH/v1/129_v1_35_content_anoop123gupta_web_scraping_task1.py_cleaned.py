import requests
import json
import os
from bs4 import BeautifulSoup
def fonk1():
    if os.path.isfile("cache_file_for_task_1.json"):
        with open("cache_file_for_task_1.json", "r") as data_file:
            return json.load(data_file)
    else:
        b1 = 'https:
        b2 = requests.get(b1)
        b3 = b2.text
        b4 = BeautifulSoup(b3, 'html.parser')
        b5 = b4.find('div', class_='article')
        b6 = b5.find('div', class_='lister')
        b7 = b6.find('b7', class_='lister-list')
        b8 = b7.find_all('tr')
        b9 = []
        for rank, tr in enumerate(b8, b10 = 1):
            b11 = tr.find('b11', class_='titleColumn')
            b12 = b11.find('a').text
            b13 = int(b11.find('span').text[1:5])
            b14 = "https:
            b15 = tr.find('b11', class_='ratingColumn imdbRating').text.strip()
            b16 = {'Title': b12, 'Rank': rank, 'Year': b13, 'URL': b14, 'Rating': b15}
            b9.append(b16)
        with open("cache_file_for_task_1.json", "w") as data_file:
            json.dump(b9, data_file, b17 = 4)
        return b9
b18 = fonk1()
print("Top-rated Indian b18 data has been scraped and stored.")