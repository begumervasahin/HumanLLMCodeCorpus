import csv
from parsel import Selector
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
with open('output.csv', 'w+', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Position', 'Company', 'Education', 'Location', 'URL'])
driver = webdriver.Chrome('C:
driver.get('https:
username = driver.find_element_by_name("session_key")
username.send_keys('enter-your-email-here')
sleep(0.5)
password = driver.find_element_by_name('session_password')
password.send_keys('enter-your-password-here')
sleep(0.5)
sign_in_button = driver.find_element_by_class_name('sign-in-form__submit-btn')
sign_in_button.click()
sleep(2)
driver.get('https:
search_query = driver.find_element_by_name('q')
search_query.send_keys('site:linkedin.com/in AND "python developer" AND "london"')
search_query.send_keys(Keys.RETURN)
sleep(0.5)
urls = driver.find_elements_by_xpath('
urls = [url.get_attribute('href') for url in urls]
sleep(0.5)
for url in urls:
    driver.get(url)
    sleep(2)
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
    print('\n')
    print(f'Name: {name}')
    print(f'Position: {position}')
    print(f'Company: {company}')
    print(f'Education: {education}')
    print(f'Location: {location}')
    print(f'URL: {profile_url}')
    print('\n')
    with open('output.csv', 'a+', encoding='utf-8-sig', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, position, company, education, location, profile_url])
driver.quit()