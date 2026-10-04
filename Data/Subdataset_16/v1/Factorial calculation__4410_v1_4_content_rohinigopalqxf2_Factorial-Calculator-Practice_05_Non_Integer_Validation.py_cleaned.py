
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
def fonk1():
    b1 = webdriver.Chrome()
    b1.maximize_window()
    return b1
def fonk2(b1, url):
    b1.get(url)
def fonk3(b1, element_id, text):
    b1.find_element(By.ID, element_id).send_keys(text)
def fonk4(b1, xpath):
    b1.find_element(By.XPATH, xpath).click()
def fonk5(b1, xpath):
    return b1.find_element(By.XPATH, xpath).text
def fonk6():
    b1 = fonk1()
    try:
        fonk2(b1, 'https:
        fonk3(b1, 'number', 'aa')
        fonk4(b1, "
        time.sleep(3)
        b2 = fonk5(b1, "
        if b2 = = "Please enter an integer":
            print("Success - Factorial calculation failed for non-integer")
        else:
            print("Failure - Factorial is calculated for non-integer")
    finally:
        b1.quit()
if b3 = = "__main__":
    fonk6()