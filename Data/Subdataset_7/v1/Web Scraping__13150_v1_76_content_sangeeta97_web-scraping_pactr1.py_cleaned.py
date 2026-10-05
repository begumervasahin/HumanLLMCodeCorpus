import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import multiprocessing as mp
from multiprocessing.dummy import Pool as ThreadPool
import time
b1 = list(range(86, 10000, 1))
b2 = ["https:
b3 = pd.DataFrame({'number': b1, 'url': b2})
def fonk1(url):
    try:
        b4 = requests.get(url, verify=False)
        b5 = BeautifulSoup(b4.text, 'lxml')
        b6 = (b5.find_all('table')[2]).find_all('td')[2].get_text()
        b7 = (b5.find_all('table')[2]).find_all('td')[9].get_text()
        b8 = (b5.find_all('table')[2]).find_all('td')[11].get_text()
        b9 = [str(td.text) for td in (b5.find_all('table')[4]).find_all('td')]
        time.sleep(2)
        return b6, b7, b8, str(b9)
    except Exception as e:
        print("Error processing URL:", url)
        print(e)
        return 'no_value'
b10 = ThreadPool(mp.cpu_count())
b11 = b10.map(extract_text, b2)
b10.close()
b10.join()
b12 = pd.DataFrame(b11, columns=['b6', 'b7', 'b8', 'b9'])
b13 = pd.concat([b3, b12], axis=1)
b13.to_excel('pac_28sept.xlsx', b1 = False)