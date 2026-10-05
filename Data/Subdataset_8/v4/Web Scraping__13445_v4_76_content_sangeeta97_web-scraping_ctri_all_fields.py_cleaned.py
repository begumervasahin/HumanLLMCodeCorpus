import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
import re
import time
import random
import multiprocessing as mp
from multiprocessing.dummy import Pool as ThreadPool
index = list(range(1, 34000, 1))
url = [f"http:
data = {'number': index, 'url': url}
df = pd.DataFrame(data)
lk = re.compile(r'\\[nrt]')
def extract_text(url):
    text_list = []
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        table = soup.find('table')
        aa = re.findall(r'(?sm)(?<=CTRI Number)[^A-Za-z]*(\w+\W+.*)(?=Last Modified On:)', table.text)
        aa = lk.sub(' ', str(aa))
        text_list.append('%;'.join([str(aa), str(bb), str(cc), str(dd), str(ee), str(ff), str(gg), str(hh), str(ii), str(jj),
                                    str(kk), str(ll), str(mm), str(nn), str(oo), str(pp), str(qq), str(rr), str(ss), str(tt),
                                    str(uu), str(vv), str(ww), str(xx), str(yy), str(zz), str(ab), str(ac), str(ad), str(ae),
                                    str(af), str(ag), str(ah), str(ai), str(aj), str(ak), str(al)]))
        time.sleep(2)
    except:
        text_list.append('no_value')
    finally:
        return text_list
pool = ThreadPool(mp.cpu_count())
io = df.url.tolist()
results = pool.map(extract_text, io)
pool.close()
pool.join()
df2 = pd.DataFrame(np.array(results), columns=['all'])
df2 = df.merge(df2, how='outer', left_index=True, right_index=True)
df2.to_excel('results_29May.xlsx')