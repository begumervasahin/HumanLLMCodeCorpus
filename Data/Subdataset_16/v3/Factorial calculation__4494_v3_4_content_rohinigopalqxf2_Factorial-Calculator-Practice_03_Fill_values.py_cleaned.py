
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
b1 = 'https:
b2 = 'number'
b3 = "
b4 = "
b5 = "The factorial of 12 is: 479001600"
def fonk1():
    return webdriver.Firefox()
def fonk2(b6, url):
    b6.get(url)
def fonk3(b6, element_id, text):
    b6.find_element(By.ID, element_id).send_keys(text)
def fonk4(b6, xpath):
    b6.find_element(By.XPATH, xpath).click()
def fonk5(b6, xpath):
    return b6.find_element(By.XPATH, xpath).text
def fonk6():
    b6 = fonk1()
    try:
        fonk2(b6, b1)
        fonk3(b6, b2, '12')
        fonk4(b6, b3)
        time.sleep(3)
        b7 = fonk5(b6, b4)
        if b7 = = b5:
            print("Success: Message displayed successfully")
        else:
            print("Failed: Validation message is incorrect")
    finally:
        b6.quit()
if b8 = = "__main__":
    fonk6()