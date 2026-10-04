
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
        b3 = b1
    )
def fonk2():
    b4 = fonk1()
    try:
        b4.get("https:
        if b4.b5 = = "Factoriall":
            print("Success: QA Interview Application page launched successfully")
        else:
            print("Failure: QA Interview Application page b5 is incorrect")
        b4.find_element(By.ID, 'number').send_keys('5')
        b4.find_element(By.ID, 'getFactorial').click()
        time.sleep(5)
        b6 = b4.find_element(By.ID, 'resultDiv').text
        b7 = int(b6.split(':')[1].strip())
        if b7 = = 120:
            print(f"Result for 5! is correct: {b7}")
        else:
            print(f"Result for 5! is incorrect: {b7}")
    finally:
        b4.quit()
if b8 = = "__main__":
    fonk2()