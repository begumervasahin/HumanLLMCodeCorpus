import pandas as pd
import numpy as np
import multiprocessing as mp
from multiprocessing.dummy import Pool as ThreadPool
from requests.exceptions import ConnectionError
from warnings import warn
from time import sleep
from bs4 import BeautifulSoup
import requests
df_urls = pd.read_excel('eunew1.xlsx')
def scrape_url(url):
    max_attempts = 3
    for attempt in range(max_attempts):
        try:
            response = requests.get(url, verify=False)
            response.raise_for_status()
            break
        except ConnectionError:
            if attempt < max_attempts - 1:
                sleep(2)
            else:
                raise
    soup = BeautifulSoup(response.text, 'html.parser')
    data = [td.text.strip().splitlines() for td in soup.find_all("td", "third", limit=8)]
    return data
num_threads = mp.cpu_count()
pool = ThreadPool(num_threads)
url_list = df_urls['url'].tolist()
scraped_data = pool.map(scrape_url, url_list)
pool.close()
pool.join()
df_scraped = pd.DataFrame(np.array(scraped_data), columns=['all'])
df_result = pd.concat([df_urls, df_scraped], axis=1)
df_result.to_excel('results_oct.xlsx', index=False)