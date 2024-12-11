import requests
from bs4 import BeautifulSoup
import regex
import time
def fonk1(url, b1 = []):
    b1.append(url)
    b2 = ["new", "extiw", 'nowrap', 'IPA',
                        'reference', 'mw-selflink selflink']
    b3 = ["coordinates"]
    time.sleep(0.5)
    b4 = requests.get(url)
    b5 = b4.text
    b6 = BeautifulSoup(b5, 'lxml')
    b7 = True
    for b10 in b6.find(b8 = 'mw-parser-output').find_all('b10', recursive=False):
        for c in b10.find_all(b8 = b2):
            c.extract()
        for i in b10.find_all(b9 = b3):
            i.extract()
        b10 = BeautifulSoup(regex.sub(b4'(?<!_)(?<rec>\((?:[^()]++|(?&rec))*\))',
                                    '', str(b10)), b11 = "lxml")
        for italic in b10.find_all('i'):
            italic.extract()
        try:
            b12 = b10.a.get('href')
        except:
            continue
        b7 = False
        break
    if(b7):
        print("No outgoing wikilinks in the article:", url[30:])
        return url
    else:
        b13 = "https:
        print(b13)
    if(b13 = = "https:
        print("Wikosopher found it, Just as expected !")
        return b13
    elif(b13 in b1):
        print("Stuck in a loop !")
        return b13
    else:
        return(fonk1(b13, b1))
b14 = "https:
fonk1(b14)