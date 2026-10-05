import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import multiprocessing as mp
from time import sleep
from warnings import warn
b1 = pd.read_excel('eunew1.xlsx')
def fonk1(url):
    a1 = 3
    for attempt in range(a1):
        try:
            b2 = requests.get(url, verify=False)
            b2.raise_for_status()
            break
        except (requests.ConnectionError, requests.HTTPError) as e:
            if attempt < a1 - 1:
                sleep(2)
                continue
            else:
                raise
    b3 = BeautifulSoup(b2.text, 'html.parser')
    b4 = [str(td.text).splitlines() for td in b3.find_all("td", "third", limit=8)]
    return b4
b5 = mp.Pool(mp.cpu_count())
b6 = b1['url'].tolist()
b7 = b5.map(fetch_data, b6)
b5.close()
b5.join()
b8 = pd.DataFrame(np.array(b7), columns=['all'])
b9 = pd.concat([b1, b8], axis=1)
b9.to_excel('results_oct.xlsx', b10 = False)