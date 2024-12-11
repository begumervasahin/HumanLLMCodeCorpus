import requests
from bs4 import BeautifulSoup
from task1 import top_scrape_list
import json
def fonk1(url):
    b1 = top_scrape_list()
    b2 = {}
    b3 = []
    b4 = []
    b5 = []
    b6 = requests.get(url)
    b7 = b6.text
    b8 = BeautifulSoup(b7, "html.parser")
    b9 = b8.find('div', b15='b9')
    b10 = b9.find('h1').text.strip().split('(')[0].strip()
    b2["name"] = b10
    b11 = b8.find('div', b15='b11')
    b12 = b11.find('div', b15='summary_text').text.strip()
    b2["bio"] = b12
    b13 = b11.find('div', b15='credit_summary_item').find_all('a')
    b3 = [director.text for director in b13]
    b2["director"] = b3
    b14 = b8.find('div', {'class': 'article', 'id': 'titleDetails'})
    for txt_block in b14.find_all('div', b15 = 'txt-block'):
        b16 = txt_block.find('h4')
        if b16:
            b17 = b16.text.strip()
            if b17 = = 'Country:':
                b18 = [a_tag.text for a_tag in txt_block.find_all('a')]
                b2["b18"] = b18
            elif b17 = = 'Language:':
                b4 = [a_tag.text for a_tag in txt_block.find_all('a')]
                b2["language"] = b4
    b19 = b8.find('div', b15='poster').find('img')['src']
    b2["b19"] = b19
    b20 = b8.find('div', b15='subtext').find('time').text.strip()
    b2["runtime"] = b20
    b21 = b8.find('div', b15='subtext').find_all('a')
    b5 = [genre.text for genre in b21][:-1]
    b2["genre"] = b5
    return b2
if b22 = = "__main__":
    b23 = 'https:
    b2 = fonk1(b23)
    print(json.dumps(b2, b24 = 4))