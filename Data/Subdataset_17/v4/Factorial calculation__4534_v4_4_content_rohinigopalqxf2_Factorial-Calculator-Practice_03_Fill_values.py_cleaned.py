
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
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
        navigate_to_page(driver, 'https:
        enter_text(driver, 'number', '12')
        click_button(driver, "
        time.sleep(3)
        validation_result = get_validation_result(driver, "
        expected_result = "The factorial of 12 is: 479001600"
        if validation_result == expected_result:
            print("Success: Message displayed successfully")
        else:
            print("Failed: Validation message is incorrect")
    finally:
        driver.quit()
if __name__ == "__main__":
    main()