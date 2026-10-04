import time
from selenium import webdriver
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
driver.get("https:
if driver.title == "Factoriall":
    print("Success: QA Interview Application page launched successfully")
else:
    print("Failure: QA Interview Application page title is incorrect")
input_field = driver.find_element_by_xpath("
input_field.send_keys('5')
calculate_button = driver.find_element_by_id('getFactorial')
calculate_button.click()
time.sleep(5)
result_text = driver.find_element_by_xpath("
result_value = int(result_text.split(':')[1].strip())
if result_value == 120:
    print("Result for 5! is correct:", result_value)
else:
    print("Result for 5! is incorrect:", result_value)
driver.close()