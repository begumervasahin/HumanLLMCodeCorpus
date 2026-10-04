import csv
from parsel import Selector
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
writer = csv.writer(open('output.csv', 'w+', encoding='utf-8-sig', newline=''))
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
    sel = Selector(text = driver.page_source)
    name = sel.xpath('
    name = ' '.join(name)
    position = sel.xpath('
    position = ' '.join(position)
    experience = sel.xpath('
    company = experience.xpath('./li[@data-control-name = "position_see_more"]
    company = ''.join(company.split()) if company else None
    education = experience.xpath('.
    education = ' '.join(education.split()) if education else None
    location = ' '.join(sel.xpath('
    url = driver.current_url
    print('\n')
    print('Name: ', name)
    print('Position: ', position)
    print('Company: ', company)
    print('Education: ', education)
    print('Location: ', location)
    print('URL: ', url)
    print('\n')
    writer.writerow([name,
                 position,
                 company,
                 education,
                 location,
                 url])
driver.quit()