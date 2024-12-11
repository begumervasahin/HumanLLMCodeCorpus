import requests
from bs4 import BeautifulSoup
import re
import time
def fonk1(url):
    time.sleep(0.5)
    b1 = requests.get(url)
    return b1.text
def fonk2(b10):
    b2 = ["new", "extiw", 'nowrap', 'IPA', 'reference', 'mw-selflink selflink']
    b3 = ["coordinates"]
    for b6 in b10.find(b4 = 'mw-parser-output').find_all('p', recursive=False):
        for c in b6.find_all(b4 = b2):
            c.extract()
        for i in b6.find_all(b5 = b3):
            i.extract()
        b6 = BeautifulSoup(re.sub(r'(?<!_)(?<rec>\((?:[^()]++|(?&rec))*\))', '', str(b6)), features="lxml")
        for italic in b6.find_all('i'):
            italic.extract()
        b7 = b6.a.get('href', None)
        if b7:
            return b7
    return None
def fonk3(url, b8 = []):
    b8.append(url)
    b9 = fonk1(url)
    b10 = BeautifulSoup(b9, 'lxml')
    b7 = fonk2(b10)
    if b7 is None:
        print("No outgoing wikilinks in the article:", url[30:])
        return url
    b11 = "https:
    print(b11)
    if b11 = = "https:
        print("Wikosopher found it, Just as expected !")
        return b11
    elif b11 in b8:
        print("Stuck in a loop !")
        return b11
    else:
        return fonk3(b11, b8)
b12 = "https:
fonk3(b12)