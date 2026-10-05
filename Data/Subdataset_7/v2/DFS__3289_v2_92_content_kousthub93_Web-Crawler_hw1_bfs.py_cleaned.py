import requests
from bs4 import BeautifulSoup
import re
import time
def fonk1(b1, b2, b16, b9):
    for link in b2:
        if link not in b1 and len(link) > 1 and link not in b16:
            b1.append(link)
    for link in b1:
        if link not in b9:
            b9.append(link)
    return b1
def fonk2(next_url, b16, b9):
    b16.append(next_url)
    b1 = []
    b2 = []
    time.sleep(1)
    b3 = requests.get(next_url)
    b4 = b3.text
    b5 = BeautifulSoup(b4, 'html.parser')
    b6 = b5.find('div', {'id': 'mw-content-text'})
    for link in b6.find_all('a', {'href': re.compile("^/wiki")}):
        if ':' not in link.get('href'):
            b7 = "https:
            b8 = b7.split('
            b2.append(str(b8[0]))
    return fonk1(b1, b2, b16, b9)
def fonk3(list_in_use, *lists, b16):
    for link in list_in_use:
        if link not in b16:
            return link
    for lst in lists:
        if len(lst) < 1000:
            return fonk3(lst, *lists, b16)
    return 'links not found'
def fonk4(b17, *lists):
    for lst in lists:
        if b17 in lst:
            return lst
def fonk5(b24):
    b9 = []
    b10 = []
    b11 = []
    b12 = []
    b13 = []
    b14 = []
    b15 = []
    b16 = []
    b9.append(b24)
    b10.append(b24)
    while len(b9) < 1000:
        b17 = fonk3(b10, b10, b11, b12, b13, b14, b15, b16)
        if b17 = = 'links not found':
            print("Crawling ends: No further links found")
            break
        else:
            b18 = fonk4(b17, b10, b11, b12, b13, b14, b15)
            if b18 = = b10:
                b19 = fonk2(b17, b16, b9)
                for link in b19:
                    b11.append(link)
            elif b18 = = b11:
                b20 = fonk2(b17, b16, b9)
                for link in b20:
                    if link not in b10 and link not in b11:
                        b12.append(link)
            elif b18 = = b12:
                b21 = fonk2(b17, b16, b9)
                for link in b21:
                    if link not in b11 and link not in b12:
                        b13.append(link)
            elif b18 = = b13:
                b22 = fonk2(b17, b16, b9)
                for link in b22:
                    if link not in b12 and link not in b13:
                        b14.append(link)
            elif b18 = = b14:
                b23 = fonk2(b17, b16, b9)
                for link in b23:
                    if link not in b13 and link not in b14:
                        b15.append(link)
    with open('TASK 1-E.txt', 'w') as file:
        for url in b9[:1000]:
            file.write(url.lower() + "\n")
b24 = "https:
fonk5(b24)