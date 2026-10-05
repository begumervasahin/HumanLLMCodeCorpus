import pandas as pd
import numpy as np
import multiprocessing as mp
from multiprocessing.dummy import Pool as ThreadPool
from requests.exceptions import ConnectionError
from warnings import warn
from time import sleep
from bs4 import BeautifulSoup
import requests
b1 = pd.read_excel('eunew1.xlsx')
def fonk1(url):
    a1 = 3
    for i in range(a1):
        try:
            b2 = requests.get(url, verify=False)
            break
        except ConnectionError as e:
            if i < a1 - 1:
                sleep(2)
                continue
            else:
                raise
    if b2.status_code != 200:
        warn('Request: {}; Status code: {}'.format(requests, b2.status_code))
    b3 = BeautifulSoup(b2.text, 'html.parser')
    b4 = [(str(td.text)).splitlines() for td in b3.find_all("td", "third", limit=8)]
    return b4
b5 = mp.cpu_count()
b6 = ThreadPool(b5)
b7 = b1['url'].tolist()
b8 = b6.map(scrape_url, b7)
b6.close()
b6.join()
b9 = pd.DataFrame(np.array(b8), columns=['all'])
b9 = pd.concat([b1, b9], axis=1)
b9.to_excel('results_oct.xlsx', b10 = False)