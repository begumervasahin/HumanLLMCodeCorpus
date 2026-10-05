import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
import pandas as pd
USERNAME = "your_username"
PASSWORD = "your_password"
def driving(x):
    if any(keyword.lower() in x.lower() for keyword in ['data', 'scien', 'machine']):
        return 1
    else:
        return 0
linkedin = 'https:
browser = webdriver.Firefox()
browser.get(linkedin)
time.sleep(3)
email = browser.find_element_by_name('session_key')
password = browser.find_element_by_name('session_password')
email.send_keys(USERNAME)
password.send_keys(PASSWORD + Keys.RETURN)
time.sleep(3)
r = pd.read_csv("output_search.csv")
r['driver'] = r['title'].apply(driving)
r = r[r['driver'] != 0]
Exp_df = pd.DataFrame(columns=['profile', 'exp_title', 'exp_company', 'exp_dates'])
Edu_df = pd.DataFrame(columns=['profile', 'ed_name', 'ed_deg', 'ed_dates'])
Ski_df = pd.DataFrame(columns=['profile', 'skill'])
for link in r['profile']:
    if link == 'https:
        continue
    time.sleep(2)
    search = link
    browser.get(search)
    time.sleep(2)
    for _ in range(4):
        browser.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)
        time.sleep(0.75)
    page = BeautifulSoup(browser.page_source, 'html.parser')
    titles = page.find_all('div', class_="pv-entity__position-group-pager")
    companies = page.find_all('span', class_="pv-entity__secondary-title")
    dates = page.find_all('h4', class_="pv-entity__date-range")
    arraylen1 = min(len(titles), len(companies), len(dates))
    profile = link
    exp_titles = [title.h3.text.strip() for title in titles][:arraylen1]
    exp_companies = [company.text.strip() for company in companies][:arraylen1]
    exp_dates = [date.text.strip().split('\n')[-1] for date in dates][:arraylen1]
    institution = page.find_all('div', class_="pv-entity__degree-info")
    degree = page.find_all('p', class_="pv-entity__degree-name")
    dates = page.find_all('p', class_="pv-entity__dates")
    arraylen2 = min(len(institution), len(degree), len(dates))
    ed_name = [inst.text.strip().split('\n')[-1] for inst in institution][:arraylen2]
    ed_deg = [deg.text.strip().split('\n')[-1] for deg in degree][:arraylen2]
    ed_dates = [d.text.strip().split('\n')[-1] for d in dates][:arraylen2]
    if len(ed_dates) < arraylen2:
        ed_dates = 'NA'
    skill = page.find_all('span', class_="pv-skill-category-entity__name-text")
    arraylen3 = len(skill)
    profile = link
    skills = [s.text.strip() for s in skill][:arraylen3]
    try:
        temp1 = pd.DataFrame({'profile': profile, 'exp_title': exp_titles, 'exp_company': exp_companies, 'exp_dates': exp_dates})
        temp2 = pd.DataFrame({'profile': profile, 'ed_name': ed_name, 'ed_deg': ed_deg, 'ed_dates': ed_dates})
        temp3 = pd.DataFrame({'profile': profile, 'skill': skills})
        Exp_df = Exp_df.append(temp1, ignore_index=True)
        Edu_df = Edu_df.append(temp2, ignore_index=True)
        Ski_df = Ski_df.append(temp3, ignore_index=True)
        print(link, 'completed')
    except Exception as e:
        print(link, 'skipped:', e)
        continue
browser.quit()
Exp_df.to_csv("output_experience.csv", index=False, sep='\t', encoding='utf-8')
Edu_df.to_csv("output_education.csv", index=False, sep='\t', encoding='utf-8')
Ski_df.to_csv("output_skills.csv", index=False, sep='\t', encoding='utf-8')