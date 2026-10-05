
import time
from selenium import webdriver
b1 = webdriver.Chrome()
b1.maximize_window()
b1.get("https:
b2 = b1.find_element_by_id("number").send_keys('12')
b3 = b1.find_element_by_xpath("
if(b1.find_element_by_xpath("
    print("Failure - For integer value factorial calculation is failing")
else:
    print("Success - For integer value factorial is calculated")
b1.close()