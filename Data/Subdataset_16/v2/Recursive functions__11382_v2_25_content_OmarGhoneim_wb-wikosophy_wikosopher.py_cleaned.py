import requests
from bs4 import BeautifulSoup
import re
import time
def fonk1(url, b1 = []):
    b1.append(url)
    b2 = ["new", "extiw", 'nowrap', 'IPA', 'reference', 'mw-selflink selflink']
    b3 = ["coordinates"]
    time.sleep(0.5)
    b4 = requests.get(url)
    b5 = BeautifulSoup(b4.text, 'lxml')
    b6 = True
    for b9 in b5.find(b7 = 'mw-parser-output').find_all('p', recursive=False):
        for tag in b9.find_all(b7 = b2):
            tag.extract()
        for tag in b9.find_all(b8 = b3):
            tag.extract()
        b9 = BeautifulSoup(re.sub(r'(?<!_)(?<rec>\((?:[^()]++|(?&rec))*\))', '', str(b9)), 'lxml')
        for italic in b9.find_all('i'):
            italic.extract()
        try:
            b10 = b9.a.get('href')
            b6 = False
            break
        except AttributeError:
            continue
    if b6:
        print("No outgoing wikilinks in the article:", url[30:])
        return url
    else:
        b11 = "https:
        print(b11)
    if b11 = = "https:
        print("Philosophy page found, just as expected!")
        return b11
    elif b11 in b1:
        print("Stuck in a loop!")
        return b11
    else:
        return fonk1(b11, b1)
if b12 = = "__main__":
    b13 = "https:
    fonk1(b13)