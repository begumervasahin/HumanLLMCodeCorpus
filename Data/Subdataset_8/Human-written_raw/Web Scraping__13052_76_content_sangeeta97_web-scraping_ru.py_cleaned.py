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
df1= pd.read_excel('eunew1.xlsx')
def solve1(url):
    tries=3
    for i in range(tries):
        try:
            response = get(url, verify = False)
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
    result= [(str(td.text)).splitlines() for td in page_html.find_all("td", "third", limit=8)]
    return result
import multiprocessing as mp
from multiprocessing.dummy import Pool as ThreadPool
pool = ThreadPool(mp.cpu_count())
io= df1.url.tolist()
results = pool.map(solve1, io)
df2 = pd.DataFrame(np.array(results), columns=['all'])
pool.close()
pool.join()
df2= df1.merge(df2, how='outer', left_index= True, right_index= True)
df2.to_excel('results_oct.xlsx')