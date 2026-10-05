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
    if (link.get('href') is not None and link.get('href') != '/' and link.get('href') != ''):
        if (re.match('^/currencies' , link.get('href'))):
            b5 = re.search('/currencies/(.+?)/', link.get('href')).group(1)
            if(b5 not in b4 and b5 != 'volume'):
                b4.append(b5)
b6 = get_proxies()
b7 = []
b8 = Thread(target=parse_and_write, args=(b4[0:25], b6))
b9 = Thread(target=parse_and_write, args=(b4[25:50], b6))
b10 = Thread(target=parse_and_write, args=(b4[50:75], b6))
b11 = Thread(target=parse_and_write, args=(b4[75:100], b6))
b8.start()
b9.start()
b10.start()
b11.start()
b8.join()
b9.join()
b10.join()
b11.join()
b7.append(b8)
b7.append(b9)
b7.append(b10)
b7.append(b11)
for t in b7:
    t.join()
print("Exiting Main Thread")