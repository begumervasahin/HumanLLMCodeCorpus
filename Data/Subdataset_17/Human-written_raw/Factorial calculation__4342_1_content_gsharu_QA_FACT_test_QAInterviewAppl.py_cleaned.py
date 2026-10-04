
import time
from selenium import webdriver
desired_cap = { 'device': 'iPhone 7','realMobile': 'true', 'platform': 'iOS','browserName': 'safari', 'browserstack.debug': 'true' }
driver = webdriver.Remote(command_executor='http:
driver.get("https:
if(driver.title=="Factoriall"):
    print ("Success: QA Interview Application page launched successfully")
else:
    print ("Failure: QA Interview Application page Title is incorrect")
driver.find_element_by_xpath("
driver.find_element_by_id('getFactorial').click()
time.sleep(5)
result = float((driver.find_element_by_xpath("
if ( result == 120):
    print("Result for 5! is correct:",result)
else:
    print("Result for 5! is incorrect:",result)
driver.close()