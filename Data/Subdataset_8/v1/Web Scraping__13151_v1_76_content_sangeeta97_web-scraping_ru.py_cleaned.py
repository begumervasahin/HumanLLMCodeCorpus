import pandas as pd
import numpy as np
import multiprocessing as mp
from multiprocessing.dummy import Pool as ThreadPool
from requests.exceptions import ConnectionError
from warnings import warn
from time import sleep
from bs4 import BeautifulSoup
import requests
df1 = pd.read_excel('eunew1.xlsx')
def scrape_url(url):
    tries = 3
    for i in range(tries):
        try:
            response = requests.get(url, verify=False)
            break
        except ConnectionError as e:
            if i < tries - 1:
                sleep(2)
                continue
            else:
                raise
    if response.status_code != 200:
        warn('Request: {}; Status code: {}'.format(requests, response.status_code))
    page_html = BeautifulSoup(response.text, 'html.parser')
    result = [(str(td.text)).splitlines() for td in page_html.find_all("td", "third", limit=8)]
    return result
num_threads = mp.cpu_count()
pool = ThreadPool(num_threads)
urls = df1['url'].tolist()
results = pool.map(scrape_url, urls)
pool.close()
pool.join()
df2 = pd.DataFrame(np.array(results), columns=['all'])
df2 = pd.concat([df1, df2], axis=1)
df2.to_excel('results_oct.xlsx', index=False)