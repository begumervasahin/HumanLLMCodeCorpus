import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
import random
from random import sample
import re
b1 = pd.read_csv('S8nested6feb.csv')
b2 = pd.read_csv('sk_S116feb19.csv')
b3 = list(b1.nct_id.values)
b4 = sample(b3, 211)
b5 = list(b2.nct_id.values)
b6 = sample(b5, 422)
b7 = pd.DataFrame(b4)
b7.b8 = ['nct_id']
b9 = pd.DataFrame(b6)
b9.b8 = ['nct_id']
b7['urllist']= ["https:
b9['urllist']= ["https:
def fonk1(url):
    b10 = requests.get(url)
    b11 = BeautifulSoup(b10.text, "html.parser")
    b12 = b11.find_all(href=re.compile("\?V\_"))
    return len(b12)
b7['number']= b7.urllist.map(get_number)
b7['num6']= b7.number.map(lambda x: list(range(1, x+1)))
b13 = list(b7.nct_id*b7.number)
b14 = pd.DataFrame(b13, b7.num6)
b14.reset_index(b15 = True)
b14.b8 = ['first', 'second']
b14['second']= b14.second.map(lambda x: ",".join([x[i:i+11] for i in range(0, len(x), 11)]))
b14['second']= b14.second.str.split(',')
b16 = b14.stack().apply(pd.Series).stack().unstack(1)
b16['ff']= list(zip(b16['first'].astype(str), b16['second'].astype(str)))
b16['nurl']= ["https:
def fonk2(url):
    b17 = requests.get(url)
    b11 = BeautifulSoup(b17.content, "html.parser")
    b18 = b11.findAll('div',attrs={"id":"ContactsLocationsBody"})
    b19 = b11.b19
    b20 = []
    for th in b18:
        b20.extend(th.find_all('td'))
        b20 = [ele.text.strip() for ele in b20]
        return b20[1]
b16['History_Contacts']= b16.nurl.astype(str).map(lambda x: fonk2(x))
b16.to_csv('S8_07.csv')
b9['number']= b9.urllist.map(get_number)
b9['num6']= b9.number.map(lambda x: list(range(1, x+1)))
b21 = list(b9.nct_id*b9.number)
b22 = pd.DataFrame(b21, b9.num6)
b22.reset_index(b15 = True)
b22.b8 = ['first', 'second']
b22['second']= b22.second.map(lambda x: ",".join([x[i:i+11] for i in range(0, len(x), 11)]))
b22['second']= b22.second.str.split(',')
b23 = b22.stack().apply(pd.Series).stack().unstack(1)
b23['ff']= list(zip(b23['first'].astype(str), b23['second'].astype(str)))
b23['nurl']= ["https:
b23['History_Contacts']= b23.nurl.astype(str).map(lambda x: fonk2(x))
b23.to_csv('S11_07.csv')