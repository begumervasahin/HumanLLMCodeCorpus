import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import multiprocessing as mp
from multiprocessing.dummy import Pool as ThreadPool
import time
index = list(range(86, 10000, 1))
urls = ["https:
df = pd.DataFrame({'number': index, 'url': urls})
def extract_text(url):
    try:
        r = requests.get(url, verify=False)
        soup = BeautifulSoup(r.text, 'lxml')
        pt = (soup.find_all('table')[2]).find_all('td')[2].get_text()
        p1 = (soup.find_all('table')[2]).find_all('td')[9].get_text()
        s1 = (soup.find_all('table')[2]).find_all('td')[11].get_text()
        n1 = [str(td.text) for td in (soup.find_all('table')[4]).find_all('td')]
        time.sleep(2)
        return pt, p1, s1, str(n1)
    except Exception as e:
        print("Error processing URL:", url)
        print(e)
        return 'no_value'
pool = ThreadPool(mp.cpu_count())
results = pool.map(extract_text, urls)
pool.close()
pool.join()
df2 = pd.DataFrame(results, columns=['pt', 'p1', 's1', 'n1'])
df_final = pd.concat([df, df2], axis=1)
df_final.to_excel('pac_28sept.xlsx', index=False)