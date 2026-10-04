import csv
from parsel import Selector
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
b1 = csv.b1(open('output.csv', 'w+', encoding='utf-8-sig', newline=''))
b1.writerow(['Name', 'Position', 'Company', 'Education', 'Location', 'URL'])
b2 = webdriver.Chrome('C:
b2.get('https:
b3 = b2.find_element_by_name("session_key")
b3.send_keys('enter-your-email-here')
sleep(0.5)
b4 = b2.find_element_by_name('session_password')
b4.send_keys('enter-your-b4-here')
sleep(0.5)
b5 = b2.find_element_by_class_name('sign-in-form__submit-btn')
b5.click()
sleep(2)
b2.get('https:
b6 = b2.find_element_by_name('q')
b6.send_keys('site:linkedin.com/in AND "python developer" AND "london"')
b6.send_keys(Keys.RETURN)
sleep(0.5)
b7 = b2.find_elements_by_xpath('
b7 = [b15.get_attribute('href') for b15 in b7]
sleep(0.5)
for b15 in b7:
    b2.get(b15)
    sleep(2)
    b8 = Selector(text = b2.page_source)
    b9 = b8.xpath('
    b9 = ' '.join(b9)
    b10 = b8.xpath('
    b10 = ' '.join(b10)
    b11 = b8.xpath('
    b12 = b11.xpath('./li[@data-control-b9 = "position_see_more"]
    b12 = ''.join(b12.split()) if b12 else None
    b13 = b11.xpath('.
    b13 = ' '.join(b13.split()) if b13 else None
    b14 = ' '.join(b8.xpath('
    b15 = b2.current_url
    print('\n')
    print('Name: ', b9)
    print('Position: ', b10)
    print('Company: ', b12)
    print('Education: ', b13)
    print('Location: ', b14)
    print('URL: ', b15)
    print('\n')
    b1.writerow([b9,
                 b10,
                 b12,
                 b13,
                 b14,
                 b15])
b2.quit()