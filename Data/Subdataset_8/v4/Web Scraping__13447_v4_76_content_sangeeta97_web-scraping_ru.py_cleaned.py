import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import numpy as np
import multiprocessing as mp
from time import sleep
from warnings import warn
df1 = pd.read_excel('eunew1.xlsx')
def fetch_data(url):
    tries = 3
    for i in range(tries):
        try:
            response = requests.get(url, verify=False)
            break
        except requests.ConnectionError as e:
            if i < tries - 1:
                sleep(2)
                continue
            else:
                raise
    if response.status_code != 200:
        warn('Request: {}; Status code: {}'.format(requests, response.status_code))
    page_html = BeautifulSoup(response.text, 'html.parser')
    result = [str(td.text).splitlines() for td in page_html.find_all("td", "third", limit=8)]
    return result
pool = mp.Pool(mp.cpu_count())
urls = df1.url.tolist()
results = pool.map(fetch_data, urls)
pool.close()
pool.join()
df2 = pd.DataFrame(np.array(results), columns=['all'])
df2 = df1.merge(df2, how='outer', left_index=True, right_index=True)
df2.to_excel('results_oct.xlsx')