
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
import pandas as pd
COMPANY = input("Enter Company ID: ")
USERNAME = input("Enter username: ")
PASSWORD = input("Enter password: ")
EMPLOYEE = 1000
linkedin_url = 'https:
browser = webdriver.Firefox()
browser.get(linkedin_url)
time.sleep(3)
email_field = browser.find_element_by_name('session_key')
password_field = browser.find_element_by_name('session_password')
email_field.send_keys(USERNAME + Keys.RETURN)
password_field.send_keys(PASSWORD + Keys.RETURN)
time.sleep(3)
search_url = f"https:
browser.get(search_url)
time.sleep(3)
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
df = pd.DataFrame(columns=['name', 'title', 'location', 'profile'])
current_url = 'url_placeholder'
while True:
    if current_url.find('page=100') != -1:
        break
    previous_url = current_url
    current_url = browser.current_url
    if current_url == previous_url:
        break
    page = BeautifulSoup(browser.page_source, 'lxml')
    page_names = page.find_all('span', class_='actor-name')
    page_titles = page.find_all('p', class_='subline-level-1')
    page_locations = page.find_all('p', class_='subline-level-2')
    page_profiles = page.find_all('a', class_='search-result__result-link')
    names = [name.text for name in page_names]
    titles = [title.text.replace('\n', '') for title in page_titles]
    locations = [location.text.replace('\n', '') for location in page_locations]
    profiles = [linkedin_url + profile['href'] for profile in page_profiles][::2]
    temp_df = pd.DataFrame({'name': names, 'title': titles, 'location': locations, 'profile': profiles})
    temp_df = temp_df[temp_df['name'] != 'LinkedIn Member']
    df = df.append(temp_df)
    if df.shape[0] >= EMPLOYEE:
        break
    next_button = browser.find_element_by_class_name('next')
    next_button.click()
    time.sleep(5)
df.reset_index(drop=True, inplace=True)
df.to_csv("output_search.csv", index=False)
browser.quit()