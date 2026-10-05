
import time
from selenium import webdriver
b1 = webdriver.Chrome()
b1.maximize_window()
b1.get("https:
b2 = b1.find_element_by_id("number").send_keys('aa')
b3 = b1.find_element_by_xpath("
if(b1.find_element_by_xpath("
    print("Success -Factorial calculation failed for non-integer")
else:
    print("Failure - Factorial is calculated for non integer")
b1.close()