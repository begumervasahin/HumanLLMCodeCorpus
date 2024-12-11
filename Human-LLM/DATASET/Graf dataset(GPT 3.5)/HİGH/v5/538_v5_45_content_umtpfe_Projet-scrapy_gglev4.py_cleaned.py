from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException, WebDriverException, ElementNotVisibleException
import time
b1 = webdriver.Firefox()
b2 = "http:
while True:
    try:
        b1.get(b2)
        b3 = True
        while b3:
            try:
                b4 = b1.find_elements_by_xpath('
                for result in b4:
                    print(result.text)
                b5 = b1.find_element_by_xpath('
                b5.click()
            except (NoSuchElementException, ElementNotVisibleException, TimeoutException, WebDriverException) as e:
                print(f"Exception occurred: {type(e).__name__}")
            except Exception as e:
                print(f"Unhandled exception occurred: {type(e).__name__}")
                try:
                    b6 = b1.find_element_by_xpath('
                    b1.switch_to.frame(b6)
                    b7 = b1.find_element_by_xpath("
                    b7.click()
                    time.sleep(120)
                    b1.switch_to.default_content()
                except NoSuchElementException:
                    print("No CAPTCHA found.")
                except Exception as e:
                    print(f"Error handling CAPTCHA: {type(e).__name__}")
                b3 = False
    except Exception as e:
        print(f"Unhandled exception outside loop: {type(e).__name__}")