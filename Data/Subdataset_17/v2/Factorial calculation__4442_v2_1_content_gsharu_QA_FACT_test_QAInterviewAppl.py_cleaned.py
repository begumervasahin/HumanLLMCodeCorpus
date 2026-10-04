
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
def create_driver() -> WebDriver:
    desired_capabilities = {
        'device': 'iPhone 7',
        'realMobile': 'true',
        'platform': 'iOS',
        'browserName': 'safari',
        'browserstack.debug': 'true'
    }
    return webdriver.Remote(
        command_executor='http:
        desired_capabilities=desired_capabilities
    )
def main():
    driver = create_driver()
    try:
        driver.get("https:
        if driver.title == "Factoriall":
            print("Success: QA Interview Application page launched successfully")
        else:
            print("Failure: QA Interview Application page title is incorrect")
            return
        driver.find_element(By.ID, 'number').send_keys('5')
        driver.find_element(By.ID, 'getFactorial').click()
        time.sleep(5)
        result_text = driver.find_element(By.ID, 'resultDiv').text
        result_value = int(result_text.split(':')[1].strip())
        if result_value == 120:
            print(f"Success: Result for 5! is correct: {result_value}")
        else:
            print(f"Failure: Result for 5! is incorrect: {result_value}")
    finally:
        driver.quit()
if __name__ == "__main__":
    main()