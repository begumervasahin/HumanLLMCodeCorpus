import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
from random import sample
import re
b1 = pd.read_csv('S8nested6feb.csv')
b2 = pd.read_csv('sk_S116feb19.csv')
b3 = sample(list(b1.nct_id.values), 211)
b4 = sample(list(b2.nct_id.values), 422)
b5 = pd.DataFrame(b3, b12=['nct_id'])
b6 = pd.DataFrame(b4, b12=['nct_id'])
b5['urllist'] = b5['nct_id'].apply(lambda x: f"https:
b6['urllist'] = b6['nct_id'].apply(lambda x: f"https:
def fonk1(url):
    b7 = requests.get(url)
    b8 = BeautifulSoup(b7.text, "html.parser")
    b9 = b8.find_all(href=re.compile(b7"\?V\_"))
    return len(b9)
b5['number'] = b5['urllist'].map(get_number)
b5['num6'] = b5['number'].map(lambda x: list(range(1, x+1)))
b10 = list(b5.nct_id * b5.number)
b11 = pd.DataFrame(b10, b5.num6).reset_index()
b11.b12 = ['first', 'second']
b11['second'] = b11['second'].map(lambda x: ",".join([x[i:i+11] for i in range(0, len(x), 11)]))
b11['second'] = b11['second'].str.split(',')
b13 = b11.stack().apply(pd.Series).stack().unstack(1)
b13['ff'] = list(zip(b13['first'].astype(str), b13['second'].astype(str)))
b13['nurl'] = b13['ff'].apply(lambda x: f"https:
def fonk2(url):
    b14 = requests.get(url)
    b8 = BeautifulSoup(b14.content, "html.parser")
    b15 = b8.findAll('div', attrs={"id":"ContactsLocationsBody"})
    if b15:
        b16 = [ele.text.strip() for th in b15 for ele in th.find_all('td')]
        return b16[1] if b16 else None
    return None
b13['History_Contacts'] = b13['nurl'].map(scrape_PI)
b13.to_csv('S8_07.csv', b17 = False)
b6['number'] = b6['urllist'].map(get_number)
b6['num6'] = b6['number'].map(lambda x: list(range(1, x+1)))
b18 = list(b6.nct_id * b6.number)
b19 = pd.DataFrame(b18, b6.num6).reset_index()
b19.b12 = ['first', 'second']
b19['second'] = b19['second'].map(lambda x: ",".join([x[i:i+11] for i in range(0, len(x), 11)]))
b19['second'] = b19['second'].str.split(',')
b20 = b19.stack().apply(pd.Series).stack().unstack(1)
b20['ff'] = list(zip(b20['first'].astype(str), b20['second'].astype(str)))
b20['nurl'] = b20['ff'].apply(lambda x: f"https:
b20['History_Contacts'] = b20['nurl'].map(scrape_PI)
b20.to_csv('S11_07.csv', b17 = False)