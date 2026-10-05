import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
import re
import time
import multiprocessing as mp
index = list(range(1, 34000, 1))
url = ["http:
d = {'number': index, 'url': url}
df = pd.DataFrame(data=d)
lk = re.compile(r'\\[nrt]')
def text1(url):
    aw = []
    try:
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'lxml')
        table = soup.find('table')
        aa = re.findall(r'(?sm)(?<=CTRI Number)[^A-Za-z]*(\w+\W+.*)(?=Last Modified On:)', table.text)
        aa = lk.sub(' ', str(aa))
        bb = re.findall(r'(?sm)(?<=Last Modified On:)[^A-Za-z]*(\w+\W+.*)(?=Post Graduate Thesis)', table.text)
        bb = lk.sub(' ', str(bb))
        cc = re.findall(r'(?sm)(?<=Post Graduate Thesis)[^A-Za-z]*(\w+\W+.*)(?=Type of Trial)', table.text)
        cc = lk.sub(' ', str(cc))
        aw.append('%;'.join([str(aa), str(bb), str(cc)]))
        time.sleep(2)
    except Exception as e:
        print(f"An error occurred for URL: {url}, Error: {e}")
        aw.append('no_value')
    finally:
        return aw
def process_urls(urls):
    results = []
    for url in urls:
        results.append(text1(url))
    return results
if __name__ == "__main__":
    num_processes = mp.cpu_count()
    urls_split = np.array_split(df['url'].tolist(), num_processes)
    pool = mp.Pool(processes=num_processes)
    results = pool.map(process_urls, urls_split)
    pool.close()
    pool.join()
    flat_results = [item for sublist in results for item in sublist]
    df['all'] = flat_results
    df.to_excel('results_29May.xlsx', index=False)