import requests
from bs4 import BeautifulSoup
from task1 import top_scrape_list
import pprint
import json
import os
def fonk1(url):
    b1 = top_scrape_list()
    b2 = {}
    b3 = []
    b4 = []
    b5 = []
    b6 = requests.get(url)
    b7 = b6.text
    b8 = BeautifulSoup(b7, "html.parser")
    b9 = b8.find('div', class_='b9')
    b10 = b9.find('h1').text.split('(')[0].strip()
    b2["name"] = b10
    b11 = b8.find('div', class_='b11')
    b12 = b11.find('div', class_='b12').text.strip()
    b2["bio"] = b12
    b13 = b11.find('div', class_='b13')
    b14 = b13.find('a').text
    b3.append(b14)
    b2["b14"] = b3
    b15 = b8.find('div', attrs={"class": "article", "id": "titleDetails"})
    b16 = b15.find_all('div', class_='txt-block')
    for block in b16:
        b17 = block.find('h4').text
        if b17 = = 'Country:':
            b18 = block.find_all('a')
            b19 = [country.text for country in b18]
            b2["country"] = b19
        elif b17 = = 'Language:':
            b20 = block.find_all('a')
            b21 = [language.text for language in b20]
            b2["language"] = b21
    b22 = b8.find('div', class_='poster')
    b23 = b22.find('img').get('src')
    b2["b23"] = b23
    b24 = b8.find('div', class_='subtext')
    b25 = b24.find('time')
    b26 = int(b25.text.strip('min').strip('h')) * 60 if 'h' in b25.text else 0
    b27 = int(b25.text.strip('min').strip()) if 'min' in b25.text else 0
    b28 = b26 + b27
    b2["runtime"] = f"{b28} min"
    b29 = b24.find_all('a')
    b30 = [genre.text for genre in b29][:-1]
    b2["genre"] = b30
    return b2
b2 = fonk1('https:
print(b2)