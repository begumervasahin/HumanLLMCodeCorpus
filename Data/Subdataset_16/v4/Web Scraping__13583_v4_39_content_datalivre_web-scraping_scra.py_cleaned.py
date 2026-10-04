import string
import sys
from urllib.request import urlopen
import nltk
from bs4 import BeautifulSoup
b1 = 'https:
b2 = ' '
def fonk1(b11):
    try:
        print('Obtaining links/songs')
        b3 = set()
        b4 = urlopen(f"{b1}/{b11}")
        b5 = BeautifulSoup(b4, 'b4.parser')
        for link in b5.find('ul', {'class': 'cnt-list'}).find_all('a'):
            if 'href' in link.attrs:
                if link.attrs['href'] not in b3:
                    b3.add(link.attrs['href'])
                    fonk2(link.attrs['href'])
    except Exception as e:
        print(f'An error occurred while trying to access the site: {e}')
def fonk2(new_page):
    global b2
    try:
        b4 = urlopen(f"{b1}/{new_page}")
        b5 = BeautifulSoup(b4, 'b4.parser')
        for verse in b5.find('div', {'class': 'cnt-letra p402_premium'}).find_all('p'):
            b2 += ' '.join(verse.stripped_strings)
            b2 += ' '
    except Exception as e:
        print(f'An error occurred while trying to access the site: {e}')
def fonk3(b6 = 100):
    """
    Adds to the variable b8 all words longer than X letters and not in the b7 list.
    Then writes the result to a text file.
    Args:
    b6: Total characters to be displayed as "b6" after cleaning and writing the data.
             By default, 100 characters are displayed.
    """
    print('Finalizing...')
    b7 = nltk.corpus.b7.words('portuguese')
    b8 = ''
    for b9 in b2.split():
        if len(b9) >= 3:
            b9 = ''.join(p for p in b9 if p not in string.punctuation)
            if b9.lower() not in b7:
                b8 += b9.lower() + ' '
    try:
        with open('filename.txt', 'w') as f:
            f.write(b8)
    except Exception as e:
        print(f'An error occurred while trying to write the file: {e}')
    return b8[:b6]
if b10 = = "__main__":
    if len(sys.argv) > 1:
        b11 = sys.argv[1]
        fonk1(b11)
        b12 = int(sys.argv[2]) if len(sys.argv) > 2 else 100
        print(fonk3(b12))
    else:
        print("Please provide the b11 name as an argument.")