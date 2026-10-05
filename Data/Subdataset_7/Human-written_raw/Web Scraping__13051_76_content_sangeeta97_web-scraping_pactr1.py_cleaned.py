import requests
from bs4 import BeautifulSoup
import re
import time
import random
import xlrd
import pandas as pd
import numpy as np
import re
b1 = list(range(86, 10000, 1))
b2 = ["https:
b3 = {'number': b1, 'b2': b2}
b4 = pd.DataFrame(data=b3)
def fonk1(b2):
    b5 = []
    try:
        b6 = requests.get(b2, verify = False)
        b7 = BeautifulSoup(b6.text, 'lxml')
        b8 = (page_html1.find_all('table')[2]).find_all('td')[2].get_text()
        b9 = (b7.find_all('table')[2]).find_all('td')[9].get_text()
        b10 = (page_html1.find_all('table')[2]).find_all('td')[11].get_text()
        b11 = [str(td.text) for td in (b7.find_all('table')[4]).find_all('td')]
        time.sleep(2)
        b5.append(b8, b9, b10, str(b11))
    except:
        b5.append('no_value')
    finally:
        return b5
import multiprocessing as mp
from multiprocessing.dummy import Pool as ThreadPool
b12 = ThreadPool(mp.cpu_count())
b13 = b4.b2.tolist()
b14 = b12.map(text1, b13)
b15 = pd.DataFrame(np.array(b14), columns=['all'])
b12.close()
b12.join()
b15 = b4.merge(b15, how='outer', left_index= True, right_index= True)
b15.to_excel('pac_28sept.xlsx')