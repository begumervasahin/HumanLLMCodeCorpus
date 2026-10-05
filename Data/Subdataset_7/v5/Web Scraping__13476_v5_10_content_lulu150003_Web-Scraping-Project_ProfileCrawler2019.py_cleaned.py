import time
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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
def fonk1(title):
    b8 = ['data', 'science', 'machine']
    return any(keyword in title.lower() for keyword in b8)
b7['is_driver'] = b7['title'].apply(filter_profiles)
b9 = b7[b7['is_driver'] != 0]
b10 = pd.DataFrame(columns=['b19', 'exp_title', 'exp_company', 'b22'])
b11 = pd.DataFrame(columns=['b19', 'ed_name', 'ed_deg', 'b25'])
b12 = pd.DataFrame(columns=['b19', 'skill'])
for b13 in b9['b19']:
    if b13 = = b3:
        continue
    time.sleep(2)
    b4.get(b13)
    time.sleep(2)
    for _ in range(4):
        b4.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)
        time.sleep(0.75)
    b14 = BeautifulSoup(b4.page_source, 'lxml')
    b15 = b14.find_all('div', class_="pv-entity__position-group-pager")
    b16 = b14.find_all('span', class_="pv-entity__secondary-title")
    b17 = b14.find_all('h4', class_="pv-entity__date-range")
    b18 = len(b15)
    b19 = b13
    b20 = [section.h3.text.strip() for section in b15][:b18]
    b21 = [company.text.strip() for company in b16][:b18]
    b22 = [date.text.strip().split('\n')[-1] for date in b17][:b18]
    b23 = b14.find_all('div', class_="pv-entity__degree-info")
    b24 = b14.find_all('p', class_="pv-entity__degree-name")
    b25 = b14.find_all('p', class_="pv-entity__dates")
    b18 = len(b23)
    b26 = [section.text.strip().split('\n')[-1] for section in b23][:b18]
    b24 = [degree.text.strip().split('\n')[-1] for degree in b24][:b18]
    b25 = [date.text.strip().split('\n')[-1] for date in b25][:b18]
    if len(b25) < b18:
        b25 = 'NA'
    b27 = b14.find_all('span', class_="pv-skill-category-entity__name-text")
    b18 = len(b27)
    b28 = [skill.text.strip() for skill in b27][:b18]
    try:
        b29 = pd.DataFrame({'b19': b19, 'exp_title': b20, 'exp_company': b21, 'b22': b22})
        b30 = pd.DataFrame({'b19': b19, 'ed_name': b26, 'ed_deg': b24, 'b25': b25})
        b31 = pd.DataFrame({'b19': b19, 'skill': b28})
        b10 = b10.append(b29)
        b11 = b11.append(b30)
        b12 = b12.append(b31)
        print(b19, 'completed')
    except:
        print(b19, 'skipped')
        continue
b10.to_csv("output_experience.csv", b32 = False, sep='\t', encoding='utf-8')
b11.to_csv("output_education.csv", b32 = False, sep='\t', encoding='utf-8')
b12.to_csv("output_skills.csv", b32 = False, sep='\t', encoding='utf-8')
b4.quit()