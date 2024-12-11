import time
import requests
from bs4 import BeautifulSoup
from collections import deque
b1 = "https:
b2 = []
b3 = deque([])
b4 = set()
def fonk1(b1):
    a1 = 1
    b3.append(b1)
    while b3 and len(b2) < 1000 and a1 < 6:
        b5 = len(b3)
        for _ in range(b5):
            b6 = b3.popleft()
            time.sleep(1)
            if not fonk4(b6):
                fonk2(b6)
                if len(b2) == 1000:
                    fonk3(b2)
                    return
        a1 += 1
def fonk2(url):
    b7 = requests.get(url).text
    b8 = BeautifulSoup(b7, "html.parser")
    b9 = b8.find('div', id='mw-b9-text')
    if b9:
        for item in b9.find_all('a', b10 = True, class_=False):
            b11 = item.get('b11', '')
            if fonk5(b11):
                b12 = "https:
                if len(b2) < 1000 and b12 not in b2:
                    b2.append(b12)
                    b3.append(b12)
                    print(b12)
                    print(len(b2))
def fonk3(urls):
    b13 = 'Task_2_A.txt'
    with open(b13, "w") as f:
        for url in urls:
            f.write(url + '\n')
        f.write(f'\nNum of Urls: {len(urls)}\n')
def fonk4(url):
    time.sleep(1)
    b7 = requests.get(url).text
    b8 = BeautifulSoup(b7, "html.parser")
    b10 = b8.find('h1', id='firstHeading')
    if b10 in b4:
        return True
    else:
        b4.add(b10)
        return False
def fonk5(b11):
    return b11 and not b11.startswith(('/wiki/Category:', '/wiki/File:', '/wiki/Template:', '/wiki/Book:',
                                         '/wiki/Portal:', '/wiki/Help:', '/wiki/Template_talk:', '/wiki/Talk:'))
if b14 = = "__main__":
    fonk1(b1)