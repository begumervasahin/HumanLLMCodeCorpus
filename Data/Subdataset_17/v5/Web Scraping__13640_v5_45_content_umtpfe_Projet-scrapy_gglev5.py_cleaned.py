from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException, WebDriverException
import time
def get_search_results(driver, url):
    while True:
        driver.get(url)
        while True:
            try:
                results = driver.find_elements(By.XPATH, '
                for result in results:
                    print(result.text)
                next_button = driver.find_element(By.XPATH, '
                next_button.click()
            except NoSuchElementException:
                handle_captcha(driver)
                break
            except TimeoutException:
                continue
def handle_captcha(driver):
    try:
        frame = driver.find_element(By.XPATH, '
        driver.switch_to.frame(frame)
        captcha_box = driver.find_element(By.XPATH, "
    except NoSuchElementException:
        pass
def setup_proxy():
    profile = webdriver.FirefoxProfile()
    driver = webdriver.Firefox(firefox_profile=profile)
    driver.get("https:
    tbody = driver.find_element(By.TAG_NAME, "tbody")
    rows = tbody.find_elements(By.TAG_NAME, "tr")
    for row in rows:
        columns = row.text.split()
        if len(columns) >= 2:
            host, port = columns[0], columns[1]
            configure_proxy(profile, host, port)
            break
    driver.quit()
    return profile
def configure_proxy(profile, host, port):
    profile.set_preference("network.proxy.type", 1)
    profile.set_preference("network.proxy.http", host)
    profile.set_preference("network.proxy.http_port", int(port))
    profile.set_preference("network.proxy.ssl", host)
    profile.set_preference("network.proxy.ssl_port", int(port))
def main():
    url = "http:
    profile = setup_proxy()
    driver = webdriver.Firefox(firefox_profile=profile)
    try:
        get_search_results(driver, url)
    finally:
        driver.quit()
if __name__ == "__main__":
    main()