from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException, WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
def fonk1(b2):
    b1 = webdriver.FirefoxProfile()
    b2.quit()
    b2 = webdriver.Firefox(firefox_profile=b1)
    b2.get("https:
    b3 = b2.find_element_by_tag_name("b3")
    b4 = b3.find_elements_by_tag_name("tr")
    for b5 in b4:
        b5 = b5.text.split(" ")
        b6 = b5[0]
        b7 = b5[1]
        b1.set_preference("network.proxy.type", 1)
        b1.set_preference("network.proxy.http", b6)
        b1.set_preference("network.proxy.http_port", int(b7))
        b1.set_preference("network.proxy.ssl", b6)
        b1.set_preference("network.proxy.ssl_port", int(b7))
    b2.quit()
    b2 = webdriver.Firefox(firefox_profile=b1)
    return b2
def fonk2():
    while True:
        try:
            b2 = webdriver.Firefox()
            b8 = "http:
            b2.get(b8)
            while True:
                try:
                    b9 = b2.find_elements_by_xpath('
                    for result in b9:
                        print(result.text)
                    b10 = b2.find_element_by_xpath('
                    b10.click()
                except NoSuchElementException:
                    try:
                        b11 = b2.find_element_by_xpath('
                        b2.switch_to.b11(b11)
                        b2.find_element_by_xpath("
                        b2 = fonk1(b2)
                        time.sleep(30)
                        b2.switch_to.default_content()
                        continue
                    except NoSuchElementException:
                        break
        except (WebDriverException, TimeoutException) as e:
            print(f"Error occurred: {e}")
            b2.quit()
            continue
        finally:
            b2.quit()
if b12 = = "__main__":
    fonk2()