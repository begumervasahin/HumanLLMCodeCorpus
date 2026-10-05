import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
import pandas as pd
b1 = "your_username"
b2 = "your_password"
def fonk1(x):
    if any(keyword.lower() in x.lower() for keyword in ['data', 'scien', 'machine']):
        return 1
    else:
        return 0
b3 = 'https:
b4 = webdriver.Firefox()
b4.get(b3)
time.sleep(3)
b5 = b4.find_element_by_name('session_key')
b6 = b4.find_element_by_name('session_password')
b5.send_keys(b1)
b6.send_keys(b2 + Keys.RETURN)
time.sleep(3)
b7 = pd.read_csv("output_search.csv")
b7['driver'] = b7['title'].apply(driving)
b7 = b7[b7['driver'] != 0]
b8 = pd.DataFrame(columns=['b18', 'exp_title', 'exp_company', 'b21'])
b9 = pd.DataFrame(columns=['b18', 'b25', 'b26', 'b27'])
b10 = pd.DataFrame(columns=['b18', 'b28'])
for b11 in b7['b18']:
    if b11 = = 'https:
        continue
    time.sleep(2)
    b12 = b11
    b4.get(b12)
    time.sleep(2)
    for _ in range(4):
        b4.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)
        time.sleep(0.75)
    b13 = BeautifulSoup(b4.page_source, 'html.parser')
    b14 = b13.find_all('div', class_="pv-entity__position-group-pager")
    b15 = b13.find_all('span', class_="pv-entity__secondary-title")
    b16 = b13.find_all('h4', class_="pv-entity__date-range")
    b17 = min(len(b14), len(b15), len(b16))
    b18 = b11
    b19 = [title.h3.text.strip() for title in b14][:b17]
    b20 = [company.text.strip() for company in b15][:b17]
    b21 = [date.text.strip().split('\n')[-1] for date in b16][:b17]
    b22 = b13.find_all('div', class_="pv-entity__degree-info")
    b23 = b13.find_all('p', class_="pv-entity__degree-name")
    b16 = b13.find_all('p', class_="pv-entity__dates")
    b24 = min(len(b22), len(b23), len(b16))
    b25 = [inst.text.strip().split('\n')[-1] for inst in b22][:b24]
    b26 = [deg.text.strip().split('\n')[-1] for deg in b23][:b24]
    b27 = [d.text.strip().split('\n')[-1] for d in b16][:b24]
    if len(b27) < b24:
        b27 = 'NA'
    b28 = b13.find_all('span', class_="pv-b28-category-entity__name-text")
    b29 = len(b28)
    b18 = b11
    b30 = [s.text.strip() for s in b28][:b29]
    try:
        b31 = pd.DataFrame({'b18': b18, 'exp_title': b19, 'exp_company': b20, 'b21': b21})
        b32 = pd.DataFrame({'b18': b18, 'b25': b25, 'b26': b26, 'b27': b27})
        b33 = pd.DataFrame({'b18': b18, 'b28': b30})
        b8 = b8.append(b31, ignore_index=True)
        b9 = b9.append(b32, ignore_index=True)
        b10 = b10.append(b33, ignore_index=True)
        print(b11, 'completed')
    except Exception as e:
        print(b11, 'skipped:', e)
        continue
b4.quit()
b8.to_csv("output_experience.csv", b34 = False, sep='\t', encoding='utf-8')
b9.to_csv("output_education.csv", b34 = False, sep='\t', encoding='utf-8')
b10.to_csv("output_skills.csv", b34 = False, sep='\t', encoding='utf-8')