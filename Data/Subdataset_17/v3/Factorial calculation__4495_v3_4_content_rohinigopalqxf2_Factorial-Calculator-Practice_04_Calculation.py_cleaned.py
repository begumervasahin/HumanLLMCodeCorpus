
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
def setup_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver
def navigate_to_page(driver, url):
    driver.get(url)
def enter_text(driver, element_id, text):
    driver.find_element(By.ID, element_id).send_keys(text)
def click_button(driver, xpath):
    driver.find_element(By.XPATH, xpath).click()
def get_result_text(driver, xpath):
    return driver.find_element(By.XPATH, xpath).text
def main():
    driver = setup_driver()
    try:
        navigate_to_page(driver, 'https:
        enter_text(driver, 'number', '12')
        click_button(driver, "
        time.sleep(3)
        result_text = get_result_text(driver, "
        if result_text == "Please enter an integer":
            print("Failure - For integer value factorial calculation is failing")
        else:
            print("Success - For integer value factorial is calculated")
    finally:
        driver.quit()
if __name__ == "__main__":
    main()