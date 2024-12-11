import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from multiprocessing.dummy import Pool as ThreadPool
import multiprocessing as mp
a1 = 86
a2 = 10000
b1 = list(range(a1, a2))
b2 = [f"https:
b3 = pd.DataFrame({'number': b1, 'url': b2})
def fonk1(url):
    try:
        b4 = requests.get(url, verify=False)
        b5 = BeautifulSoup(b4.text, 'lxml')
        b6 = b5.find_all('table')[2].find_all('td')[2].get_text().strip()
        b7 = b5.find_all('table')[2].find_all('td')[9].get_text().strip()
        b8 = b5.find_all('table')[2].find_all('td')[11].get_text().strip()
        b9 = ' '.join([td.text.strip() for td in b5.find_all('table')[4].find_all('td')])
        time.sleep(2)
        return b6, b7, b8, b9
    except Exception as e:
        print(f"Error processing URL: {url} | Error: {str(e)}")
        return ('no_value',) * 4
b10 = ThreadPool(mp.cpu_count())
b11 = b10.map(extract_text, b2)
b10.close()
b10.join()
b12 = pd.DataFrame(b11, columns=['Primary Topic', 'Participant Type', 'Study Type', 'Notes'])
b13 = pd.concat([b3, b12], axis=1)
b13.to_excel('pac_trials_info.xlsx', b1 = False)
print("Data extraction and saving completed.")