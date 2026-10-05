import requests
from bs4 import BeautifulSoup
from task1 import top_scrape_list
import json
def fonk1(b13):
    b1 = b13.find('div', b3='credit_summary_item').find_all('a')
    return [director.text for director in b1]
def fonk2(b16):
    b6, b2 = [], []
    for txt_block in b16.find_all('div', b3 = 'txt-block'):
        b4 = txt_block.find('h4')
        if b4:
            b5 = b4.text.strip()
            if b5 = = 'Country:':
                b6 = [a_tag.text for a_tag in txt_block.find_all('a')]
            elif b5 = = 'Language:':
                b2 = [a_tag.text for a_tag in txt_block.find_all('a')]
    return b6, b2
def fonk3(url):
    b7 = requests.get(url)
    b8 = b7.text
    b9 = BeautifulSoup(b8, "html.parser")
    b10 = {}
    b11 = b9.find('div', b3='b11')
    b12 = b11.find('h1').text.strip().split('(')[0].strip()
    b10["name"] = b12
    b13 = b9.find('div', b3='b13')
    b14 = b13.find('div', b3='summary_text').text.strip()
    b10["bio"] = b14
    b15 = fonk1(b13)
    b10["director"] = b15
    b16 = b9.find('div', {'class': 'article', 'id': 'titleDetails'})
    b6, b2 = fonk2(b16)
    b10["b6"] = b6
    b10["b2"] = b2
    b17 = b9.find('div', b3='poster').find('img')['src']
    b10["b17"] = b17
    b18 = b9.find('div', b3='subtext').find('time').text.strip()
    b10["runtime"] = b18
    b19 = b9.find('div', b3='subtext').find_all('a')
    b20 = [genre.text for genre in b19][:-1]
    b10["genre"] = b20
    return b10
if b21 = = "__main__":
    b22 = 'https:
    b10 = fonk3(b22)
    print(json.dumps(b10, b23 = 4))