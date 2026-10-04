import pandas as pd
import requests
from bs4 import BeautifulSoup
from random import sample
import re
df2 = pd.read_csv('S8nested6feb.csv')
df1 = pd.read_csv('sk_S116feb19.csv')
s8random = sample(df2['nct_id'].tolist(), 211)
s11random = sample(df1['nct_id'].tolist(), 422)
total8 = pd.DataFrame(s8random, columns=['nct_id'])
total11 = pd.DataFrame(s11random, columns=['nct_id'])
total8['urllist'] = total8['nct_id'].apply(lambda x: f"https:
total11['urllist'] = total11['nct_id'].apply(lambda x: f"https:
def get_number(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    versions = soup.find_all(href=re.compile(r"\?V\_"))
    return len(versions)
total8['number'] = total8['urllist'].map(get_number)
total8['num6'] = total8['number'].map(lambda x: list(range(1, x+1)))
expanded_s8_ids = list(total8['nct_id'] * total8['number'])
expanded_s8 = pd.DataFrame(expanded_s8_ids, total8['num6']).reset_index()
expanded_s8.columns = ['version', 'nct_id']
expanded_s8['nct_id'] = expanded_s8['nct_id'].str.split(',')
def split_and_expand(df):
    df = df.stack().apply(pd.Series).stack().unstack(1)
    df['ff'] = list(zip(df['version'].astype(str), df['nct_id'].astype(str)))
    df['nurl'] = df['ff'].apply(lambda x: f"https:
    return df
expanded_s8 = split_and_expand(expanded_s8)
def scrape_PI(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    contact_section = soup.find('div', id="ContactsLocationsBody")
    if contact_section:
        contact_details = [td.text.strip() for td in contact_section.find_all('td')]
        return contact_details[1] if contact_details else None
    return None
expanded_s8['History_Contacts'] = expanded_s8['nurl'].map(scrape_PI)
expanded_s8.to_csv('S8_07.csv', index=False)
total11['number'] = total11['urllist'].map(get_number)
total11['num6'] = total11['number'].map(lambda x: list(range(1, x+1)))
expanded_s11_ids = list(total11['nct_id'] * total11['number'])
expanded_s11 = pd.DataFrame(expanded_s11_ids, total11['num6']).reset_index()
expanded_s11.columns = ['version', 'nct_id']
expanded_s11['nct_id'] = expanded_s11['nct_id'].str.split(',')
expanded_s11 = split_and_expand(expanded_s11)
expanded_s11['History_Contacts'] = expanded_s11['nurl'].map(scrape_PI)
expanded_s11.to_csv('S11_07.csv', index=False)