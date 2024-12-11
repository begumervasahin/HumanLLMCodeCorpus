import time
import requests
from bs4 import BeautifulSoup
import re
from collections import deque
b1 = "https:
b2 = []
b3 = deque([])
b4 = []
def fonk1(b1):
    a1 = 1
    b3.append(b1)
    while (len(b3)) != 0 and len(b2) < 1000 and a1 < 6:
        b5 = len(b3)
        for i in range (0,b5):
            b6 = b3.popleft()
            time.sleep(1)
            b7 = requests.get(b6).text
            b8 = BeautifulSoup(b7, "html.parser")
            b9 = b8.find('div', {'id': 'mw-b9-text'})
            for item in b9.findAll('a', {'b13': True} and {'class': False}):
                if ('
                and not item.get('href').startswith('/wiki/Category:') \
                and not item.get('href').startswith('/wiki/File:') \
                and not item.get('href').startswith('/wiki/Template:') \
                and not item.get('href').startswith('/wiki/Book:') \
                and not item.get('href').startswith('/wiki/Portal:') \
                and not item.get('href').startswith('/wiki/Help:') \
                and not item.get('href').startswith('/wiki/Template_talk:') \
                and not item.get('href').startswith('/wiki/Talk:'):
                    b10 = "https:
                    if len(b2) < 1000 and b10 not in b2:
                        b2.append(b10)
                        b3.append(b10)
                        print(b10)
                        print(len(b2))
                    if len(b2) == 1000:
                        fonk2(b2)
                        return 0
        a1 += 1
def fonk2(urls):
    b11 = r'Task_2_A.txt'
    b12 = open(b11, "w")
    for b10 in urls:
        b12.write(b10 + '\n')
    b12.write('\n' + "Num of Urls: " + str(len(urls)) + '\n')
    b12.close()
def fonk3(arg_url):
    time.sleep(1)
    b7 = requests.get(arg_url).text
    b8 = BeautifulSoup(b7, "html.parser")
    b13 = b8.find('h1', {'id': 'firstHeading'})
    if b13 in b4:
        return 1
    else:
        b4.append(b13)
        return 0
fonk1(b1)