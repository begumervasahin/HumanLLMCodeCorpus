import pandas as pd
import requests
from bs4 import BeautifulSoup
from random import sample
import re
df_s8 = pd.read_csv('S8nested6feb.csv')
df_s11 = pd.read_csv('sk_S116feb19.csv')
def random_sample(dataframe, sample_size):
    return sample(list(dataframe.nct_id.values), sample_size)
s8_sample = random_sample(df_s8, 211)
s11_sample = random_sample(df_s11, 422)
df_s8_sampled = pd.DataFrame(s8_sample, columns=['nct_id'])
df_s11_sampled = pd.DataFrame(s11_sample, columns=['nct_id'])
def generate_urls(df):
    return ["https:
df_s8_sampled['urllist'] = generate_urls(df_s8_sampled)
df_s11_sampled['urllist'] = generate_urls(df_s11_sampled)
def get_number_of_versions(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    version_links = soup.find_all(href=re.compile(r"\?V\_"))
    return len(version_links)
df_s8_sampled['number'] = df_s8_sampled['urllist'].map(get_number_of_versions)
df_s11_sampled['number'] = df_s11_sampled['urllist'].map(get_number_of_versions)
def generate_version_numbers(df):
    return df['number'].map(lambda x: list(range(1, x + 1)))
df_s8_sampled['version_numbers'] = generate_version_numbers(df_s8_sampled)
df_s11_sampled['version_numbers'] = generate_version_numbers(df_s11_sampled)
def create_version_df(df):
    version_urls = [
        str(nct_id) + "?V_" + str(version) + "=View"
        for nct_id, versions in zip(df['nct_id'], df['version_numbers'])
        for version in versions
    ]
    repeated_nct_ids = df['nct_id'].repeat(df['number']).reset_index(drop=True)
    return pd.DataFrame({'nct_id': repeated_nct_ids, 'version_url': version_urls})
df_s8_versions = create_version_df(df_s8_sampled)
df_s11_versions = create_version_df(df_s11_sampled)
def scrape_principal_investigator(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    contacts_section = soup.find('div', attrs={"id": "ContactsLocationsBody"})
    if contacts_section:
        td_elements = contacts_section.find_all('td')
        contact_info = [ele.text.strip() for ele in td_elements]
        if len(contact_info) > 1:
            return contact_info[1]
    return None
def add_pi_info(df):
    df['full_url'] = "https:
    df['PI_info'] = df['full_url'].map(scrape_principal_investigator)
    return df
df_s8_versions = add_pi_info(df_s8_versions)
df_s11_versions = add_pi_info(df_s11_versions)
df_s8_versions.to_csv('S8_07.csv', index=False)
df_s11_versions.to_csv('S11_07.csv', index=False)