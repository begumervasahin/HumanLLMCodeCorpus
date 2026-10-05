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
        time.sleep(2)
        b4 = b1.find_element_by_xpath("
        b5 = b4.text
        if b5 != "Please enter an integer":
            print("Success: Factorial calculated successfully")
            print("Factorial Value:", b5)
        else:
            print("Failed: For integer value, factorial calculation is failing")
    finally:
        b1.quit()
if b6 = = "__main__":
    fonk1()