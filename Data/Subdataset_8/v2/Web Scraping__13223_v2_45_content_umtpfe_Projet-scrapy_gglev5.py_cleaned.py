from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException, WebDriverException
import time
def switch_proxy(driver):
    profile = webdriver.FirefoxProfile()
    driver.quit()
    driver = webdriver.Firefox(firefox_profile=profile)
    driver.get("https:
    tbody = driver.find_element_by_tag_name("tbody")
    for row in tbody.find_elements_by_tag_name("tr"):
        host, port = row.text.split(" ")
        profile.set_preference("network.proxy.type", 1)
        profile.set_preference("network.proxy.http", host)
        profile.set_preference("network.proxy.http_port", int(port))
        profile.set_preference("network.proxy.ssl", host)
        profile.set_preference("network.proxy.ssl_port", int(port))
    driver.quit()
    driver = webdriver.Firefox(firefox_profile=profile)
    return driver
def main():
    while True:
        try:
            driver = webdriver.Firefox()
            url = "http:
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
                        driver = switch_proxy(driver)
                        time.sleep(30)
                        driver.switch_to.default_content()
                        continue
                    except NoSuchElementException:
                        break
        except (WebDriverException, TimeoutException) as e:
            print(f"Error occurred: {e}")
            driver.quit()
            continue
        finally:
            driver.quit()
if __name__ == "__main__":
    main()