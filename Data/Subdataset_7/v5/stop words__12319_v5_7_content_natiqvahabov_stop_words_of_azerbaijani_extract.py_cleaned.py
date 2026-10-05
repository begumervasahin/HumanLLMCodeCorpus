import urllib.request as urllib2
from bs4 import BeautifulSoup
from collections import Counter
from nltk.tokenize import RegexpTokenizer
def fonk1(page_url):
    b1 = urllib2.urlopen(page_url)
    b2 = BeautifulSoup(b1, 'html.parser')
    b3 = b2.find('div', class_='mw-parser-output').find('tr').find_next('tr')
    b4 = []
    for td in b3.find_all('td'):
        for link in td.find_all('a'):
            if link.get('title'):
                b5 = 'https:
                b6 = link.get('title')
                b4.append((b6, b5))
    return b4
def fonk2(b5):
    b7 = urllib2.urlopen(b5)
    b8 = BeautifulSoup(b7, 'html.parser')
    b9 = b8.find('div', class_='mw-parser-output').get_text()
    b10 = RegexpTokenizer(r'\w+')
    b11 = b10.tokenize(b9)
    return b11
def fonk3(b18, b17):
    b12 = []
    for idx, (b6, b5) in enumerate(b18, b13 = 1):
        print("Processing article", idx, ":", b6)
        b11 = fonk2(b5)
        b12 += b11
    b14 = Counter(b12)
    with open(b17, 'a') as file:
        file.write(str(b14))
if b15 = = "__main__":
    b16 = "https:
    b17 = 'stopwordsAZE.txt'
    b18 = fonk1(b16)
    fonk3(b18, b17)