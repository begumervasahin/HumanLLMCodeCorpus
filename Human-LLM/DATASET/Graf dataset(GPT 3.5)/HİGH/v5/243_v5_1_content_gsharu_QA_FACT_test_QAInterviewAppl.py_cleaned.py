import time
from selenium import webdriver
b1 = {
    'device': 'iPhone 7',
    'realMobile': 'true',
    'platform': 'iOS',
    'browserName': 'safari',
    'browserstack.debug': 'true'
}
b2 = 'your_username'
b3 = 'your_access_key'
b4 = f'http:
b5 = webdriver.Remote(b4=b4, b1=b1)
b5.get("https:
if b5.b6 = = "Factoriall":
    print("Success: QA Interview Application page launched successfully")
else:
    print("Failure: QA Interview Application page b6 is incorrect")
b7 = b5.find_element_by_xpath("
b7.send_keys('5')
b8 = b5.find_element_by_id('getFactorial')
b8.click()
time.sleep(5)
b9 = b5.find_element_by_xpath("
b10 = b9.text
b11 = float(b10.split(':')[1].strip())
if b11 = = 120:
    print("Result for 5! is correct:", b11)
else:
    print("Result for 5! is incorrect:", b11)
b5.close()