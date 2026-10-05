from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import TimeoutException, WebDriverException
import time
import threading
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
        except :
            try:
                b6 = b1.find_element_by_xpath('
                b1.switch_to.b6(b6)
                b1.find_element_by_xpath("
                b7 = webdriver.FirefoxProfile()
                b1 = webdriver.Firefox(firefox_profile=b7)
                b1.get("https:
                b8 = b1.find_element_by_tag_name("b8")
                b9 = b8.find_elements_by_tag_name("tr")
                for b10 in b9:
                    b10 = b10.text.split(" ")
                    b11 = b10[0]
                    b12 = b10[1]
                    b7.set_preference("network.proxy.type", 1)
                    b7.set_preference("network.proxy.http", b11)
                    b7.set_preference("network.proxy.http_port", int(b12) )
                    b7.set_preference("network.proxy.ssl", b11)
                    b7.set_preference("network.proxy.ssl_port", int(b12) )
                b1.quit()
                b1 = webdriver.Firefox(firefox_profile=b7)
                time.sleep(30)
                b1.switch_to.default_content()
                continue
            except:
                b3 = False