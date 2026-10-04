import csv
from parsel import Selector
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
b1 = 'enter-your-email-here'
b2 = 'enter-your-b7-here'
with open('output.csv', 'w+', b3 = 'utf-8-sig', newline='') as file:
    b4 = csv.b4(file)
    b4.writerow(['Name', 'Position', 'Company', 'Education', 'Location', 'URL'])
    b5 = webdriver.Chrome('C:
    b5.get('https:
    b6 = b5.find_element_by_name("session_key")
    b6.send_keys(b1)
    sleep(0.5)
    b7 = b5.find_element_by_name('session_password')
    b7.send_keys(b2)
    sleep(0.5)
    b8 = b5.find_element_by_class_name('sign-in-form__submit-btn')
    b8.click()
    sleep(2)
    b5.get('https:
    b9 = b5.find_element_by_name('q')
    b9.send_keys('site:linkedin.com/in AND "python developer" AND "london"')
    b9.send_keys(Keys.RETURN)
    sleep(0.5)
    b10 = b5.find_elements_by_xpath('
    b11 = [url.get_attribute('href') for url in b10]
    sleep(0.5)
    for profile_url in b11:
        b5.get(profile_url)
        sleep(2)
        b12 = Selector(text=b5.page_source)
        b13 = b12.xpath('
        b13 = ' '.join(b13.split()) if b13 else None
        b14 = b12.xpath('
        b14 = ' '.join(b14.split()) if b14 else None
        b15 = b12.xpath('
        b16 = b15.xpath('./li[@data-control-b13 = "position_see_more"]
        b16 = ' '.join(b16.split()) if b16 else None
        b17 = b15.xpath('.
        b17 = ' '.join(b17.split()) if b17 else None
        b18 = b12.xpath('
        b18 = ' '.join(b18.split()) if b18 else None
        b19 = b5.b19
        print(f'\nName: {b13}\nPosition: {b14}\nCompany: {b16}\nEducation: {b17}\nLocation: {b18}\nURL: {b19}\n')
        b4.writerow([b13, b14, b16, b17, b18, b19])
    b5.quit()