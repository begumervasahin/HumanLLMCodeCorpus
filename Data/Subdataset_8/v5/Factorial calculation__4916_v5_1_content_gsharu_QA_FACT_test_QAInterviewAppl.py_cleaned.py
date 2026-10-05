import time
from selenium import webdriver
desired_capabilities = {
    'device': 'iPhone 7',
    'realMobile': 'true',
    'platform': 'iOS',
    'browserName': 'safari',
    'browserstack.debug': 'true'
}
USERNAME = 'your_username'
ACCESS_KEY = 'your_access_key'
command_executor = f'http:
driver = webdriver.Remote(command_executor=command_executor, desired_capabilities=desired_capabilities)
driver.get("https:
if driver.title == "Factoriall":
    print("Success: QA Interview Application page launched successfully")
else:
    print("Failure: QA Interview Application page title is incorrect")
number_input = driver.find_element_by_xpath("
number_input.send_keys('5')
calculate_button = driver.find_element_by_id('getFactorial')
calculate_button.click()
time.sleep(5)
result_element = driver.find_element_by_xpath("
result_text = result_element.text
result_value = float(result_text.split(':')[1].strip())
if result_value == 120:
    print("Result for 5! is correct:", result_value)
else:
    print("Result for 5! is incorrect:", result_value)
driver.close()