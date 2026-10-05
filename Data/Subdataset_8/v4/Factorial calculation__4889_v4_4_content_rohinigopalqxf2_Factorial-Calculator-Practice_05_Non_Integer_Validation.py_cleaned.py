
import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
try:
    driver.get("https:
    input_value = 'aa'
    textbox = driver.find_element_by_id("number")
    textbox.send_keys(input_value)
    calculate_button = driver.find_element_by_xpath("
    calculate_button.click()
    validation_message = driver.find_element_by_xpath("
    if validation_message == "Please enter an integer":
        print("Success: Factorial calculation failed for non-integer input")
    else:
        print("Failure: Factorial is calculated for non-integer input")
finally:
    driver.close()