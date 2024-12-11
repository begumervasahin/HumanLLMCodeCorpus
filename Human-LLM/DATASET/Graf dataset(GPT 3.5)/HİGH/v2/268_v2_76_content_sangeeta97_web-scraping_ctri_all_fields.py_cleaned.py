import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
import re
import time
import multiprocessing as mp
b1 = list(range(1, 34000))
b2 = [f"http:
b3 = pd.DataFrame({'number': b1, 'url': b2})
b4 = re.compile(r'\\[nrt]')
def fonk1(url):
    b5 = []
    try:
        b6 = requests.get(url)
        b7 = BeautifulSoup(b6.text, 'lxml')
        b8 = b7.find('b8')
        b9 = re.findall(r'(?sm)(?<=CTRI Number)[^A-Za-z]*(\w+\W+.*)(?=Last Modified On:)', b8.text)
        b10 = re.findall(r'(?sm)(?<=Last Modified On:)[^A-Za-z]*(\w+\W+.*)(?=Post Graduate Thesis)', b8.text)
        b11 = re.findall(r'(?sm)(?<=Post Graduate Thesis)[^A-Za-z]*(\w+\W+.*)(?=Type of Trial)', b8.text)
        b5.append('%;'.join([str(b9), str(b10), str(b11)]))
        time.sleep(2)
    except Exception as e:
        print(f"An error occurred for URL: {url}, Error: {e}")
        b5.append('no_value')
    finally:
        return b5
def fonk2(batch_urls):
    b12 = []
    for url in batch_urls:
        b12.append(fonk1(url))
    return b12
if b13 = = "__main__":
    b14 = mp.cpu_count()
    b15 = np.array_split(b3['url'].tolist(), b14)
    with mp.Pool(b16 = b14) as pool:
        b17 = pool.map(process_urls, b15)
    b18 = [item for sublist in b17 for item in sublist]
    b3['all'] = b18
    b3.to_excel('results_29May.xlsx', b19 = False)