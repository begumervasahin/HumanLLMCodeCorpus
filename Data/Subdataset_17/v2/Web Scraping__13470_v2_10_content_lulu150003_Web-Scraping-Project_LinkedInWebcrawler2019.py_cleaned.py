from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
import pandas as pd
import time
COMPANY = input("Enter Company ID: ")
USERNAME = input("Enter username: ")
PASSWORD = input("Enter password: ")
EMPLOYEE_LIMIT = 1000
LINKEDIN_URL = 'https:
options = Options()
options.headless = False
service = Service('/path/to/geckodriver')
browser = webdriver.Firefox(service=service, options=options)
def login_to_linkedin(username, password):
    browser.get(LINKEDIN_URL)
    time.sleep(3)
    email_field = browser.find_element(By.NAME, 'session_key')
    password_field = browser.find_element(By.NAME, 'session_password')
    email_field.send_keys(username)
    password_field.send_keys(password + Keys.RETURN)
    time.sleep(3)
def search_company_employees(company_id):
    search_url = f"https:
    browser.get(search_url)
    time.sleep(3)
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
def parse_page():
    soup = BeautifulSoup(browser.page_source, 'lxml')
    names = [element.text for element in soup.find_all('span', class_='actor-name')]
    titles = [element.text.strip() for element in soup.find_all('span', class_='subline-level-1')]
    locations = [element.text.strip() for element in soup.find_all('span', class_='subline-level-2')]
    profiles = [LINKEDIN_URL + element['href'] for element in soup.find_all('a', class_='search-result__result-link')][::2]
    return pd.DataFrame({
        'name': names,
        'title': titles,
        'location': locations,
        'profile': profiles
    })
def scrape_employees(employee_limit):
    df = pd.DataFrame(columns=['name', 'title', 'location', 'profile'])
    current_url = browser.current_url
    while True:
        if 'page=100' in current_url or len(df) >= employee_limit:
            break
        previous_url = current_url
        current_url = browser.current_url
        if current_url == previous_url:
            break
        temp_df = parse_page()
        temp_df = temp_df[temp_df['name'] != 'LinkedIn Member']
        df = df.append(temp_df, ignore_index=True)
        try:
            next_button = browser.find_element(By.CLASS_NAME, 'artdeco-pagination__button--next')
            next_button.click()
            time.sleep(5)
        except Exception as e:
            print(f"Error: {e}")
            break
    return df
def main():
    login_to_linkedin(USERNAME, PASSWORD)
    search_company_employees(COMPANY)
    employee_data = scrape_employees(EMPLOYEE_LIMIT)
    employee_data.reset_index(drop=True, inplace=True)
    employee_data.to_csv("output_search.csv", index=False)
    browser.quit()
if __name__ == "__main__":
    main()