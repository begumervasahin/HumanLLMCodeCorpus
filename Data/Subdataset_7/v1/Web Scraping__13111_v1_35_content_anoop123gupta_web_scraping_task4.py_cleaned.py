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
    b9 = b8.find('div', b13='title_wrapper').find('h1').text.strip()
    b2["b9"] = b9.split('(')[0].strip()
    b10 = b8.find('div', b13='plot_summary_wrapper').find('div', b13='summary_text').text.strip()
    b2["bio"] = b10
    b11 = b8.find('div', b13='plot_summary_wrapper').find('div', b13='credit_summary_item').find_all('a')
    b3 = [director.text for director in b11]
    b2["director"] = b3
    b12 = b8.find('div', {'class': 'article', 'id': 'titleDetails'})
    for txt_block in b12.find_all('div', b13 = 'txt-block'):
        b14 = txt_block.find('h4')
        if b14:
            b15 = b14.text.strip()
            if b15 = = 'Country:':
                b16 = [a_tag.text for a_tag in txt_block.find_all('a')]
                b2["b16"] = b16
            elif b15 = = 'Language:':
                b4 = [a_tag.text for a_tag in txt_block.find_all('a')]
                b2["language"] = b4
    b17 = b8.find('div', b13='poster').find('img')['src']
    b2["b17"] = b17
    b18 = b8.find('div', b13='subtext').find('time').text.strip()
    b2["runtime"] = b18
    b19 = b8.find('div', b13='subtext').find_all('a')
    b5 = [genre.text for genre in b19][:-1]
    b2["genre"] = b5
    return b2
if b20 = = "__main__":
    b21 = 'https:
    b2 = fonk1(b21)
    print(json.dumps(b2, b22 = 4))