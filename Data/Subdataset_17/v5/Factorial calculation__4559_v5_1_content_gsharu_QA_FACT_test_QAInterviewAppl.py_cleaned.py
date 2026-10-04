import time
from selenium import webdriver
def setup_driver():
    desired_cap = {
        'device': 'iPhone 7',
        'realMobile': 'true',
        'platform': 'iOS',
        'browserName': 'safari',
        'browserstack.debug': 'true'
    }
    driver = webdriver.Remote(
        command_executor='http:
        desired_capabilities=desired_cap
    )
    return driver
def open_application(driver, url):
    driver.get(url)
    if driver.title == "Factoriall":
        print("Success: QA Interview Application page launched successfully")
    else:
        print("Failure: QA Interview Application page title is incorrect")
def calculate_factorial(driver, number):
    input_field = driver.find_element_by_xpath("
    input_field.send_keys(str(number))
    calculate_button = driver.find_element_by_id('getFactorial')
    calculate_button.click()
    time.sleep(5)
    result_text = driver.find_element_by_xpath("
    result_value = int(result_text.split(':')[1].strip())
    return result_value
def main():
    driver = setup_driver()
    try:
        open_application(driver, "https:
        result = calculate_factorial(driver, 5)
        if result == 120:
            print("Result for 5! is correct:", result)
        else:
            print("Result for 5! is incorrect:", result)
    finally:
        driver.close()
if __name__ == "__main__":
    main()