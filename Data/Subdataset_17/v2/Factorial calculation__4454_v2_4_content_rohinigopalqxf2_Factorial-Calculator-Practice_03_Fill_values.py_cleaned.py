
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
URL = 'https:
TEXTBOX_ID = 'number'
CALCULATE_BUTTON_XPATH = "
RESULT_XPATH = "
EXPECTED_RESULT = "The factorial of 12 is: 479001600"
def main():
    driver = webdriver.Firefox()
    try:
        driver.get(URL)
        driver.find_element(By.ID, TEXTBOX_ID).send_keys('12')
        driver.find_element(By.XPATH, CALCULATE_BUTTON_XPATH).click()
        time.sleep(3)
        validation_result = driver.find_element(By.XPATH, RESULT_XPATH).text
        if validation_result == EXPECTED_RESULT:
            print("Success: Message displayed successfully")
        else:
            print("Failed: Validation message is incorrect")
    finally:
        driver.quit()
if __name__ == "__main__":
    main()