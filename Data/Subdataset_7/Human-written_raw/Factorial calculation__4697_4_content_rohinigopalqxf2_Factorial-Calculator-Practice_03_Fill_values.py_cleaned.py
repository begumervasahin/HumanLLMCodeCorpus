
import time
from selenium import webdriver
b1 = webdriver.Firefox()
b1.get('https:
b2 = b1.find_element_by_id("number").send_keys('12')
b3 = b1.find_element_by_xpath("
b4 = b1.find_element_by_xpath("
time.sleep(3)
if(b4.text !="Please enter an integer"):
    print ("Success: Message displayed successfully")
else:
    print ("Failed: Validation message is failing")
b1.quit()