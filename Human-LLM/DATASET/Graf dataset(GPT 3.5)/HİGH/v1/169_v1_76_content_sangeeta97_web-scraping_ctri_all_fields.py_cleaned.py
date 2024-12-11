import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
import re
import time
import multiprocessing as mp
b1 = list(range(1, 34000, 1))
b2 = ["http:
b3 = {'number': b1, 'b2': b2}
b4 = pd.DataFrame(data=b3)
b5 = re.compile(b7'\\[nrt]')
def fonk1(b2):
    b6 = []
    try:
        b7 = requests.get(b2)
        b8 = BeautifulSoup(b7.text, 'lxml')
        b9 = b8.find('b9')
        b10 = re.findall(b7'(?sm)(?<=CTRI Number)[^A-Za-z]*(\w+\W+.*)(?=Last Modified On:)', b9.text)
        b10 = b5.sub(' ', str(b10))
        b11 = re.findall(b7'(?sm)(?<=Last Modified On:)[^A-Za-z]*(\w+\W+.*)(?=Post Graduate Thesis)', b9.text)
        b11 = b5.sub(' ', str(b11))
        b12 = re.findall(b7'(?sm)(?<=Post Graduate Thesis)[^A-Za-z]*(\w+\W+.*)(?=Type of Trial)', b9.text)
        b12 = b5.sub(' ', str(b12))
        b6.append('%;'.join([str(b10), str(b11), str(b12)]))
        time.sleep(2)
    except Exception as e:
        print(f"An error occurred for URL: {b2}, Error: {e}")
        b6.append('no_value')
    finally:
        return b6
def fonk2(urls):
    b13 = []
    for b2 in urls:
        b13.append(fonk1(b2))
    return b13
if b14 = = "__main__":
    b15 = mp.cpu_count()
    b16 = np.array_split(b4['b2'].tolist(), b15)
    b17 = mp.Pool(processes=b15)
    b13 = b17.map(process_urls, b16)
    b17.close()
    b17.join()
    b18 = [item for sublist in b13 for item in sublist]
    b4['all'] = b18
    b4.to_excel('results_29May.xlsx', b1 = False)