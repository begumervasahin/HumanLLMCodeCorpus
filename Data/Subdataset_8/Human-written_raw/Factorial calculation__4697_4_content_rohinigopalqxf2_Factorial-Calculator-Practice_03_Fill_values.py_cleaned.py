
import time
from selenium import webdriver
driver = webdriver.Firefox()
driver.get('https:
textbox_value = driver.find_element_by_id("number").send_keys('12')
calculate_button = driver.find_element_by_xpath("
validation_result = driver.find_element_by_xpath("
time.sleep(3)
if(validation_result.text !="Please enter an integer"):
    print ("Success: Message displayed successfully")
else:
    print ("Failed: Validation message is failing")
driver.quit()