
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
def fonk1():
    return webdriver.Firefox()
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
        fonk3(b1, 'number', '12')
        fonk4(b1, "
        time.sleep(3)
        b2 = fonk5(b1, "
        b3 = "The factorial of 12 is: 479001600"
        if b2 = = b3:
            print("Success: Message displayed successfully")
        else:
            print("Failed: Validation message is incorrect")
    finally:
        b1.quit()
if b4 = = "__main__":
    fonk6()