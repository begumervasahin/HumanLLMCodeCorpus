import time
from selenium import webdriver
def test_non_integer_factorial_calculation():
    driver = webdriver.Chrome()
    driver.maximize_window()
    try:
        driver.get("https:
        input_value = 'aa'
        input_box = driver.find_element_by_id("number")
        input_box.send_keys(input_value)
        calculate_button = driver.find_element_by_xpath("
        calculate_button.click()
        validation_message = driver.find_element_by_xpath("
        if validation_message == "Please enter an integer":
            print("Success: Factorial calculation failed for non-integer input")
        else:
            print("Failure: Factorial is calculated for non-integer input")
    finally:
        driver.close()
if __name__ == "__main__":
    test_non_integer_factorial_calculation()