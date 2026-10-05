import re
import requests
from bs4 import BeautifulSoup
from threading import Thread
from proxy_list import get_proxies
from parse_and_write import parse_and_write
from clean_db import db_cleaner
url = 'https:
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
coins = []
for link in soup.find_all('a'):
    if (link.get('href') != None and link.get('href') != '/' and link.get('href') != '
        if (re.match('^/currencies' , link.get('href'))):
            coin = re.search('/currencies/(.+?)/', link.get('href')).group(1)
            if(coin not in coins and coin != 'volume'):
                coins.append(coin)
proxies = get_proxies()
threads = []
t1 = Thread(target=parse_and_write, args=(coins[0:25], proxies))
t2 = Thread(target=parse_and_write, args=(coins[25:50], proxies))
t3 = Thread(target=parse_and_write, args=(coins[50:75], proxies))
t4 = Thread(target=parse_and_write, args=(coins[75:100], proxies))
t1.start()
t2.start()
t3.start()
t4.start()
t1.join()
t2.join()
t3.join()
t4.join()
threads.append(t1)
threads.append(t2)
threads.append(t3)
threads.append(t4)
for t in threads:
    t.join()
print("Exiting Main Thread")