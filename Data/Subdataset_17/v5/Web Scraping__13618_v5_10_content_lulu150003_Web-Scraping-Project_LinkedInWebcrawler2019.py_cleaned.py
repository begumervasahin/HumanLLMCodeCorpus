from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
from bs4 import BeautifulSoup
import pandas as pd
def initialize_browser():
    browser = webdriver.Firefox()
    browser.get('https:
    time.sleep(3)
    return browser
def login(browser, username, password):
    email_input = browser.find_element_by_name('session_key')
    password_input = browser.find_element_by_name('session_password')
    email_input.send_keys(username + Keys.RETURN)
    password_input.send_keys(password + Keys.RETURN)
    time.sleep(3)
def load_search_results(browser, company_id):
    search_url = f"https:
    browser.get(search_url)
    time.sleep(3)
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
def extract_profiles_from_page(browser, linkedin_url):
    page = BeautifulSoup(browser.page_source, 'lxml')
    names = [name.text for name in page.find_all('span', class_='actor-name')]
    titles = [title.text.strip() for title in page.find_all('p', class_='subline-level-1')]
    locations = [location.text.strip() for location in page.find_all('p', class_='subline-level-2')]
    profiles = [linkedin_url + profile['href'] for profile in page.find_all('a', class_='search-result__result-link')[::2]]
    data = {
        'name': names,
        'title': titles,
        'location': locations,
        'profile': profiles
    }
    return pd.DataFrame(data)
def main():
    company_id = input("Enter Company ID: ")
    username = input("Enter username: ")
    password = input("Enter password: ")
    employee_limit = 1000
    linkedin_url = 'https:
    browser = initialize_browser()
    login(browser, username, password)
    load_search_results(browser, company_id)
    df = pd.DataFrame(columns=['name', 'title', 'location', 'profile'])
    current_url = 'url_placeholder'
    while True:
        if 'page=100' in current_url:
            break
        previous_url = current_url
        current_url = browser.current_url
        if current_url == previous_url:
            break
        temp_df = extract_profiles_from_page(browser, linkedin_url)
        temp_df = temp_df[temp_df['name'] != 'LinkedIn Member']
        df = df.append(temp_df, ignore_index=True)
        if df.shape[0] >= employee_limit:
            break
        try:
            next_button = browser.find_element_by_class_name('next')
            next_button.click()
        except NoSuchElementException:
            print("No more pages or navigation error.")
            break
        time.sleep(5)
    df.reset_index(drop=True, inplace=True)
    df.to_csv("output_search.csv", index=False)
    browser.quit()
if __name__ == "__main__":
    main()