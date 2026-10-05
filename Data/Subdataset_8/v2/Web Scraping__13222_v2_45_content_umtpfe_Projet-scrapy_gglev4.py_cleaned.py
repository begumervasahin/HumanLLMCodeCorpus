from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException, WebDriverException, ElementNotVisibleException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
driver = webdriver.Firefox()
search_url = "http:
while True:
    driver.get(search_url)
    continue_search = True
    while continue_search:
        try:
            search_results = driver.find_elements_by_xpath('
            for result in search_results:
                print(result.text)
            next_button = driver.find_element_by_xpath('
            next_button.click()
        except NoSuchElementException:
            print("No such element found.")
        except ElementNotVisibleException:
            print("Element not visible.")
        except TimeoutException:
            print("Timeout occurred.")
        except WebDriverException:
            print("WebDriver exception occurred.")
        except:
            try:
                captcha_frame = driver.find_element_by_xpath('
                driver.switch_to.frame(captcha_frame)
                captcha_checkbox = driver.find_element_by_xpath("
                captcha_checkbox.click()
                time.sleep(120)
                driver.switch_to.default_content()
                continue
            except:
                continue_search = False