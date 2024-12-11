import time
from selenium import webdriver
def fonk1():
    b1 = webdriver.Chrome()
    b1.maximize_window()
    try:
        b1.get("https:
        b2 = b1.find_element_by_id("number")
        b2.send_keys('12')
        b3 = b1.find_element_by_xpath("
        b3.click()
        b4 = b1.find_element_by_xpath("
        if b4 = = "Please enter an integer":
            print("Failure: Factorial calculation failed for integer value")
        else:
            print("Success: Factorial calculated successfully")
    finally:
        b1.quit()
if b5 = = "__main__":
    fonk1()