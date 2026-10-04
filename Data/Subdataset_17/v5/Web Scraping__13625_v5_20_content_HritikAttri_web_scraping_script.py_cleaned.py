import csv
from parsel import Selector
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
def linkedin_login(driver, email, password):
    driver.get('https:
    username_field = driver.find_element_by_name("session_key")
    username_field.send_keys(email)
    sleep(0.5)
    password_field = driver.find_element_by_name('session_password')
    password_field.send_keys(password)
    sleep(0.5)
    sign_in_button = driver.find_element_by_class_name('sign-in-form__submit-btn')
    sign_in_button.click()
    sleep(2)
def google_search(driver, query):
    driver.get('https:
    search_query_field = driver.find_element_by_name('q')
    search_query_field.send_keys(query)
    search_query_field.send_keys(Keys.RETURN)
    sleep(0.5)
def get_profile_urls(driver):
    urls = driver.find_elements_by_xpath('
    return [url.get_attribute('href') for url in urls]
def extract_profile_info(driver):
    sel = Selector(text=driver.page_source)
    name = sel.xpath('
    name = ' '.join(name.split()) if name else 'N/A'
    position = sel.xpath('
    position = ' '.join(position.split()) if position else 'N/A'
    experience = sel.xpath('
    company = experience.xpath('./li[@data-control-name = "position_see_more"]
    company = ' '.join(company.split()) if company else 'N/A'
    education = experience.xpath('.
    education = ' '.join(education.split()) if education else 'N/A'
    location = sel.xpath('
    location = ' '.join(location.split()) if location else 'N/A'
    profile_url = driver.current_url
    return {
        'name': name,
        'position': position,
        'company': company,
        'education': education,
        'location': location,
        'url': profile_url
    }
def write_to_csv(writer, profile_info):
    writer.writerow([
        profile_info['name'],
        profile_info['position'],
        profile_info['company'],
        profile_info['education'],
        profile_info['location'],
        profile_info['url']
    ])
def main():
    with open('output.csv', 'w+', encoding='utf-8-sig', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Position', 'Company', 'Education', 'Location', 'URL'])
        driver = webdriver.Chrome('C:
        linkedin_login(driver, 'enter-your-email-here', 'enter-your-password-here')
        google_search(driver, 'site:linkedin.com/in AND "python developer" AND "london"')
        profile_urls = get_profile_urls(driver)
        sleep(0.5)
        for url in profile_urls:
            driver.get(url)
            sleep(2)
            profile_info = extract_profile_info(driver)
            print('\n')
            print(f"Name: {profile_info['name']}")
            print(f"Position: {profile_info['position']}")
            print(f"Company: {profile_info['company']}")
            print(f"Education: {profile_info['education']}")
            print(f"Location: {profile_info['location']}")
            print(f"URL: {profile_info['url']}")
            print('\n')
            write_to_csv(writer, profile_info)
        driver.quit()
if __name__ == "__main__":
    main()