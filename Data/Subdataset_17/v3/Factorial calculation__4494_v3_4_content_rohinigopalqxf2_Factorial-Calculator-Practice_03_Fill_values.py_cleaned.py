
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
URL = 'https:
TEXTBOX_ID = 'number'
CALCULATE_BUTTON_XPATH = "
RESULT_XPATH = "
EXPECTED_RESULT = "The factorial of 12 is: 479001600"
def setup_driver():
    return webdriver.Firefox()
def navigate_to_page(driver, url):
    driver.get(url)
def enter_text(driver, element_id, text):
    driver.find_element(By.ID, element_id).send_keys(text)
def click_button(driver, xpath):
    driver.find_element(By.XPATH, xpath).click()
def get_validation_result(driver, xpath):
    return driver.find_element(By.XPATH, xpath).text
def main():
    driver = setup_driver()
    try:
        navigate_to_page(driver, URL)
        enter_text(driver, TEXTBOX_ID, '12')
        click_button(driver, CALCULATE_BUTTON_XPATH)
        time.sleep(3)
        validation_result = get_validation_result(driver, RESULT_XPATH)
        if validation_result == EXPECTED_RESULT:
            print("Success: Message displayed successfully")
        else:
            print("Failed: Validation message is incorrect")
    finally:
        driver.quit()
if __name__ == "__main__":
    main()