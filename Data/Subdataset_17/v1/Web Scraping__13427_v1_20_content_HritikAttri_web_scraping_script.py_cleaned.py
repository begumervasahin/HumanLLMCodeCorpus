import csv
from parsel import Selector
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
linkedin_email = 'enter-your-email-here'
linkedin_password = 'enter-your-password-here'
with open('output.csv', 'w+', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Position', 'Company', 'Education', 'Location', 'URL'])
    driver = webdriver.Chrome('C:
    driver.get('https:
    username = driver.find_element_by_name("session_key")
    username.send_keys(linkedin_email)
    sleep(0.5)
    password = driver.find_element_by_name('session_password')
    password.send_keys(linkedin_password)
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
        if name:
            name = ' '.join(name.split())
        position = sel.xpath('
        if position:
            position = ' '.join(position.split())
        experience = sel.xpath('
        company = experience.xpath('./li[@data-control-name = "position_see_more"]
        if company:
            company = ' '.join(company.split())
        education = experience.xpath('.
        if education:
            education = ' '.join(education.split())
        location = sel.xpath('
        if location:
            location = ' '.join(location.split())
        current_url = driver.current_url
        print('\n')
        print('Name: ', name)
        print('Position: ', position)
        print('Company: ', company)
        print('Education: ', education)
        print('Location: ', location)
        print('URL: ', current_url)
        print('\n')
        writer.writerow([name, position, company, education, location, current_url])
    driver.quit()