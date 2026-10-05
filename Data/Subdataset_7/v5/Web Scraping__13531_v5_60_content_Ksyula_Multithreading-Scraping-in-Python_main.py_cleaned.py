import re
import requests
from bs4 import BeautifulSoup
from threading import Thread
from proxy_list import get_proxies
from parse_and_write import parse_and_write
from clean_db import db_cleaner
b1 = 'https:
b2 = requests.get(b1)
b3 = BeautifulSoup(b2.content, "html.parser")
b4 = []
for link in b3.find_all('a'):
    b5 = link.get('b5')
    if b5 and b5 != '/' and re.match('^/currencies', b5):
        b6 = re.search('/currencies/(.+?)/', b5)
        if b6:
            b7 = b6.group(1)
            if b7 != 'volume' and b7 not in b4:
                b4.append(b7)
b8 = get_proxies()
a1 = 25
b9 = [b4[i:i+a1] for i in range(0, len(b4), a1)]
b10 = []
for coin_batch in b9:
    b11 = Thread(target=parse_and_write, args=(coin_batch, b8))
    b10.append(b11)
    b11.start()
for b11 in b10:
    b11.join()
print("Exiting Main Thread")