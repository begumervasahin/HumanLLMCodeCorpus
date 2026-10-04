
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
b1 = 'https:
b2 = 'number'
b3 = "
b4 = "
b5 = "The factorial of 12 is: 479001600"
def fonk1():
    b6 = webdriver.Firefox()
    try:
        b6.get(b1)
        b6.find_element(By.ID, b2).send_keys('12')
        b6.find_element(By.XPATH, b3).click()
        time.sleep(3)
        b7 = b6.find_element(By.XPATH, b4).text
        if b7 = = b5:
            print("Success: Message displayed successfully")
        else:
            print("Failed: Validation message is incorrect")
    finally:
        b6.quit()
if b8 = = "__main__":
    fonk1()