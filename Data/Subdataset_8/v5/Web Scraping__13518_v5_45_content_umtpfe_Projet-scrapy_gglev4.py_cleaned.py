from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException, WebDriverException, ElementNotVisibleException
import time
driver = webdriver.Firefox()
search_url = "http:
while True:
    try:
        driver.get(search_url)
        continue_search = True
        while continue_search:
            try:
                search_results = driver.find_elements_by_xpath('
                for result in search_results:
                    print(result.text)
                next_button = driver.find_element_by_xpath('
                next_button.click()
            except (NoSuchElementException, ElementNotVisibleException, TimeoutException, WebDriverException) as e:
                print(f"Exception occurred: {type(e).__name__}")
            except Exception as e:
                print(f"Unhandled exception occurred: {type(e).__name__}")
                try:
                    captcha_frame = driver.find_element_by_xpath('
                    driver.switch_to.frame(captcha_frame)
                    captcha_checkbox = driver.find_element_by_xpath("
                    captcha_checkbox.click()
                    time.sleep(120)
                    driver.switch_to.default_content()
                except NoSuchElementException:
                    print("No CAPTCHA found.")
                except Exception as e:
                    print(f"Error handling CAPTCHA: {type(e).__name__}")
                continue_search = False
    except Exception as e:
        print(f"Unhandled exception outside loop: {type(e).__name__}")