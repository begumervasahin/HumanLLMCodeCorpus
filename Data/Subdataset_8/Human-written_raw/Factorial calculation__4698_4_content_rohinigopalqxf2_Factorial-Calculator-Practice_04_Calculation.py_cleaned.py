
import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https:
textbox_value = driver.find_element_by_id("number").send_keys('12')
calculate_button = driver.find_element_by_xpath("
if(driver.find_element_by_xpath("
    print("Failure - For integer value factorial calculation is failing")
else:
    print("Success - For integer value factorial is calculated")
driver.close()