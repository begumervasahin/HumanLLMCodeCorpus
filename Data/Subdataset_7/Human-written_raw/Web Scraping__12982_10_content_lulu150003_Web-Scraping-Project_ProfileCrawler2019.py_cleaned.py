import requests
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from bs4 import BeautifulSoup
import pandas as pd
b1 = PASSWORD =
b2 = 'https:
b3 = webdriver.Firefox()
b3.get(b2)
time.sleep(3)
b4 = b3.find_element_by_name('session_key')
b5 = b3.find_element_by_name('session_password')
b4.send_keys(b1 + Keys.RETURN)
b5.send_keys(PASSWORD + Keys.RETURN)
time.sleep(3)
import csv
b6 = pd.read_csv("output_search.csv")
def fonk1(x):
    if x.lower().find('data') != -1 or x.lower().find('scien') != -1 or x.lower().find('Data') != -1 or x.lower().find('Scien') != -1 or x.lower().find('machine') != -1:
        return(1)
    else:
        return(0)
b6['driver'] = list(map(driving, b6['title']))
b6 = b6[b6.driver != 0]
b7 = pd.DataFrame(columns = ['b17', 'exp_title', 'exp_company', 'b20'])
b8 = pd.DataFrame(columns = ['b17', 'b24', 'b25', 'b26'])
b9 = pd.DataFrame(columns = ['b17', 'b27'])
for b10 in b6.loc[:,'b17']:
    if b10 = = 'https:
        continue
    time.sleep(2)
    b11 = b10
    b3.get(b11)
    time.sleep(2)
    b3.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)
    time.sleep(.75)
    b3.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)
    time.sleep(.75)
    b3.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)
    time.sleep(.75)
    b3.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)
    time.sleep(.75)
    b3.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)
    b12 = BeautifulSoup(b3.page_source, 'lxml')
    b13 = b12.find_all('div', class_ = "pv-entity__position-group-pager")
    b14 = b12.find_all('span', class_ = "pv-entity__secondary-title")
    b15 = b12.find_all('h4', class_ = "pv-entity__date-range")
    b16 = len(b12.find_all('div', class_ = "pv-entity__position-group-pager"))
    b17 = b10
    b18 = list(map(lambda x: x.h3.text.strip(), b13))[0:b16]
    b19 = list(map(lambda x: x.text.strip(), b14))[0:b16]
    b20 = list(map(lambda x: x.text.strip().split('\n')[-1], b15))[0:b16]
    b21 = b12.find_all('div', class_ = "pv-entity__degree-info")
    b22 = b12.find_all('p', class_ = "pv-entity__degree-name")
    b15 = b12.find_all('p', class_ = "pv-entity__dates")
    b23 = len(b12.find_all('div', class_ = "pv-entity__degree-info"))
    b17 = b10
    b24 = list(map(lambda x: x.text.strip().split('\n')[-1], b21))[0:b23]
    b25 = list(map(lambda x: x.text.strip().split('\n')[-1], b22))[0:b23]
    b26 = list(map(lambda x: x.text.strip().split('\n')[-1], b15))[0:b23]
    if len(b26) < b23:
        b26 = 'NA'
    b27 = b12.find_all('span', class_ = "pv-b27-category-entity__name-text")
    b28 = len(b12.find_all('span', class_ = "pv-b27-category-entity__name-text"))
    b17 = b10
    b27 = list(map(lambda x: x.text.strip(), b27))[0:b28]
    try:
        b29 = pd.DataFrame({'b17':b17, 'exp_title':b18, 'exp_company':b19, 'b20':b20})
        b30 = pd.DataFrame({'b17':b17, 'b24':b24, 'b25':b25, 'b26':b26})
        b31 = pd.DataFrame({'b17':b17, 'b27':b27})
        b7 = b7.append(b29)
        b8 = b8.append(b30)
        b9 = b9.append(b31)
        print(b10, 'completed')
    except:
        print(b10, 'skipped')
        continue
b7.reset_index()
b8.reset_index()
b9.reset_index()
b7.to_csv("output_experience.csv", b32 = False,sep='\t', encoding='utf-8')
b8.to_csv("output_education.csv", b32 = False,sep='\t', encoding='utf-8')
b9.to_csv("output_skills.csv", b32 = False,sep='\t', encoding='utf-8')
b3.quit()