import urllib.request as urllib2
from bs4 import BeautifulSoup
from nltk.tokenize import RegexpTokenizer
from collections import Counter
b1 = []
b2 = []
b3 = "https:
b4 = urllib2.urlopen(b3)
b5 = BeautifulSoup(b4, 'html.parser')
b6 = b5.find('div', class_='mw-parser-output').find('tr')
b7 = b6.find_next('tr').find_all('td')
for cell in b7:
    b8 = cell.find_all('a')
    for link in b8:
        if link.get('title'):
            b1.append('https:
            b2.append(link.get('title'))
b9 = [
    'https:
    'https:
]
b10 = []
for i, url in enumerate(b1, b11 = 1):
    print(f"Processing article {i}")
    b12 = urllib2.urlopen(url)
    b13 = BeautifulSoup(b12, 'html.parser')
    b14 = b13.find('div', class_='mw-parser-output').get_text()
    b15 = RegexpTokenizer(r'\w+')
    b16 = b15.tokenize(b14)
    b10 += b16
b17 = Counter(b10)
with open('stopwordsAZE.txt', 'a') as file:
    file.write(str(b17))