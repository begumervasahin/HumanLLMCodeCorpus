from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
dicoProxy = {
    0: "34.244.2.233:8123",
    1: "85.93.47.137:8080",
    2: "46.63.162.171:8080",
    3: "138.197.180.57:3128",
    4: "85.30.219.120:46761",
    5: "85.15.189.121:41033",
    6: "103.57.21.30:53281",
    7: "103.76.188.209:34424",
    8: "103.89.253.246:3128",
    9: "105.30.17.3:53281"
}
def change_proxy(index):
    print("Changing proxy...")
    proxy = dicoProxy[index].split(':')
    profile = webdriver.FirefoxProfile()
    profile.set_preference("network.proxy.type", 1)
    profile.set_preference("network.proxy.http", proxy[0])
    profile.set_preference("network.proxy.http_port", int(proxy[1]))
    profile.set_preference("network.proxy.ssl", proxy[0])
    profile.set_preference("network.proxy.ssl_port", int(proxy[1]))
    profile.update_preferences()
    return webdriver.Firefox(firefox_profile=profile)
def main():
    i = 0
    url = "http:
    driver = webdriver.Firefox()
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
                driver.switch_to.default_content()
                time.sleep(10)
                driver.switch_to.default_content()
                driver.quit()
                i += 1
                driver = change_proxy(i)
                time.sleep(10)
            except NoSuchElementException:
                print("No CAPTCHA found.")
            except TimeoutException:
                print("Timeout occurred.")
                break
            except Exception as e:
                print("An error occurred:", str(e))
                break
if __name__ == "__main__":
    main()