
import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
try:
    driver.get("https:
    textbox_value = driver.find_element_by_id("number").send_keys('12')
    calculate_button = driver.find_element_by_xpath("
    validation_message = driver.find_element_by_xpath("
    if validation_message == "Please enter an integer":
        print("Failure: Factorial calculation failed for integer value")
    else:
        print("Success: Factorial calculated successfully")
finally:
    driver.close()