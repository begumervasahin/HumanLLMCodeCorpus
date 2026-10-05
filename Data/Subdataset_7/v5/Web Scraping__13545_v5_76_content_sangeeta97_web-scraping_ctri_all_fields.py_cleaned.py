import pandas as pd
import requests
from bs4 import BeautifulSoup
import re
import time
import multiprocessing as mp
from multiprocessing.dummy import Pool as ThreadPool
b1 = "http:
b2 = range(1, 34000)
b3 = [b1.format(i) for i in b2]
b4 = pd.DataFrame({'number': b2, 'url': b3})
b5 = re.compile(r'\\[nrt]')
def fonk1(url):
    b6 = []
    try:
        b7 = requests.get(url)
        b8 = BeautifulSoup(b7.text, 'lxml')
        b9 = b8.find('b9')
        b10 = ['CTRI Number', 'Last Modified On', 'Post Graduate Thesis', 'Type of Trial',
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
        b11 = []
        for field in b10:
            b12 = r'(?sm)(?<={})([^A-Za-z]*)(\w+\W+.*?)(?={})'.format(field, b10[b10.b18(field) + 1] if b10.b18(field) < len(b10) - 1 else 'Source of Monetary or Material Support')
            b13 = re.findall(b12, b9.text)
            b13 = b5.sub(' ', str(b13))
            b11.append(b13)
        b6.append('%;'.join(b11))
        time.sleep(2)
    except Exception as e:
        b6.append('no_value')
        print(f"Error extracting data from {url}: {e}")
    finally:
        return b6
b14 = ThreadPool(mp.cpu_count())
b15 = b14.map(extract_text, b4['url'])
b14.close()
b14.join()
b16 = pd.DataFrame(b15, columns=['all'])
b17 = pd.concat([b4, b16], axis=1)
b17.to_excel('results_29May.xlsx', b18 = False)