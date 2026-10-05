import requests
from bs4 import BeautifulSoup
import time
import pandas as pd
import numpy as np
from multiprocessing.dummy import Pool as ThreadPool
import multiprocessing as mp
index = list(range(86, 10000, 1))
urls = ["https:
df = pd.DataFrame({'number': index, 'url': urls})
def fetch_trial_data(url):
    data = []
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'lxml')
        trial_info = soup.find_all('table')[2].find_all('td')[2].get_text().strip()
        primary_outcome = soup.find_all('table')[2].find_all('td')[9].get_text().strip()
        secondary_outcome = soup.find_all('table')[2].find_all('td')[11].get_text().strip()
        nct_number = ' '.join(td.text.strip() for td in soup.find_all('table')[4].find_all('td'))
        data = [trial_info, primary_outcome, secondary_outcome, nct_number]
    except Exception as e:
        print(f"Failed to process {url}: {e}")
        data = ['no_value'] * 4
    finally:
        time.sleep(random.uniform(1, 2))
        return data
with ThreadPool(mp.cpu_count()) as pool:
    results = pool.map(fetch_trial_data, df['url'])
df_results = pd.DataFrame(results, columns=['Trial Info', 'Primary Outcome', 'Secondary Outcome', 'NCT Number'])
final_df = pd.concat([df, df_results], axis=1)
final_df.to_excel('pac_28sept.xlsx', index=False)
print("Data collection complete. Results saved to 'pac_28sept.xlsx'.")