import requests
from bs4 import BeautifulSoup
import time
import random
import pandas as pd
from multiprocessing.dummy import Pool as ThreadPool
import multiprocessing as mp
b1 = list(range(86, 10000))
b2 = [f"https:
b3 = pd.DataFrame({'Trial ID': b1, 'URL': b2})
def fonk1(url):
    try:
        b4 = requests.get(url)
        b4.raise_for_status()
        b5 = BeautifulSoup(b4.text, 'lxml')
        b6 = b5.find_all('table')[2].find_all('td')[2].get_text().strip()
        b7 = b5.find_all('table')[2].find_all('td')[9].get_text().strip()
        b8 = b5.find_all('table')[2].find_all('td')[11].get_text().strip()
        b9 = ' '.join(td.text.strip() for td in b5.find_all('table')[4].find_all('td'))
        return b6, b7, b8, b9
    except requests.RequestException as e:
        print(f"Failed to process {url}: {e}")
        return 'no_value', 'no_value', 'no_value', 'no_value'
with ThreadPool(mp.cpu_count()) as pool:
    b10 = pool.map(fetch_trial_data, b3['URL'])
b11 = pd.DataFrame(b10, columns=['Trial Info', 'Primary Outcome', 'Secondary Outcome', 'NCT Number'])
b12 = pd.concat([b3, b11], axis=1)
b12.to_excel('pac_28sept.xlsx', b13 = False)
print("Data collection complete. Results saved to 'pac_28sept.xlsx'.")