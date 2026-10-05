import time
from selenium import webdriver
def test_factorial_calculation():
    driver = webdriver.Chrome()
    driver.maximize_window()
    try:
        driver.get("https:
        input_box = driver.find_element_by_id("number")
        input_box.send_keys('12')
        calculate_button = driver.find_element_by_xpath("
        calculate_button.click()
        validation_message = driver.find_element_by_xpath("
        if validation_message == "Please enter an integer":
            print("Failure: Factorial calculation failed for integer value")
        else:
            print("Success: Factorial calculated successfully")
    finally:
        driver.quit()
if __name__ == "__main__":
    test_factorial_calculation()