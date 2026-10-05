import pandas as pd
import requests
from bs4 import BeautifulSoup
import re
import time
import multiprocessing as mp
from multiprocessing.dummy import Pool as ThreadPool
base_url = "http:
index_range = range(1, 34000)
urls = [base_url.format(i) for i in index_range]
df = pd.DataFrame({'number': index_range, 'url': urls})
line_break_regex = re.compile(r'\\[nrt]')
def extract_text(url):
    extracted_data = []
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        table = soup.find('table')
        data_fields = ['CTRI Number', 'Last Modified On', 'Post Graduate Thesis', 'Type of Trial',
                       'Type of Study', 'Study Design', 'Public Title of Study', 'Scientific Title of Study',
                       'Secondary IDs if Any', 'Details of Principal Investigator', 'Public Query',
                       'Source of Monetary or Material Support', 'Primary Sponsor', 'Details of Secondary Sponsor',
                       'Countries of Recruitment', 'Sites of Study', 'Details of Ethics Committee',
                       'Regulatory Clearance Status from DCGI', 'Health Condition / Problems Studied',
                       'Health Type', 'Intervention / Comparator Agent', 'Comparator Agent', 'Inclusion Criteria',
                       'ExclusionCriteria', 'Method of Generating Random Sequence', 'Method of Concealment',
                       'Blinding/Masking', 'Primary Outcome', 'Secondary Outcome', 'Target Sample Size',
                       'Phase of Trial', 'Date of First Enrollment', 'Global', 'Estimated Duration of Trial',
                       'Recruitment Status of Trial', 'Publication Details', 'Brief Summary']
        extracted_values = []
        for field in data_fields:
            regex_pattern = r'(?sm)(?<={})([^A-Za-z]*)(\w+\W+.*?)(?={})'.format(field, data_fields[data_fields.index(field) + 1] if data_fields.index(field) < len(data_fields) - 1 else 'Source of Monetary or Material Support')
            extracted_value = re.findall(regex_pattern, table.text)
            extracted_value = line_break_regex.sub(' ', str(extracted_value))
            extracted_values.append(extracted_value)
        extracted_data.append('%;'.join(extracted_values))
        time.sleep(2)
    except Exception as e:
        extracted_data.append('no_value')
        print(f"Error extracting data from {url}: {e}")
    finally:
        return extracted_data
pool = ThreadPool(mp.cpu_count())
results = pool.map(extract_text, df['url'])
pool.close()
pool.join()
df_results = pd.DataFrame(results, columns=['all'])
df_merged = pd.concat([df, df_results], axis=1)
df_merged.to_excel('results_29May.xlsx', index=False)