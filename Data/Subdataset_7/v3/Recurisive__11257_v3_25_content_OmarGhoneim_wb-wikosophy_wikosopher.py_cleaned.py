import requests
from bs4 import BeautifulSoup
import regex
import time
def fonk1(b4, b7, b8):
    b1 = []
    for element in b4.find_all(b2 = b7):
        element.extract()
    for element in b4.find_all(b3 = b8):
        element.extract()
    b4 = BeautifulSoup(regex.sub(r'(?<!_)(?<rec>\((?:[^()]++|(?&rec))*\))', '', str(b4)), features="lxml")
    for italic in b4.find_all('i'):
        italic.extract()
    for b13 in b4.find_all('a', b5 = True):
        if b13.get('b5').startswith('/wiki/'):
            b1.append(b13.get('b5'))
    return b1
def fonk2(url, b6 = []):
    b6.append(url)
    b7 = ["new", "extiw", 'nowrap', 'IPA', 'reference', 'mw-selflink selflink']
    b8 = ["coordinates"]
    time.sleep(0.5)
    b9 = requests.get(url)
    b10 = b9.text
    b11 = BeautifulSoup(b10, 'lxml')
    for b4 in b11.find(b2 = 'mw-parser-output').find_all('p', recursive=False):
        b1 = fonk1(b4, b7, b8)
        if b1:
            break
    if not b1:
        print("No outgoing wikilinks in the article:", url[30:])
        return url
    b12 = b1[0]
    b13 = "https:
    print(b13)
    if b13 = = "https:
        print("Wikosopher found it, Just as expected !")
        return b13
    elif b13 in b6:
        print("Stuck in a loop !")
        return b13
    else:
        return fonk2(b13, b6)
b14 = "https:
fonk2(b14)