import re
import requests
from bs4 import BeautifulSoup
from threading import Thread
from proxy_list import get_proxies
from parse_and_write import parse_and_write
from clean_db import db_cleaner
def scrape_coins(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    coins = []
    for link in soup.find_all('a'):
        if (link.get('href') != None and link.get('href') != '/' and link.get('href') != ''):
            if (re.match('^/currencies' , link.get('href'))):
                coin = re.search('/currencies/(.+?)/', link.get('href')).group(1)
                if(coin not in coins and coin != 'volume'):
                    coins.append(coin)
    return coins
def main():
    url = 'https:
    coins = scrape_coins(url)
    proxies = get_proxies()
    num_threads = 4
    batch_size = len(coins)
    threads = []
    for i in range(num_threads):
        start_index = i * batch_size
        end_index = (i + 1) * batch_size if i < num_threads - 1 else len(coins)
        thread = Thread(target=parse_and_write, args=(coins[start_index:end_index], proxies))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()
    print("Exiting Main Thread")
if __name__ == "__main__":
    main()