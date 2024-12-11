import urllib.request as urllib2
from bs4 import BeautifulSoup
from nltk.tokenize import RegexpTokenizer
from collections import Counter
b1 = "https:
def fonk1(url):
    b2 = []
    b3 = urllib2.urlopen(url)
    b4 = BeautifulSoup(b3, 'html.parser')
    b5 = b4.find('b5', class_='mw-b13-ltr')
    if b5:
        b6 = b5.find_all('a')
        for link in b6:
            b2.append('https:
    return b2
def fonk2(text):
    b7 = RegexpTokenizer(r'\w+')
    return b7.tokenize(text)
def fonk3(b14, filename):
    b8 = Counter(b14)
    with open(filename, 'a') as file:
        for token, count in b8.items():
            file.write(f"{token}: {count}\n")
def fonk4():
    b2 = fonk1(b1)
    b9 = []
    for i, url in enumerate(b2, b10 = 1):
        print(f"Processing article {i}/{len(b2)}")
        b11 = urllib2.urlopen(url)
        b12 = BeautifulSoup(b11, 'html.parser')
        b13 = b12.find('div', class_='mw-parser-output').get_text()
        b14 = fonk2(b13)
        b9.extend(b14)
    fonk3(b9, 'stopwordsAZE.txt')
    print("Token counts written to file.")
if b15 = = "__main__":
    fonk4()