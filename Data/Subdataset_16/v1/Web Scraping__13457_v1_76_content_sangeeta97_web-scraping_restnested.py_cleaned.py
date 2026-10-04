import pandas as pd
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
b7 = pd.DataFrame(b4, columns=['nct_id'])
b8 = pd.DataFrame(b6, columns=['nct_id'])
b7['urllist'] = ["https:
b8['urllist'] = ["https:
def fonk1(url):
    b9 = requests.get(url)
    b10 = BeautifulSoup(b9.text, "html.parser")
    b11 = b10.find_all(href=re.compile("\?V\_"))
    return len(b11)
b7['number'] = b7['urllist'].map(get_number)
b8['number'] = b8['urllist'].map(get_number)
b7['num6'] = b7['number'].map(lambda x: list(range(1, x + 1)))
b8['num6'] = b8['number'].map(lambda x: list(range(1, x + 1)))
b12 = [str(i) + "?V_" + str(j) + "=View" for i, sublist in zip(b7['nct_id'], b7['num6']) for j in sublist]
b13 = pd.DataFrame({'first': b7['nct_id'].repeat(b7['number']), 'second': b12})
b14 = [str(i) + "?V_" + str(j) + "=View" for i, sublist in zip(b8['nct_id'], b8['num6']) for j in sublist]
b15 = pd.DataFrame({'first': b8['nct_id'].repeat(b8['number']), 'second': b14})
def fonk2(url):
    b16 = requests.get(url)
    b10 = BeautifulSoup(b16.content, "html.parser")
    b17 = b10.find_all('div', attrs={"id": "ContactsLocationsBody"})
    for contact in b17:
        b18 = contact.find_all('td')
        b19 = [ele.text.strip() for ele in b18]
        return b19[1] if b19 else None
b13['nurl'] = "https:
b13['History_Contacts'] = b13['nurl'].map(scrape_PI)
b15['nurl'] = "https:
b15['History_Contacts'] = b15['nurl'].map(scrape_PI)
b13.to_csv('S8_07.csv', b20 = False)
b15.to_csv('S11_07.csv', b20 = False)