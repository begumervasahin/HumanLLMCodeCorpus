import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import multiprocessing as mp
from time import sleep
from warnings import warn
df = pd.read_excel('eunew1.xlsx')
def fetch_data(url):
    max_tries = 3
    for attempt in range(max_tries):
        try:
            response = requests.get(url, verify=False)
            response.raise_for_status()
            break
        except (requests.ConnectionError, requests.HTTPError) as e:
            if attempt < max_tries - 1:
                sleep(2)
                continue
            else:
                raise
    page_html = BeautifulSoup(response.text, 'html.parser')
    data = [str(td.text).splitlines() for td in page_html.find_all("td", "third", limit=8)]
    return data
pool = mp.Pool(mp.cpu_count())
urls = df['url'].tolist()
results = pool.map(fetch_data, urls)
pool.close()
pool.join()
df_fetched = pd.DataFrame(np.array(results), columns=['all'])
df_merged = pd.concat([df, df_fetched], axis=1)
df_merged.to_excel('results_oct.xlsx', index=False)