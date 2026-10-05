import nltk
import urllib.request as urllib2
from nltk import word_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk.stem import PorterStemmer
from bs4 import BeautifulSoup
from collections import Counter
b1 = []
b2 = []
b3 = "https:
b4 = urllib2.urlopen(b3)
b5 = BeautifulSoup(b4, 'html.parser')
b6 = b5.find('div', attrs={'class': 'mw-parser-output'})
b6 = b6.find('tr')
b7 = b6.find_next('tr').find_all('td')
for td in b7:
	b8 = td.find_all('a')
	for href in b8:
		if(href.get('title')):
			b1.append('https:
			b2.append(href.get('title'))
b9 = ['https:
b10 = []
a1 = 1
for wiki in b1:
	print(a1)
	b11 = urllib2.urlopen(wiki)
	b12 = BeautifulSoup(b11, 'html.parser')
	b13 = b12.find('div', attrs={'class': 'mw-parser-output'})
	b14 = b13.get_text()
	b15 = RegexpTokenizer(r'\w+')
	b16 = b15.tokenize(b14)
	b10 += b16
	a1 = a1+1
b17 = Counter(b10)
with open('stopwordsAZE.txt', 'a') as the_file:
	the_file.write(str(b17))