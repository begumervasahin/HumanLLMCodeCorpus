import requests
from bs4 import BeautifulSoup
import re
import time
def fonk1(b10):
    b1 = ["new", "extiw", 'nowrap', 'IPA', 'reference', 'mw-selflink selflink']
    b2 = ["coordinates"]
    for b6 in b10.find(b3 = 'mw-parser-output').find_all('p', recursive=False):
        for tag in b6.find_all(b3 = b1):
            tag.extract()
        for tag in b6.find_all(b4 = b2):
            tag.extract()
        b5 = re.sub(r'(?<!_)(?<rec>\((?:[^()]++|(?&rec))*\))', '', str(b6))
        b6 = BeautifulSoup(b5, 'lxml')
        for italic in b6.find_all('i'):
            italic.extract()
        b7 = b6.find('a', href=True)
        if b7:
            return b7['href']
    return None
def fonk2(url, b8 = None):
    if b8 is None:
        b8 = []
    b8.append(url)
    time.sleep(0.5)
    b9 = requests.get(url)
    b10 = BeautifulSoup(b9.text, 'lxml')
    b11 = fonk1(b10)
    if not b11:
        print("No outgoing wikilinks in the article:", url[30:])
        return url
    b12 = "https:
    print(b12)
    if b12 = = "https:
        print("Philosophy page found, just as expected!")
        return b12
    elif b12 in b8:
        print("Stuck in a loop!")
        return b12
    else:
        return fonk2(b12, b8)
if b13 = = "__main__":
    b14 = "https:
    fonk2(b14)