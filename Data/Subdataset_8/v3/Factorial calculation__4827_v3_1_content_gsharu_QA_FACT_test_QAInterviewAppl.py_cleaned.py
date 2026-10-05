import time
from selenium import webdriver
username = 'USERNAME'
access_key = 'ACCESS_KEY'
desired_cap = {
    'device': 'iPhone 7',
    'realMobile': 'true',
    'platform': 'iOS',
    'browserName': 'safari',
    'browserstack.debug': 'true'
}
command_executor = f'http:
driver = webdriver.Remote(command_executor=command_executor, desired_capabilities=desired_cap)
driver.get("https:
expected_title = "Factoriall"
if driver.title == expected_title:
    print(f"Success: QA Interview Application page launched successfully with title '{expected_title}'")
else:
    print(f"Failure: QA Interview Application page title is incorrect, expected '{expected_title}'")
number_input = driver.find_element_by_xpath("
number_input.send_keys('5')
calculate_button = driver.find_element_by_id('getFactorial')
calculate_button.click()
time.sleep(5)
result_element = driver.find_element_by_xpath("
result_text = result_element.text
result_value = float(result_text.split(':')[1].strip())
expected_result = 120
if result_value == expected_result:
    print(f"Result for 5! is correct: {result_value}")
else:
    print(f"Result for 5! is incorrect, expected: {expected_result}, actual: {result_value}")
driver.close()