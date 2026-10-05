import requests
from bs4 import BeautifulSoup
import time
import pandas as pd
import numpy as np
from multiprocessing.dummy import Pool as ThreadPool
import multiprocessing as mp
b1 = list(range(86, 10000, 1))
b2 = ["https:
b3 = pd.DataFrame({'number': b1, 'url': b2})
def fonk1(url):
    b4 = []
    try:
        b5 = requests.get(url)
        b5.raise_for_status()
        b6 = BeautifulSoup(b5.text, 'lxml')
        b7 = b6.find_all('table')[2].find_all('td')[2].get_text().strip()
        b8 = b6.find_all('table')[2].find_all('td')[9].get_text().strip()
        b9 = b6.find_all('table')[2].find_all('td')[11].get_text().strip()
        b10 = ' '.join(td.text.strip() for td in b6.find_all('table')[4].find_all('td'))
        b4 = [b7, b8, b9, b10]
    except Exception as e:
        print(f"Failed to process {url}: {e}")
        b4 = ['no_value'] * 4
    finally:
        time.sleep(random.uniform(1, 2))
        return b4
with ThreadPool(mp.cpu_count()) as pool:
    b11 = pool.map(fetch_trial_data, b3['url'])
b12 = pd.DataFrame(b11, columns=['Trial Info', 'Primary Outcome', 'Secondary Outcome', 'NCT Number'])
b13 = pd.concat([b3, b12], axis=1)
b13.to_excel('pac_28sept.xlsx', b1 = False)
print("Data collection complete. Results saved to 'pac_28sept.xlsx'.")