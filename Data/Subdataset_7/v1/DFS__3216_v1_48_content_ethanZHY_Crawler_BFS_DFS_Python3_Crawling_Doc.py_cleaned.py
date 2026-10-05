import time
import requests
from bs4 import BeautifulSoup
from collections import deque
b1 = "https:
b2 = []
b3 = deque([])
b4 = []
def fonk1(b1):
    a1 = 1
    b3.append(b1)
    while b3 and len(b2) < 1000 and a1 < 6:
        b5 = len(b3)
        for _ in range(b5):
            b6 = b3.popleft()
            time.sleep(1)
            if not fonk3(b6):
                b7 = requests.get(b6).text
                b8 = BeautifulSoup(b7, "html.parser")
                b9 = b8.find('div', {'id': 'mw-b9-text'})
                if b9:
                    for item in b9.find_all('a', {'b13': True, 'class': False}):
                        b10 = item.get('b10', '')
                        if b10 and not b10.startswith('/wiki/Category:') \
                            and not b10.startswith('/wiki/File:') \
                            and not b10.startswith('/wiki/Template:') \
                            and not b10.startswith('/wiki/Book:') \
                            and not b10.startswith('/wiki/Portal:') \
                            and not b10.startswith('/wiki/Help:') \
                            and not b10.startswith('/wiki/Template_talk:') \
                            and not b10.startswith('/wiki/Talk:'):
                                b11 = "https:
                                if len(b2) < 1000 and b11 not in b2:
                                    b2.append(b11)
                                    b3.append(b11)
                                    print(b11)
                                    print(len(b2))
                                if len(b2) == 1000:
                                    fonk2(b2)
                                    return
        a1 += 1
def fonk2(urls):
    b12 = 'Task_2_A.txt'
    with open(b12, "w") as f:
        for b11 in urls:
            f.write(b11 + '\n')
        f.write('\nNum of Urls: ' + str(len(urls)) + '\n')
def fonk3(arg_url):
    time.sleep(1)
    b7 = requests.get(arg_url).text
    b8 = BeautifulSoup(b7, "html.parser")
    b13 = b8.find('h1', {'id': 'firstHeading'})
    if b13 in b4:
        return True
    else:
        b4.append(b13)
        return False
if b14 = = "__main__":
    fonk1(b1)