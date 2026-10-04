import pandas as pd
import requests
from bs4 import BeautifulSoup
from random import sample
import re
b1 = pd.read_csv('S8nested6feb.csv')
b2 = pd.read_csv('sk_S116feb19.csv')
b3 = sample(b1['nct_id'].tolist(), 211)
b4 = sample(b2['nct_id'].tolist(), 422)
b5 = pd.DataFrame(b3, b12=['nct_id'])
b6 = pd.DataFrame(b4, b12=['nct_id'])
b5['urllist'] = b5['nct_id'].apply(lambda x: f"https:
b6['urllist'] = b6['nct_id'].apply(lambda x: f"https:
def fonk1(url):
    b7 = requests.get(url)
    b8 = BeautifulSoup(b7.text, "html.parser")
    b9 = b8.find_all(href=re.compile(r"\?V\_"))
    return len(b9)
b5['number'] = b5['urllist'].map(get_number)
b5['num6'] = b5['number'].map(lambda x: list(range(1, x+1)))
b10 = list(b5['nct_id'] * b5['number'])
b11 = pd.DataFrame(b10, b5['num6']).reset_index()
b11.b12 = ['version', 'nct_id']
b11['nct_id'] = b11['nct_id'].str.split(',')
def fonk2(b13):
    b13 = b13.stack().apply(pd.Series).stack().unstack(1)
    b13['ff'] = list(zip(b13['version'].astype(str), b13['nct_id'].astype(str)))
    b13['nurl'] = b13['ff'].apply(lambda x: f"https:
    return b13
b11 = fonk2(b11)
def fonk3(url):
    b7 = requests.get(url)
    b8 = BeautifulSoup(b7.content, "html.parser")
    b14 = b8.find('div', id="ContactsLocationsBody")
    if b14:
        b15 = [td.text.strip() for td in b14.find_all('td')]
        return b15[1] if b15 else None
    return None
b11['History_Contacts'] = b11['nurl'].map(scrape_PI)
b11.to_csv('S8_07.csv', b16 = False)
b6['number'] = b6['urllist'].map(get_number)
b6['num6'] = b6['number'].map(lambda x: list(range(1, x+1)))
b17 = list(b6['nct_id'] * b6['number'])
b18 = pd.DataFrame(b17, b6['num6']).reset_index()
b18.b12 = ['version', 'nct_id']
b18['nct_id'] = b18['nct_id'].str.split(',')
b18 = fonk2(b18)
b18['History_Contacts'] = b18['nurl'].map(scrape_PI)
b18.to_csv('S11_07.csv', b16 = False)