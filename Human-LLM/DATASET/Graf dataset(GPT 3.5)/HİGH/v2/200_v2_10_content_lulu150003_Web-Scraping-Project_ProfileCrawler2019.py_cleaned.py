import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
b1 = "your_username"
b2 = "your_password"
def fonk1(x):
    b3 = ['data', 'scien', 'machine']
    if any(keyword.lower() in x.lower() for keyword in b3):
        return 1
    else:
        return 0
b4 = 'https:
b5 = webdriver.Firefox()
b5.get(b4)
time.sleep(3)
b6 = b5.find_element_by_name('session_key')
b7 = b5.find_element_by_name('session_password')
b6.send_keys(b1)
b7.send_keys(b2 + Keys.RETURN)
time.sleep(3)
b8 = pd.read_csv("output_search.csv")
b8['driver'] = b8['title'].apply(driving)
b8 = b8[b8['driver'] != 0]
b9 = pd.DataFrame(columns=['b18', 'exp_title', 'exp_company', 'b21'])
b10 = pd.DataFrame(columns=['b18', 'b25', 'b26', 'b27'])
b11 = pd.DataFrame(columns=['b18', 'b28'])
for b12 in b8['b18']:
    if b12 = = 'https:
        continue
    time.sleep(2)
    b5.get(b12)
    time.sleep(2)
    for _ in range(4):
        b5.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)
        time.sleep(0.75)
    b13 = BeautifulSoup(b5.page_source, 'html.parser')
    b14 = b13.find_all('div', class_="pv-entity__position-group-pager")
    b15 = b13.find_all('span', class_="pv-entity__secondary-title")
    b16 = b13.find_all('h4', class_="pv-entity__date-range")
    b17 = min(len(b14), len(b15), len(b16))
    b18 = b12
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
    b18 = b12
    b30 = [s.text.strip() for s in b28][:b29]
    try:
        b31 = pd.DataFrame({'b18': b18, 'exp_title': b19, 'exp_company': b20, 'b21': b21})
        b32 = pd.DataFrame({'b18': b18, 'b25': b25, 'b26': b26, 'b27': b27})
        b33 = pd.DataFrame({'b18': b18, 'b28': b30})
        b9 = b9.append(b31, ignore_index=True)
        b10 = b10.append(b32, ignore_index=True)
        b11 = b11.append(b33, ignore_index=True)
        print(b12, 'completed')
    except Exception as e:
        print(b12, 'skipped:', e)
        continue
b5.quit()
b9.to_csv("output_experience.csv", b34 = False, sep='\t', encoding='utf-8')
b10.to_csv("output_education.csv", b34 = False, sep='\t', encoding='utf-8')
b11.to_csv("output_skills.csv", b34 = False, sep='\t', encoding='utf-8')