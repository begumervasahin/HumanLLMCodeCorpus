import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
b1 = "your_username"
b2 = "your_password"
def fonk1(title):
    b3 = ['data', 'scien', 'machine']
    return any(keyword.lower() in title.lower() for keyword in b3)
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
b8['has_keywords'] = b8['title'].apply(has_keywords)
b9 = b8[b8['has_keywords']]
b10 = pd.DataFrame(columns=['b19', 'exp_title', 'exp_company', 'b22'])
b11 = pd.DataFrame(columns=['b19', 'b25', 'b26', 'b27'])
b12 = pd.DataFrame(columns=['b19', 'skill'])
for b13 in b9['b19']:
    if b13 = = b4:
        continue
    time.sleep(2)
    b5.get(b13)
    time.sleep(2)
    for _ in range(4):
        b5.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)
        time.sleep(0.75)
    b14 = BeautifulSoup(b5.page_source, 'html.parser')
    b15 = b14.find_all('div', class_="pv-entity__position-group-pager")
    b16 = b14.find_all('span', class_="pv-entity__secondary-title")
    b17 = b14.find_all('h4', class_="pv-entity__date-range")
    b18 = min(len(b15), len(b16), len(b17))
    b19 = b13
    b20 = [title.h3.text.strip() for title in b15][:b18]
    b21 = [company.text.strip() for company in b16][:b18]
    b22 = [date.text.strip().split('\n')[-1] for date in b17][:b18]
    b23 = b14.find_all('div', class_="pv-entity__degree-info")
    b24 = b14.find_all('p', class_="pv-entity__degree-name")
    b17 = b14.find_all('p', class_="pv-entity__dates")
    b18 = min(len(b23), len(b24), len(b17))
    b25 = [inst.text.strip().split('\n')[-1] for inst in b23][:b18]
    b26 = [deg.text.strip().split('\n')[-1] for deg in b24][:b18]
    b27 = [d.text.strip().split('\n')[-1] for d in b17][:b18]
    if len(b27) < b18:
        b27 = 'NA'
    b28 = b14.find_all('span', class_="pv-skill-category-entity__name-text")
    b28 = [s.text.strip() for s in b28]
    try:
        b10 = b10.append({'b19': b19, 'exp_title': b20, 'exp_company': b21, 'b22': b22}, ignore_index=True)
        b11 = b11.append({'b19': b19, 'b25': b25, 'b26': b26, 'b27': b27}, ignore_index=True)
        b12 = b12.append({'b19': b19, 'skill': b28}, ignore_index=True)
        print(b13, 'completed')
    except Exception as e:
        print(b13, 'skipped:', e)
        continue
b5.quit()
b10.to_csv("output_experience.csv", b29 = False, sep='\t', encoding='utf-8')
b11.to_csv("output_education.csv", b29 = False, sep='\t', encoding='utf-8')
b12.to_csv("output_skills.csv", b29 = False, sep='\t', encoding='utf-8')