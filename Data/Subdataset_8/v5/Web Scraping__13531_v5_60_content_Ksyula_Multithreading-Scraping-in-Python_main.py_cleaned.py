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
    href = link.get('href')
    if href and href != '/' and re.match('^/currencies', href):
        coin = re.search('/currencies/(.+?)/', href)
        if coin:
            coin_name = coin.group(1)
            if coin_name != 'volume' and coin_name not in coins:
                coins.append(coin_name)
proxies = get_proxies()
batch_size = 25
coin_batches = [coins[i:i+batch_size] for i in range(0, len(coins), batch_size)]
threads = []
for coin_batch in coin_batches:
    t = Thread(target=parse_and_write, args=(coin_batch, proxies))
    threads.append(t)
    t.start()
for t in threads:
    t.join()
print("Exiting Main Thread")