
import re
import requests
from bs4 import BeautifulSoup
from threading import Thread
from proxy_list import get_proxies
from parse_and_write import parse_and_write
from clean_db import db_cleaner
def fonk1(b5):
    b1 = requests.get(b5)
    b2 = BeautifulSoup(b1.content, "html.parser")
    b3 = []
    for link in b2.find_all('a'):
        if (link.get('href') != None and link.get('href') != '/' and link.get('href') != ''):
            if (re.match('^/currencies' , link.get('href'))):
                b4 = re.search('/currencies/(.+?)/', link.get('href')).group(1)
                if(b4 not in b3 and b4 != 'volume'):
                    b3.append(b4)
    return b3
def fonk2():
    b5 = 'https:
    b3 = fonk1(b5)
    b6 = get_proxies()
    a1 = 4
    b7 = len(b3)
    b8 = []
    for i in range(a1):
        b9 = i * b7
        b10 = (i + 1) * b7 if i < a1 - 1 else len(b3)
        b11 = Thread(target=parse_and_write, args=(b3[b9:b10], b6))
        b11.start()
        b8.append(b11)
    for b11 in b8:
        b11.join()
    print("Exiting Main Thread")
if b12 = = "__main__":
    fonk2()