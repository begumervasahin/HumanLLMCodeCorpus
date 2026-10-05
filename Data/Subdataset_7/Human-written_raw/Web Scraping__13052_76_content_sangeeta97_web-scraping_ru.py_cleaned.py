from requests import get
from requests import ConnectionError
from bs4 import BeautifulSoup
import re
from time import sleep
from time import time
from random import randint
from IPython.core.display import clear_output
from warnings import warn
import pandas as pd
import random
from requests import ConnectionError
from warnings import warn
b1 = pd.read_excel('eunew1.xlsx')
def fonk1(url):
    a1 = 3
    for i in range(a1):
        try:
            b2 = get(url, verify = False)
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
import multiprocessing as mp
from multiprocessing.dummy import Pool as ThreadPool
b5 = ThreadPool(mp.cpu_count())
b6 = b1.url.tolist()
b7 = b5.map(solve1, b6)
b8 = pd.DataFrame(np.array(b7), columns=['all'])
b5.close()
b5.join()
b8 = b1.merge(b8, how='outer', left_index= True, right_index= True)
b8.to_excel('results_oct.xlsx')