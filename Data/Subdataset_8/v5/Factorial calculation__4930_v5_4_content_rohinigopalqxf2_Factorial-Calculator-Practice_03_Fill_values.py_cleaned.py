
import time
from selenium import webdriver
def test_factorial_validation_message():
    driver = webdriver.Firefox()
    try:
        driver.get('https:
        textbox = driver.find_element_by_id("number")
        textbox.send_keys('12')
        calculate_button = driver.find_element_by_xpath("
        validation_result = driver.find_element_by_xpath("
        time.sleep(3)
        if validation_result.text != "Please enter an integer":
            print("Success: Message displayed successfully")
        else:
            print("Failed: Validation message is failing")
    finally:
        driver.quit()
if __name__ == "__main__":
    test_factorial_validation_message()