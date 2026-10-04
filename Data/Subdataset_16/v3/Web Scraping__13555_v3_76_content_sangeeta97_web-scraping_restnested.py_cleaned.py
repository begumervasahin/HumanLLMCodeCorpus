import pandas as pd
import requests
from bs4 import BeautifulSoup
from random import sample
import re
b1 = pd.read_csv('S8nested6feb.csv')
b2 = pd.read_csv('sk_S116feb19.csv')
def fonk1(dataframe, sample_size):
    return sample(list(dataframe.nct_id.values), sample_size)
b3 = fonk1(b1, 211)
b4 = fonk1(b2, 422)
b5 = pd.DataFrame(b3, columns=['nct_id'])
b6 = pd.DataFrame(b4, columns=['nct_id'])
def fonk2(df):
    return ["https:
b5['urllist'] = fonk2(b5)
b6['urllist'] = fonk2(b6)
def fonk3(url):
    b7 = requests.get(url)
    b8 = BeautifulSoup(b7.text, "html.parser")
    b9 = b8.find_all(href=re.compile(r"\?V\_"))
    return len(b9)
b5['number'] = b5['urllist'].map(get_number_of_versions)
b6['number'] = b6['urllist'].map(get_number_of_versions)
def fonk4(df):
    return df['number'].map(lambda x: list(range(1, x + 1)))
b5['version_numbers'] = fonk4(b5)
b6['version_numbers'] = fonk4(b6)
def fonk5(df):
    b10 = [
        str(nct_id) + "?V_" + str(version) + "=View"
        for nct_id, versions in zip(df['nct_id'], df['version_numbers'])
        for version in versions
    ]
    b11 = df['nct_id'].repeat(df['number']).reset_index(drop=True)
    return pd.DataFrame({'nct_id': b11, 'version_url': b10})
b12 = fonk5(b5)
b13 = fonk5(b6)
def fonk6(url):
    b7 = requests.get(url)
    b8 = BeautifulSoup(b7.content, "html.parser")
    b14 = b8.find('div', attrs={"id": "ContactsLocationsBody"})
    if b14:
        b15 = b14.find_all('td')
        b16 = [ele.text.strip() for ele in b15]
        if len(b16) > 1:
            return b16[1]
    return None
def fonk7(df):
    df['full_url'] = "https:
    df['PI_info'] = df['full_url'].map(scrape_principal_investigator)
    return df
b12 = fonk7(b12)
b13 = fonk7(b13)
b12.to_csv('S8_07.csv', b17 = False)
b13.to_csv('S11_07.csv', b17 = False)