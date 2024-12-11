import time
from selenium import webdriver
def fonk1():
    b1 = webdriver.Chrome()
    b1.maximize_window()
    try:
        b1.get("https:
        b2 = 'aa'
        b3 = b1.find_element_by_id("number")
        b3.send_keys(b2)
        b4 = b1.find_element_by_xpath("
        b4.click()
        b5 = b1.find_element_by_xpath("
        if b5 = = "Please enter an integer":
            print("Success: Factorial calculation failed for non-integer input")
        else:
            print("Failure: Factorial is calculated for non-integer input")
    finally:
        b1.close()
if b6 = = "__main__":
    fonk1()