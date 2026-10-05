import time
from selenium import webdriver
def test_factorial_calculation():
    driver = webdriver.Chrome()
    driver.maximize_window()
    try:
        driver.get("https:
        textbox = driver.find_element_by_id("number")
        textbox.send_keys('12')
        calculate_button = driver.find_element_by_xpath("
        time.sleep(2)
        result_element = driver.find_element_by_xpath("
        factorial_result = result_element.text
        if factorial_result != "Please enter an integer":
            print("Success: Factorial calculated successfully")
            print("Factorial Value:", factorial_result)
        else:
            print("Failed: For integer value, factorial calculation is failing")
    finally:
        driver.quit()
if __name__ == "__main__":
    test_factorial_calculation()