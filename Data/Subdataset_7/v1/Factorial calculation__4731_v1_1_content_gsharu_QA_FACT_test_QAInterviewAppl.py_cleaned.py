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
    print("Failure: QA Interview Application page Title is incorrect")
b2.find_element_by_xpath("
b2.find_element_by_id('getFactorial').click()
time.sleep(5)
b6 = b2.find_element_by_xpath("
b7 = float(b6.split(':')[1].strip())
if b7 = = 120:
    print("Result for 5! is correct:", b7)
else:
    print("Result for 5! is incorrect:", b7)
b2.close()