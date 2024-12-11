import nltk
import urllib.request as urllib2
from nltk.tokenize import RegexpTokenizer
from bs4 import BeautifulSoup
from collections import Counter
b1 = "https:
b2 = urllib2.urlopen(b1)
b3 = BeautifulSoup(b2, 'html.parser')
b4 = b3.find('div', attrs={'class': 'mw-parser-output'}).find('tr').find_next('tr')
b5 = []
b6 = []
for td in b4.find_all('td'):
    for link in td.find_all('a'):
        if link.get('title'):
            b5.append('https:
            b6.append(link.get('title'))
b7 = ['https:
b8 = []
for idx, wiki_url in enumerate(b5, b9 = 1):
    print("Processing article", idx)
    b10 = urllib2.urlopen(wiki_url)
    b11 = BeautifulSoup(b10, 'html.parser')
    b12 = b11.find('div', attrs={'class': 'mw-parser-output'}).get_text()
    b13 = RegexpTokenizer(r'\w+')
    b14 = b13.tokenize(b12)
    b8 += b14
b15 = Counter(b8)
with open('stopwordsAZE.txt', 'a') as file:
    file.write(str(b15))