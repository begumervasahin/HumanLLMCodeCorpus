import time
from selenium import webdriver
def test_non_integer_factorial_calculation():
    driver = webdriver.Chrome()
    driver.maximize_window()
    try:
        driver.get("https:
        input_box = driver.find_element_by_id("number")
        input_box.send_keys('aa')
        calculate_button = driver.find_element_by_xpath("
        calculate_button.click()
        validation_message = driver.find_element_by_xpath("
        if validation_message == "Please enter an integer":
            print("Success: Factorial calculation failed for non-integer input")
        else:
            print("Failure: Factorial calculation succeeded for non-integer input")
    finally:
        driver.quit()
if __name__ == "__main__":
    test_non_integer_factorial_calculation()