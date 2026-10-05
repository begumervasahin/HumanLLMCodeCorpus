import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
import re
import time
import multiprocessing as mp
trial_ids = list(range(1, 34000))
urls = [f"http:
df = pd.DataFrame({'number': trial_ids, 'url': urls})
pattern = re.compile(r'\\[nrt]')
def extract_info(url):
    extracted_info = []
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        table = soup.find('table')
        ctri_number = re.findall(r'(?sm)(?<=CTRI Number)[^A-Za-z]*(\w+\W+.*)(?=Last Modified On:)', table.text)
        last_modified = re.findall(r'(?sm)(?<=Last Modified On:)[^A-Za-z]*(\w+\W+.*)(?=Post Graduate Thesis)', table.text)
        post_grad_thesis = re.findall(r'(?sm)(?<=Post Graduate Thesis)[^A-Za-z]*(\w+\W+.*)(?=Type of Trial)', table.text)
        extracted_info.append('%;'.join([str(ctri_number), str(last_modified), str(post_grad_thesis)]))
        time.sleep(2)
    except Exception as e:
        print(f"An error occurred for URL: {url}, Error: {e}")
        extracted_info.append('no_value')
    finally:
        return extracted_info
def process_urls(batch_urls):
    batch_results = []
    for url in batch_urls:
        batch_results.append(extract_info(url))
    return batch_results
if __name__ == "__main__":
    num_processes = mp.cpu_count()
    url_batches = np.array_split(df['url'].tolist(), num_processes)
    with mp.Pool(processes=num_processes) as pool:
        results = pool.map(process_urls, url_batches)
    flat_results = [item for sublist in results for item in sublist]
    df['all'] = flat_results
    df.to_excel('results_29May.xlsx', index=False)