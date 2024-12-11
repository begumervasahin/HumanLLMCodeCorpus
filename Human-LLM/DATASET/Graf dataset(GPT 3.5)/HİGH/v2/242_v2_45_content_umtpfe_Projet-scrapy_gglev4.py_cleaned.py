from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException, WebDriverException, ElementNotVisibleException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
b1 = webdriver.Firefox()
b2 = "http:
while True:
    b1.get(b2)
    b3 = True
    while b3:
        try:
            b4 = b1.find_elements_by_xpath('
            for result in b4:
                print(result.text)
            b5 = b1.find_element_by_xpath('
            b5.click()
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
                b6 = b1.find_element_by_xpath('
                b1.switch_to.frame(b6)
                b7 = b1.find_element_by_xpath("
                b7.click()
                time.sleep(120)
                b1.switch_to.default_content()
                continue
            except:
                b3 = False