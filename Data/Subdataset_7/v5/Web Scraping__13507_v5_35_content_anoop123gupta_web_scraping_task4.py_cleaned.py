import requests
from bs4 import BeautifulSoup
from task1 import top_scrape_list
def fonk1(url):
    b1 = top_scrape_list()
    b2 = {}
    b3 = requests.get(url)
    b4 = b3.text
    b5 = BeautifulSoup(b4, "html.parser")
    b6 = b5.find('div', class_='b6')
    b7 = b6.find('h1').text.split('(')[0].strip()
    b2["name"] = b7
    b8 = b5.find('div', class_='b8')
    b9 = b8.find('div', class_='b9').text.strip()
    b2["bio"] = b9
    b10 = b8.find('div', class_='b10')
    b11 = b10.find('a').text
    b2["b11"] = [b11]
    b12 = b5.find('div', attrs={"class": "article", "id": "titleDetails"})
    b13 = b12.find_all('div', class_='txt-block')
    for block in b13:
        b14 = block.find('h4').text
        if b14 = = 'Country:':
            b15 = block.find_all('a')
            b16 = [country.text for country in b15]
            b2["country"] = b16
        elif b14 = = 'Language:':
            b17 = block.find_all('a')
            b18 = [language.text for language in b17]
            b2["language"] = b18
    b19 = b5.find('div', class_='poster')
    b20 = b19.find('img').get('src')
    b2["b20"] = b20
    b21 = b5.find('div', class_='subtext')
    b22 = b21.find('time')
    b23 = int(b22.text.strip('min').strip('h')) * 60 if 'h' in b22.text else 0
    b24 = int(b22.text.strip('min').strip()) if 'min' in b22.text else 0
    b25 = b23 + b24
    b2["runtime"] = f"{b25} min"
    b26 = b21.find_all('a')
    b27 = [genre.text for genre in b26][:-1]
    b2["genre"] = b27
    return b2
b2 = fonk1('https:
print(b2)