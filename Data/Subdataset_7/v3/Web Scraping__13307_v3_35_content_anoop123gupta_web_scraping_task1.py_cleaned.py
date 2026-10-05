import requests
import json
import os
from bs4 import BeautifulSoup
def fonk1():
    b1 = "cache_file_for_task_1.json"
    if os.path.isfile(b1):
        return fonk2(b1)
    else:
        return fonk3(b1)
def fonk2(b1):
    with open(b1, "r") as data_file:
        return json.load(data_file)
def fonk3(b1):
    b2 = 'https:
    b3 = requests.get(b2)
    b4 = BeautifulSoup(b3.text, 'html.parser')
    b5 = b4.find('tbody', class_='lister-list')
    if not b5:
        raise ValueError("Failed to find movie data b5 on the webpage.")
    b6 = []
    for rank, row in enumerate(b5.find_all('tr'), b7 = 1):
        b8 = fonk4(rank, row)
        b6.append(b8)
    fonk5(b1, b6)
    return b6
def fonk4(rank, row):
    b9 = row.find('td', class_='titleColumn')
    b10 = b9.find('a').text.strip()
    b11 = int(b9.find('span').text[1:5])
    b12 = "https:
    b13 = row.find('td', class_='ratingColumn imdbRating').text.strip()
    return {'Title': b10, 'Rank': rank, 'Year': b11, 'URL': b12, 'Rating': b13}
def fonk5(b1, data):
    with open(b1, "w") as data_file:
        json.dump(data, data_file, b14 = 4)
def fonk6():
    try:
        b15 = fonk1()
        print("Top-rated Indian b15 data has been scraped and stored.")
    except Exception as e:
        print(f"An error occurred: {e}")
if b16 = = "__main__":
    fonk6()