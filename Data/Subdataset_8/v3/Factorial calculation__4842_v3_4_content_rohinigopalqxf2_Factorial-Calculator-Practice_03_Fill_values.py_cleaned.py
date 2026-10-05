import time
from selenium import webdriver
def test_factorial_validation_message():
    try:
        driver = webdriver.Firefox()
        driver.get('https:
        input_number = '12'
        textbox = driver.find_element_by_id("number")
        textbox.send_keys(input_number)
        calculate_button = driver.find_element_by_xpath("
        calculate_button.click()
        validation_result = driver.find_element_by_xpath("
        time.sleep(3)
        expected_message = "Please enter an integer"
        if validation_result.text != expected_message:
            print(f"Success: Validation message '{expected_message}' not displayed.")
        else:
            print("Failed: Validation message is not correct.")
    finally:
        driver.quit()
if __name__ == "__main__":
    test_factorial_validation_message()