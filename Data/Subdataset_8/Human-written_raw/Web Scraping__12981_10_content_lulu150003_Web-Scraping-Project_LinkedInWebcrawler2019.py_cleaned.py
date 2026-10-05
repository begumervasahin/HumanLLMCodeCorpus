from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
import pandas as pd
COMPANY = input("Enter Company ID: ")
USERNAME = input("Enter username: ")
PASSWORD = input("Enter password: ")
EMPLOYEE = 1000
linkedin = 'https:
browser = webdriver.Firefox()
browser.get(linkedin)
time.sleep(3)
email = browser.find_element_by_name('session_key')
password = browser.find_element_by_name('session_password')
email.send_keys(USERNAME + Keys.RETURN)
password.send_keys(PASSWORD + Keys.RETURN)
time.sleep(3)
search = "https:
browser.get(search)
time.sleep(3)
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
current_url = 'url_placeholder'
df = pd.DataFrame(columns = ['name', 'title', 'location', 'profile'])
    while True:
        if current_url.find('page=100') != -1:
            break
        previous_url = current_url
        current_url = browser.current_url
        if current_url == previous_url:
            break
        page = BeautifulSoup(browser.page_source, 'lxml')
        page_names = page.find_all('span', class_ = 'actor-name')
        page_titles = page.find_all('p', class_ = 'subline-level-1')
        page_locations = page.find_all('p', class_ = 'subline-level-2')
        page_profiles = page.find_all('a', class_ = 'search-result__result-link')
        names = list(map(lambda x: x.text, page_names))
        titles = list(map(lambda x: x.text.replace('\n', ''), page_titles))
        locations = list(map(lambda x: x.text.replace('\n', ''), page_locations))
        profiles = list(map(lambda x: linkedin + x['href'], page_profiles))[::2]
        temp = pd.DataFrame({'name':names, 'title':titles, 'location':locations, 'profile':profiles})
        temp = temp[temp['name'] != 'LinkedIn Member']
        df = df.append(temp)
        if df.shape[0] >= EMPLOYEE:
            break
        nextt = browser.find_element_by_class_name('next')
        nextt.click()
        time.sleep(5)
df.reset_index()
df.to_csv("output_search.csv", index = False)
browser.quit()