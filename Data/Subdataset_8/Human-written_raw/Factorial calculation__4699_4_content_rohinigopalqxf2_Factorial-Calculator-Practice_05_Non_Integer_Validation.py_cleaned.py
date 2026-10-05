
import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https:
textbox_value = driver.find_element_by_id("number").send_keys('aa')
calculate_button = driver.find_element_by_xpath("
if(driver.find_element_by_xpath("
    print("Success -Factorial calculation failed for non-integer")
else:
    print("Failure - Factorial is calculated for non integer")
driver.close()