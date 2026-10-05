
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, TimeoutException, WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
driver = webdriver.Firefox()
url = "http:
while True:
    try:
        driver.get(url)
        while True:
            try:
                results = driver.find_elements_by_xpath('
                for result in results:
                    print(result.text)
                next_button = driver.find_element_by_xpath('
                next_button.click()
            except NoSuchElementException:
                try:
                    frame = driver.find_element_by_xpath('
                    driver.switch_to.frame(frame)
                    driver.find_element_by_xpath("
                    profile = webdriver.FirefoxProfile()
                    driver = webdriver.Firefox(firefox_profile=profile)
                    driver.get("https:
                    tbody = driver.find_element_by_tag_name("tbody")
                    cell = tbody.find_elements_by_tag_name("tr")
                    for column in cell:
                        column = column.text.split(" ")
                        host = column[0]
                        port = column[1]
                        profile.set_preference("network.proxy.type", 1)
                        profile.set_preference("network.proxy.http", host)
                        profile.set_preference("network.proxy.http_port", int(port))
                        profile.set_preference("network.proxy.ssl", host)
                        profile.set_preference("network.proxy.ssl_port", int(port))
                    driver.quit()
                    driver = webdriver.Firefox(firefox_profile=profile)
                    time.sleep(30)
                    driver.switch_to.default_content()
                    continue
                except NoSuchElementException:
                    break
    except (TimeoutException, WebDriverException) as e:
        print("An error occurred:", e)
        break
driver.quit()