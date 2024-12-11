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
    for attempt in range(a1):
        try:
            b2 = requests.get(url, verify=False)
            b2.raise_for_status()
            break
        except ConnectionError:
            if attempt < a1 - 1:
                sleep(2)
            else:
                raise
    b3 = BeautifulSoup(b2.text, 'html.parser')
    b4 = [td.text.strip().splitlines() for td in b3.find_all("td", "third", limit=8)]
    return b4
b5 = mp.cpu_count()
b6 = ThreadPool(b5)
b7 = b1['url'].tolist()
b8 = b6.map(scrape_url, b7)
b6.close()
b6.join()
b9 = pd.DataFrame(np.array(b8), columns=['all'])
b10 = pd.concat([b1, b9], axis=1)
b10.to_excel('results_oct.xlsx', b11 = False)