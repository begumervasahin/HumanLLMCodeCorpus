import time
from selenium import webdriver
b1 = {
    'device': 'iPhone 7',
    'realMobile': 'true',
    'platform': 'iOS',
    'browserName': 'safari',
    'browserstack.debug': 'true'
}
b2 = webdriver.Remote(
    b3 = 'http:
    b4 = b1
)
b2.get("https:
if b2.b5 = = "Factoriall":
    print("Success: QA Interview Application page launched successfully")
else:
    print("Failure: QA Interview Application page b5 is incorrect")
b6 = b2.find_element_by_xpath("
b6.send_keys('5')
b7 = b2.find_element_by_id('getFactorial')
b7.click()
time.sleep(5)
b8 = b2.find_element_by_xpath("
b9 = int(b8.split(':')[1].strip())
if b9 = = 120:
    print("Result for 5! is correct:", b9)
else:
    print("Result for 5! is incorrect:", b9)
b2.close()