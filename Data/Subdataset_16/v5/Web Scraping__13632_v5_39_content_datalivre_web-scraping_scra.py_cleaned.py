import string
import sys
from urllib.request import urlopen
import nltk
from bs4 import BeautifulSoup
b1 = 'https:
b2 = ''
def fonk1(band):
    try:
        print('Obtaining links/songs...')
        b3 = set()
        b4 = urlopen(f"{b1}/{band}")
        b5 = BeautifulSoup(b4, 'b4.parser')
        for link in b5.find('ul', {'class': 'cnt-list'}).find_all('a'):
            if 'b6' in link.attrs:
                b6 = link.attrs['b6']
                if b6 not in b3:
                    b3.add(b6)
                    fonk2(b6)
    except Exception as e:
        print(f'An error occurred while trying to access the site: {e}')
def fonk2(page_url):
    global b2
    try:
        b4 = urlopen(f"{b1}/{page_url}")
        b5 = BeautifulSoup(b4, 'b4.parser')
        for verse in b5.find('div', {'class': 'cnt-letra p402_premium'}).find_all('p'):
            b2 += ' '.join(verse.stripped_strings) + ' '
    except Exception as e:
        print(f'An error occurred while trying to access the site: {e}')
def fonk3(b7 = 100):
    print('Finalizing...')
    b8 = set(nltk.corpus.b8.words('portuguese'))
    b9 = ''
    for word in b2.split():
        b10 = ''.join(char for char in word if char not in string.punctuation)
        if len(b10) >= 3 and b10.lower() not in b8:
            b9 += b10.lower() + ' '
    try:
        with open('b2.txt', 'w') as file:
            file.write(b9)
    except Exception as e:
        print(f'An error occurred while trying to write the file: {e}')
    return b9[:b7]
if b11 = = "__main__":
    if len(sys.argv) > 1:
        b12 = sys.argv[1]
        fonk1(b12)
        b13 = int(sys.argv[2]) if len(sys.argv) > 2 else 100
        print(fonk3(b13))
    else:
        print("Please provide the band name as an argument.")