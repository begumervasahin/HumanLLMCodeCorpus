import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from multiprocessing.dummy import Pool as ThreadPool
import multiprocessing as mp
a1 = 86
a2 = 10000
b1 = "https:
def fonk1(url):
    try:
        b2 = requests.get(url, verify=False)
        b3 = BeautifulSoup(b2.text, 'lxml')
        b4 = b3.find_all('table')[2].find_all('td')[2].get_text().strip()
        b5 = b3.find_all('table')[2].find_all('td')[9].get_text().strip()
        b6 = b3.find_all('table')[2].find_all('td')[11].get_text().strip()
        b7 = ' '.join(td.text.strip() for td in b3.find_all('table')[4].find_all('td'))
        time.sleep(2)
        return b4, b5, b6, b7
    except Exception as e:
        print(f"Error processing URL: {url} | Error: {e}")
        return 'no_value', 'no_value', 'no_value', 'no_value'
b8 = [b1.format(trial_id) for trial_id in range(a1, a2)]
with ThreadPool(mp.cpu_count()) as pool:
    b9 = pool.map(extract_trial_data, b8)
b10 = pd.DataFrame(b9, columns=['Primary Topic', 'Participant Type', 'Study Type', 'Notes'])
b11 = pd.DataFrame({'Number': range(a1, a2), 'URL': b8})
b12 = pd.concat([b11, b10], axis=1)
b12.to_excel('pac_trials_info.xlsx', b13 = False)
print("Data extraction and saving completed.")