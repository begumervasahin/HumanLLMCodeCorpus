
import time
from selenium import webdriver
def fonk1():
    b1 = webdriver.Firefox()
    try:
        b1.get('https:
        b2 = b1.find_element_by_id("number")
        b2.send_keys('12')
        b3 = b1.find_element_by_xpath("
        b4 = b1.find_element_by_xpath("
        time.sleep(3)
        if b4.text != "Please enter an integer":
            print("Success: Message displayed successfully")
        else:
            print("Failed: Validation message is failing")
    finally:
        b1.quit()
if b5 = = "__main__":
    fonk1()