import requests
from bs4 import BeautifulSoup
import regex as re
import time
def fonk1(url, b1 = None):
    if b1 is None:
        b1 = []
    b1.append(url)
    b2 = ["new", "extiw", 'nowrap', 'IPA', 'reference', 'mw-selflink selflink']
    b3 = ["coordinates"]
    time.sleep(0.5)
    b4 = requests.get(url)
    b5 = BeautifulSoup(b4.text, 'lxml')
    b6 = True
    for paragraph in b5.find(b7 = 'mw-parser-output').find_all('p', recursive=False):
        for cls in b2:
            for element in paragraph.find_all(b7 = cls):
                element.extract()
        for id_ in b3:
            for element in paragraph.find_all(b8 = id_):
                element.extract()
        b9 = re.sub(r'(?<!_)(?<rec>\((?:[^()]++|(?&rec))*\))', '', str(paragraph))
        b10 = BeautifulSoup(b9, 'lxml')
        for italic in b10.find_all('i'):
            italic.extract()
        b11 = b10.find('a', href=True)
        if b11:
            b12 = b11['href']
            b6 = False
            break
    if b6:
        print(f"No outgoing wikilinks in the article: {url[30:]}")
        return url
    b13 = "https:
    print(b13)
    if b13 = = "https:
        print("Philosophy page found!")
        return b13
    elif b13 in b1:
        print("Stuck in a loop!")
        return b13
    else:
        return fonk1(b13, b1)
if b14 = = "__main__":
    b15 = "https:
    fonk1(b15)