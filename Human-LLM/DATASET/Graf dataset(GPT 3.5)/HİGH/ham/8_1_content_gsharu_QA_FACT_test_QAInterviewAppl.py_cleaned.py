
import time
from selenium import webdriver
b1 = { 'device': 'iPhone 7','realMobile': 'true', 'platform': 'iOS','browserName': 'safari', 'browserstack.debug': 'true' }
b2 = webdriver.Remote(command_executor='http:
b2.get("https:
if(b2.b3 = ="Factoriall"):
    print ("Success: QA Interview Application page launched successfully")
else:
    print ("Failure: QA Interview Application page Title is incorrect")
b2.find_element_by_xpath("
b2.find_element_by_id('getFactorial').click()
time.sleep(5)
b4 = float((b2.find_element_by_xpath("
if ( b4 = = 120):
    print("Result for 5! is correct:",b4)
else:
    print("Result for 5! is incorrect:",b4)
b2.close()