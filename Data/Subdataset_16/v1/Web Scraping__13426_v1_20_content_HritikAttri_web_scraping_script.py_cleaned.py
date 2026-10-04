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
    b10 = [url.get_attribute('href') for url in b10]
    sleep(0.5)
    for url in b10:
        b5.get(url)
        sleep(2)
        b11 = Selector(text=b5.page_source)
        b12 = b11.xpath('
        if b12:
            b12 = ' '.join(b12.split())
        b13 = b11.xpath('
        if b13:
            b13 = ' '.join(b13.split())
        b14 = b11.xpath('
        b15 = b14.xpath('./li[@data-control-b12 = "position_see_more"]
        if b15:
            b15 = ' '.join(b15.split())
        b16 = b14.xpath('.
        if b16:
            b16 = ' '.join(b16.split())
        b17 = b11.xpath('
        if b17:
            b17 = ' '.join(b17.split())
        b18 = b5.b18
        print('\n')
        print('Name: ', b12)
        print('Position: ', b13)
        print('Company: ', b15)
        print('Education: ', b16)
        print('Location: ', b17)
        print('URL: ', b18)
        print('\n')
        b4.writerow([b12, b13, b15, b16, b17, b18])
    b5.quit()