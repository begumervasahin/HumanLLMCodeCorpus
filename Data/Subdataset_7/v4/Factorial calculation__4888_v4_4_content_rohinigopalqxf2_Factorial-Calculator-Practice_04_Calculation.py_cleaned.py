
import time
from selenium import webdriver
b1 = webdriver.Chrome()
b1.maximize_window()
try:
    b1.get("https:
    b2 = b1.find_element_by_id("number").send_keys('12')
    b3 = b1.find_element_by_xpath("
    b4 = b1.find_element_by_xpath("
    if b4 = = "Please enter an integer":
        print("Failure: Factorial calculation failed for integer value")
    else:
        print("Success: Factorial calculated successfully")
finally:
    b1.close()