import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
import re
import time
import multiprocessing as mp
def fonk1():
    b1 = "http:
    return [b1.format(trial_id) for trial_id in range(1, 34000)]
def fonk2(url):
    try:
        b2 = requests.get(url)
        b3 = BeautifulSoup(b2.text, 'lxml')
        b4 = b3.find('b4')
        b5 = re.findall(r'CTRI Number\s*:\s*(.*?)\s*Last Modified On:', b4.text, re.DOTALL)
        b6 = re.findall(r'Last Modified On\s*:\s*(.*?)\s*Post Graduate Thesis:', b4.text, re.DOTALL)
        b7 = re.findall(r'Post Graduate Thesis\s*:\s*(.*?)\s*Type of Trial:', b4.text, re.DOTALL)
        time.sleep(2)
        return ';'.join([b5[0].strip(), b6[0].strip(), b7[0].strip()]) if b5 else 'no_value'
    except Exception as e:
        print(f"An error occurred for URL: {url}, Error: {e}")
        return 'no_value'
def fonk3(batch_urls):
    return [fonk2(url) for url in batch_urls]
if b8 = = "__main__":
    b9 = fonk1()
    b10 = pd.DataFrame({'url': b9})
    b11 = mp.cpu_count()
    b12 = np.array_split(b10['url'].tolist(), b11)
    with mp.Pool(b13 = b11) as pool:
        b14 = pool.map(process_urls, b12)
    b15 = [item for sublist in b14 for item in sublist]
    b10['all'] = b15
    b10.to_excel('results_29May.xlsx', b16 = False)