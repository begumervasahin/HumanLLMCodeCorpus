import re
import requests
from bs4 import BeautifulSoup
from threading import Thread
from proxy_list import get_proxies
from parse_and_write import parse_and_write
from clean_db import db_cleaner
def fonk1(b7):
    b1 = requests.get(b7)
    b2 = BeautifulSoup(b1.content, "html.parser")
    b3 = []
    for link in b2.find_all('a'):
        b4 = link.get('b4')
        if b4 and b4 != '/' and re.match('^/currencies', b4):
            b5 = re.search('/currencies/(.+?)/', b4)
            if b5:
                b6 = b5.group(1)
                if b6 != 'volume' and b6 not in b3:
                    b3.append(b6)
    return b3
def fonk2():
    b7 = 'https:
    b3 = fonk1(b7)
    b8 = get_proxies()
    a1 = 4
    b9 = len(b3)
    b10 = []
    for i in range(a1):
        b11 = i * b9
        b12 = (i + 1) * b9 if i < a1 - 1 else len(b3)
        b13 = Thread(target=parse_and_write, args=(b3[b11:b12], b8))
        b13.start()
        b10.append(b13)
    for b13 in b10:
        b13.join()
    print("Exiting Main Thread")
if b14 = = "__main__":
    fonk2()