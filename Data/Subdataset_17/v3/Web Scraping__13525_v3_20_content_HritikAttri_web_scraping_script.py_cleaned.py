import csv
from parsel import Selector
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
LINKEDIN_EMAIL = 'enter-your-email-here'
LINKEDIN_PASSWORD = 'enter-your-password-here'
CHROME_DRIVER_PATH = 'C:
CSV_FILE_PATH = 'output.csv'
def initialize_csv(file_path):
    with open(file_path, 'w+', encoding='utf-8-sig', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Position', 'Company', 'Education', 'Location', 'URL'])
def login_to_linkedin(driver, email, password):
    driver.get('https:
    driver.find_element_by_name("session_key").send_keys(email)
    sleep(0.5)
    driver.find_element_by_name('session_password').send_keys(password)
    sleep(0.5)
    driver.find_element_by_class_name('sign-in-form__submit-btn').click()
    sleep(2)
def perform_google_search(driver, query):
    driver.get('https:
    search_query = driver.find_element_by_name('q')
    search_query.send_keys(query)
    search_query.send_keys(Keys.RETURN)
    sleep(0.5)
def get_profile_urls(driver):
    urls = driver.find_elements_by_xpath('
    return [url.get_attribute('href') for url in urls]
def extract_profile_details(driver, url):
    driver.get(url)
    sleep(2)
    sel = Selector(text=driver.page_source)
    def extract_text(xpath):
        return ' '.join(sel.xpath(xpath).extract_first().split()) if sel.xpath(xpath).extract_first() else None
    name = extract_text('
    position = extract_text('
    experience = sel.xpath('
    company = extract_text('./li[@data-control-name = "position_see_more"]
    education = extract_text('.
    location = extract_text('
    return name, position, company, education, location, url
def main():
    initialize_csv(CSV_FILE_PATH)
    driver = webdriver.Chrome(CHROME_DRIVER_PATH)
    try:
        login_to_linkedin(driver, LINKEDIN_EMAIL, LINKEDIN_PASSWORD)
        perform_google_search(driver, 'site:linkedin.com/in AND "python developer" AND "london"')
        profile_urls = get_profile_urls(driver)
        with open(CSV_FILE_PATH, 'a+', encoding='utf-8-sig', newline='') as file:
            writer = csv.writer(file)
            for profile_url in profile_urls:
                name, position, company, education, location, current_url = extract_profile_details(driver, profile_url)
                print(f'\nName: {name}\nPosition: {position}\nCompany: {company}\nEducation: {education}\nLocation: {location}\nURL: {current_url}\n')
                writer.writerow([name, position, company, education, location, current_url])
    finally:
        driver.quit()
if __name__ == "__main__":
    main()