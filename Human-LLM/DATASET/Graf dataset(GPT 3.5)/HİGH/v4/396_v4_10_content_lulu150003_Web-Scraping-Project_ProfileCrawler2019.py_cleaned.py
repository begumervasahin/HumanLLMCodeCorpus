import time
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
b1 = "your_username"
b2 = "your_password"
b3 = 'https:
b4 = webdriver.Firefox()
b4.get(b3)
time.sleep(3)
b5 = b4.find_element_by_name('session_key')
b6 = b4.find_element_by_name('session_password')
b5.send_keys(b1 + Keys.RETURN)
b6.send_keys(b2 + Keys.RETURN)
time.sleep(3)
b7 = pd.read_csv("output_search.csv")
def fonk1(x):
    if any(keyword.lower() in x.lower() for keyword in ['data', 'scien', 'machine']):
        return 1
    else:
        return 0
b7['driver'] = b7['title'].apply(driving)
b7 = b7[b7['driver'] != 0]
b8 = pd.DataFrame(columns=['b17', 'exp_title', 'exp_company', 'b20'])
b9 = pd.DataFrame(columns=['b17', 'b24', 'b25', 'b26'])
b10 = pd.DataFrame(columns=['b17', 'b27'])
for b11 in b7['b17']:
    if b11 = = 'https:
        continue
    time.sleep(2)
    b4.get(b11)
    time.sleep(2)
    for _ in range(4):
        b4.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)
        time.sleep(0.75)
    b12 = BeautifulSoup(b4.page_source, 'lxml')
    b13 = b12.find_all('div', class_="pv-entity__position-group-pager")
    b14 = b12.find_all('span', class_="pv-entity__secondary-title")
    b15 = b12.find_all('h4', class_="pv-entity__date-range")
    b16 = len(b13)
    b17 = b11
    b18 = [title.h3.text.strip() for title in b13][:b16]
    b19 = [company.text.strip() for company in b14][:b16]
    b20 = [date.text.strip().split('\n')[-1] for date in b15][:b16]
    b21 = b12.find_all('div', class_="pv-entity__degree-info")
    b22 = b12.find_all('p', class_="pv-entity__degree-name")
    b15 = b12.find_all('p', class_="pv-entity__dates")
    b23 = len(b21)
    b24 = [inst.text.strip().split('\n')[-1] for inst in b21][:b23]
    b25 = [deg.text.strip().split('\n')[-1] for deg in b22][:b23]
    b26 = [date.text.strip().split('\n')[-1] for date in b15][:b23]
    if len(b26) < b23:
        b26 = 'NA'
    b27 = b12.find_all('span', class_="pv-b27-category-entity__name-text")
    b28 = len(b27)
    b29 = [s.text.strip() for s in b27][:b28]
    try:
        b30 = pd.DataFrame({'b17': b17, 'exp_title': b18, 'exp_company': b19, 'b20': b20})
        b31 = pd.DataFrame({'b17': b17, 'b24': b24, 'b25': b25, 'b26': b26})
        b32 = pd.DataFrame({'b17': b17, 'b27': b29})
        b8 = b8.append(b30)
        b9 = b9.append(b31)
        b10 = b10.append(b32)
        print(b11, 'completed')
    except:
        print(b11, 'skipped')
        continue
b8.reset_index(b33 = True)
b9.reset_index(b33 = True)
b10.reset_index(b33 = True)
b8.to_csv("output_experience.csv", b34 = False, sep='\t', encoding='utf-8')
b9.to_csv("output_education.csv", b34 = False, sep='\t', encoding='utf-8')
b10.to_csv("output_skills.csv", b34 = False, sep='\t', encoding='utf-8')
b4.quit()