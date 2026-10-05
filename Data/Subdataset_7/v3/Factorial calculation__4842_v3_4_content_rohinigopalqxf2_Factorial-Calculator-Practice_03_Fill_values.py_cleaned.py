import time
from selenium import webdriver
def fonk1():
    try:
        b1 = webdriver.Firefox()
        b1.get('https:
        b2 = '12'
        b3 = b1.find_element_by_id("number")
        b3.send_keys(b2)
        b4 = b1.find_element_by_xpath("
        b4.click()
        b5 = b1.find_element_by_xpath("
        time.sleep(3)
        b6 = "Please enter an integer"
        if b5.text != b6:
            print(f"Success: Validation message '{b6}' not displayed.")
        else:
            print("Failed: Validation message is not correct.")
    finally:
        b1.quit()
if b7 = = "__main__":
    fonk1()