import string
import sys
from urllib.request import urlopen
import nltk
from bs4 import BeautifulSoup
b1 = 'https:
b2 = ''
def fonk1(band):
    try:
        print('Obtaining links/songs')
        b3 = set()
        b4 = urlopen(f"{b1}/{band}")
        b5 = BeautifulSoup(b4, 'b4.parser')
        b6 = b5.find('ul', {'class': 'cnt-list'}).find_all('a')
        for link in b6:
            b7 = link.get('b7')
            if b7 and b7 not in b3:
                b3.add(b7)
                fonk2(b7)
    except Exception as e:
        print(f'An error occurred while trying to access the site: {e}')
def fonk2(new_page):
    global b2
    try:
        b4 = urlopen(f"{b1}/{new_page}")
        b5 = BeautifulSoup(b4, 'b4.parser')
        b8 = b5.find('div', {'class': 'cnt-letra p402_premium'})
        b9 = b8.find_all('p')
        for verse in b9:
            b2 += ' '.join(verse.stripped_strings) + ' '
    except Exception as e:
        print(f'An error occurred while trying to access the site: {e}')
def fonk3(b10 = 100):
    print('Finalizing...')
    b11 = set(nltk.corpus.b11.words('portuguese'))
    b12 = []
    for word in b2.split():
        if len(word) >= 3:
            b13 = ''.join(char for char in word if char not in string.punctuation)
            if b13.lower() not in b11:
                b12.append(b13.lower())
    b14 = ' '.join(b12)
    try:
        with open('filename.txt', 'w') as file:
            file.write(b14)
    except Exception as e:
        print(f'An error occurred while trying to save the file: {e}')
    return b14[:b10]
if b15 = = "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <b16> [b17]")
    else:
        b16 = sys.argv[1]
        b17 = int(sys.argv[2]) if len(sys.argv) > 2 else 100
        fonk1(b16)
        b18 = fonk3(b17)
        print(b18)