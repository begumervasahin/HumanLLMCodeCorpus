import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import numpy as np
import multiprocessing as mp
from time import sleep
from warnings import warn
b1 = pd.read_excel('eunew1.xlsx')
def fonk1(url):
    a1 = 3
    for i in range(a1):
        try:
            b2 = requests.get(url, verify=False)
            break
        except requests.ConnectionError as e:
            if i < a1 - 1:
                sleep(2)
                continue
            else:
                raise
    if b2.status_code != 200:
        warn('Request: {}; Status code: {}'.format(requests, b2.status_code))
    b3 = BeautifulSoup(b2.text, 'html.parser')
    b4 = [str(td.text).splitlines() for td in b3.find_all("td", "third", limit=8)]
    return b4
b5 = mp.Pool(mp.cpu_count())
b6 = b1.url.tolist()
b7 = b5.map(fetch_data, b6)
b5.close()
b5.join()
b8 = pd.DataFrame(np.array(b7), columns=['all'])
b8 = b1.merge(b8, how='outer', left_index=True, right_index=True)
b8.to_excel('results_oct.xlsx')