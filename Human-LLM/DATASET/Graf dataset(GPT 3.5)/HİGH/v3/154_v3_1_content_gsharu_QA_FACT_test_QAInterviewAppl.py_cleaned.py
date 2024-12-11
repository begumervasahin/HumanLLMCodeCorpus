import time
from selenium import webdriver
b1 = 'USERNAME'
b2 = 'ACCESS_KEY'
b3 = {
    'device': 'iPhone 7',
    'realMobile': 'true',
    'platform': 'iOS',
    'browserName': 'safari',
    'browserstack.debug': 'true'
}
b4 = f'http:
b5 = webdriver.Remote(b4=b4, desired_capabilities=b3)
b5.get("https:
b6 = "Factoriall"
if b5.b7 = = b6:
    print(f"Success: QA Interview Application page launched successfully with b7 '{b6}'")
else:
    print(f"Failure: QA Interview Application page b7 is incorrect, expected '{b6}'")
b8 = b5.find_element_by_xpath("
b8.send_keys('5')
b9 = b5.find_element_by_id('getFactorial')
b9.click()
time.sleep(5)
b10 = b5.find_element_by_xpath("
b11 = b10.text
b12 = float(b11.split(':')[1].strip())
a1 = 120
if b12 = = a1:
    print(f"Result for 5! is correct: {b12}")
else:
    print(f"Result for 5! is incorrect, expected: {a1}, actual: {b12}")
b5.close()