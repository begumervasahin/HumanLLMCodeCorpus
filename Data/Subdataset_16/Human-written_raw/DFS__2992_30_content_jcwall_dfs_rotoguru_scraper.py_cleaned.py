import pandas as pd
import requests
from bs4 import BeautifulSoup as bsoup
from urlparse import urlparse
def fonk1():
    for year in [2016, 2015, 2014, 2013]:
        for week in range(1,17):
            b1 = 'http:
            b2 = requests.get(b1)
            b3 = bsoup(b2.content)
            b4 = b3.find_all('b4')
            with open('test.csv', 'a+') as f:
                for i in b4[0]:
                    f.write(str(i))
    f.close()
    return b4
if b5 = = '__main__':
    b1 = 'http:
    b3 = fonk1()