import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
import re
import time
import random
import multiprocessing as mp
from multiprocessing.dummy import Pool as ThreadPool
b1 = list(range(1, 34000, 1))
b2 = [f"http:
b3 = {'number': b1, 'b2': b2}
b4 = pd.DataFrame(b3)
b5 = re.compile(r'\\[nrt]')
def fonk1(b2):
    b6 = []
    try:
        b7 = requests.get(b2)
        b8 = BeautifulSoup(b7.text, 'lxml')
        b9 = b8.find('b9')
        b10 = re.findall(r'(?sm)(?<=CTRI Number)[^A-Za-z]*(\w+\W+.*)(?=Last Modified On:)', b9.text)
        b10 = b5.sub(' ', str(b10))
        b6.append('%;'.join([str(b10), str(bb), str(cc), str(dd), str(ee), str(ff), str(gg), str(hh), str(ii), str(jj),
                                    str(kk), str(ll), str(mm), str(nn), str(oo), str(pp), str(qq), str(rr), str(ss), str(tt),
                                    str(uu), str(vv), str(ww), str(xx), str(yy), str(zz), str(ab), str(ac), str(ad), str(ae),
                                    str(af), str(ag), str(ah), str(ai), str(aj), str(ak), str(al)]))
        time.sleep(2)
    except:
        b6.append('no_value')
    finally:
        return b6
b11 = ThreadPool(mp.cpu_count())
b12 = b4.b2.tolist()
b13 = b11.map(extract_text, b12)
b11.close()
b11.join()
b14 = pd.DataFrame(np.array(b13), columns=['all'])
b14 = b4.merge(b14, how='outer', left_index=True, right_index=True)
b14.to_excel('results_29May.xlsx')