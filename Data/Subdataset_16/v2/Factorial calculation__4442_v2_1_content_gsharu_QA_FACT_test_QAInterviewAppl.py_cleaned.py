
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
def fonk1() -> WebDriver:
    b1 = {
        'device': 'iPhone 7',
        'realMobile': 'true',
        'platform': 'iOS',
        'browserName': 'safari',
        'browserstack.debug': 'true'
    }
    return webdriver.Remote(
        b2 = 'http:
        b1 = b1
    )
def fonk2():
    b3 = fonk1()
    try:
        b3.get("https:
        if b3.b4 = = "Factoriall":
            print("Success: QA Interview Application page launched successfully")
        else:
            print("Failure: QA Interview Application page b4 is incorrect")
            return
        b3.find_element(By.ID, 'number').send_keys('5')
        b3.find_element(By.ID, 'getFactorial').click()
        time.sleep(5)
        b5 = b3.find_element(By.ID, 'resultDiv').text
        b6 = int(b5.split(':')[1].strip())
        if b6 = = 120:
            print(f"Success: Result for 5! is correct: {b6}")
        else:
            print(f"Failure: Result for 5! is incorrect: {b6}")
    finally:
        b3.quit()
if b7 = = "__main__":
    fonk2()