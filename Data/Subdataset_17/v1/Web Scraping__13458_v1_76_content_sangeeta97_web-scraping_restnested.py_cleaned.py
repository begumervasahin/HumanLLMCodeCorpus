import pandas as pd
import requests
from bs4 import BeautifulSoup
import random
from random import sample
import re
df2 = pd.read_csv('S8nested6feb.csv')
df1 = pd.read_csv('sk_S116feb19.csv')
s8 = list(df2.nct_id.values)
s8random = sample(s8, 211)
s11 = list(df1.nct_id.values)
s11random = sample(s11, 422)
total8 = pd.DataFrame(s8random, columns=['nct_id'])
total11 = pd.DataFrame(s11random, columns=['nct_id'])
total8['urllist'] = ["https:
total11['urllist'] = ["https:
def get_number(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    nl = soup.find_all(href=re.compile("\?V\_"))
    return len(nl)
total8['number'] = total8['urllist'].map(get_number)
total11['number'] = total11['urllist'].map(get_number)
total8['num6'] = total8['number'].map(lambda x: list(range(1, x + 1)))
total11['num6'] = total11['number'].map(lambda x: list(range(1, x + 1)))
nw = [str(i) + "?V_" + str(j) + "=View" for i, sublist in zip(total8['nct_id'], total8['num6']) for j in sublist]
gg = pd.DataFrame({'first': total8['nct_id'].repeat(total8['number']), 'second': nw})
nw11 = [str(i) + "?V_" + str(j) + "=View" for i, sublist in zip(total11['nct_id'], total11['num6']) for j in sublist]
g11 = pd.DataFrame({'first': total11['nct_id'].repeat(total11['number']), 'second': nw11})
def scrape_PI(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    contacts = soup.find_all('div', attrs={"id": "ContactsLocationsBody"})
    for contact in contacts:
        td_elements = contact.find_all('td')
        result = [ele.text.strip() for ele in td_elements]
        return result[1] if result else None
gg['nurl'] = "https:
gg['History_Contacts'] = gg['nurl'].map(scrape_PI)
g11['nurl'] = "https:
g11['History_Contacts'] = g11['nurl'].map(scrape_PI)
gg.to_csv('S8_07.csv', index=False)
g11.to_csv('S11_07.csv', index=False)