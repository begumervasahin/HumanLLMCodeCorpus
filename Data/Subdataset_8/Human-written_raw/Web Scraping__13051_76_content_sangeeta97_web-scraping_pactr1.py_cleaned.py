import requests
from bs4 import BeautifulSoup
import re
import time
import random
import xlrd
import pandas as pd
import numpy as np
import re
index= list(range(86, 10000, 1))
url= ["https:
d = {'number': index, 'url': url}
df = pd.DataFrame(data=d)
def text1(url):
    aw= []
    try:
        r = requests.get(url, verify = False)
        soup = BeautifulSoup(r.text, 'lxml')
        pt= (page_html1.find_all('table')[2]).find_all('td')[2].get_text()
        p1= (soup.find_all('table')[2]).find_all('td')[9].get_text()
        s1= (page_html1.find_all('table')[2]).find_all('td')[11].get_text()
        n1= [str(td.text) for td in (soup.find_all('table')[4]).find_all('td')]
        time.sleep(2)
        aw.append(pt, p1, s1, str(n1))
    except:
        aw.append('no_value')
    finally:
        return aw
import multiprocessing as mp
from multiprocessing.dummy import Pool as ThreadPool
pool = ThreadPool(mp.cpu_count())
io= df.url.tolist()
results = pool.map(text1, io)
df2 = pd.DataFrame(np.array(results), columns=['all'])
pool.close()
pool.join()
df2= df.merge(df2, how='outer', left_index= True, right_index= True)
df2.to_excel('pac_28sept.xlsx')