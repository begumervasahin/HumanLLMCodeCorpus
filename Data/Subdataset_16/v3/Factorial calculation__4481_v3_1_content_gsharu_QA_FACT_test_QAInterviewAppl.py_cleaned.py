
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
        b5 = b3.find_element(By.ID, 'number')
        b5.send_keys('5')
        b6 = b3.find_element(By.ID, 'getFactorial')
        b6.click()
        time.sleep(5)
        b7 = b3.find_element(By.ID, 'resultDiv').text
        b8 = int(b7.split(':')[1].strip())
        if b8 = = 120:
            print(f"Success: Result for 5! is correct: {b8}")
        else:
            print(f"Failure: Result for 5! is incorrect: {b8}")
    finally:
        b3.quit()
if b9 = = "__main__":
    fonk2()