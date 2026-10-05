import requests
from bs4 import BeautifulSoup
import regex
import time
def fonk1(url, b1 = []):
    b1.append(url)
    b2 = ["new", "extiw", 'nowrap', 'IPA', 'reference', 'mw-selflink selflink']
    b3 = ["coordinates"]
    time.sleep(0.5)
    b4 = requests.get(url)
    b5 = b4.text
    b6 = BeautifulSoup(b5, 'lxml')
    b7 = True
    for b10 in b6.find(b8 = 'mw-parser-output').find_all('p', recursive=False):
        for element in b10.find_all(b8 = b2):
            element.extract()
        for element in b10.find_all(b9 = b3):
            element.extract()
        b10 = BeautifulSoup(regex.sub(r'(?<!_)(?<rec>\((?:[^()]++|(?&rec))*\))', '', str(b10)), features="lxml")
        for italic in b10.find_all('i'):
            italic.extract()
        try:
            b11 = b10.a.get('href')
        except:
            continue
        b7 = False
        break
    if b7:
        print("No outgoing wikilinks in the article:", url[30:])
        return url
    else:
        b12 = "https:
        print(b12)
    if b12 = = "https:
        print("Wikosopher found it, Just as expected !")
        return b12
    elif b12 in b1:
        print("Stuck in a loop !")
        return b12
    else:
        return fonk1(b12, b1)
b13 = "https:
fonk1(b13)