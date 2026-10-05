import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
import re
import time
import multiprocessing as mp
def generate_urls():
    base_url = "http:
    return [base_url.format(trial_id) for trial_id in range(1, 34000)]
def extract_info(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        table = soup.find('table')
        ctri_number = re.findall(r'CTRI Number\s*:\s*(.*?)\s*Last Modified On:', table.text, re.DOTALL)
        last_modified = re.findall(r'Last Modified On\s*:\s*(.*?)\s*Post Graduate Thesis:', table.text, re.DOTALL)
        post_grad_thesis = re.findall(r'Post Graduate Thesis\s*:\s*(.*?)\s*Type of Trial:', table.text, re.DOTALL)
        time.sleep(2)
        return ';'.join([ctri_number[0].strip(), last_modified[0].strip(), post_grad_thesis[0].strip()]) if ctri_number else 'no_value'
    except Exception as e:
        print(f"An error occurred for URL: {url}, Error: {e}")
        return 'no_value'
def process_urls(batch_urls):
    return [extract_info(url) for url in batch_urls]
if __name__ == "__main__":
    urls = generate_urls()
    df = pd.DataFrame({'url': urls})
    num_processes = mp.cpu_count()
    url_batches = np.array_split(df['url'].tolist(), num_processes)
    with mp.Pool(processes=num_processes) as pool:
        results = pool.map(process_urls, url_batches)
    flat_results = [item for sublist in results for item in sublist]
    df['all'] = flat_results
    df.to_excel('results_29May.xlsx', index=False)