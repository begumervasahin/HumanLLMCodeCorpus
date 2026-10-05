import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
proxy_dict = {
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
def change_proxy(proxy_value):
    print("Attempting to change proxy...")
    proxy_info = proxy_dict[proxy_value].split(':')
    return proxy_info
def main():
    profile = webdriver.FirefoxProfile()
    driver = webdriver.Firefox(firefox_profile=profile)
    url = "http:
    driver.get(url)
    while True:
        driver.get(url)
        val = True
        while val:
            try:
                results = driver.find_elements_by_xpath('
                for result in results:
                    print(result.text)
                next_button = driver.find_element_by_xpath('
                next_button.click()
            except NoSuchElementException:
                try:
                    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '
                except:
                    try:
                        print("Captcha encountered.")
                        frame = driver.find_element_by_xpath('
                        driver.switch_to.frame(frame)
                        driver.find_element_by_xpath("
                        driver.switch_to.default_content()
                        time.sleep(10)
                        driver.switch_to.default_content()
                        try:
                            print("Attempting to change proxy...")
                            proxy_info = change_proxy(i)
                            print("Changing proxy...")
                            profile = webdriver.FirefoxProfile()
                            profile.set_preference("network.proxy.type", 1)
                            profile.set_preference("network.proxy.https", proxy_info[0])
                            profile.set_preference("network.proxy.https_port", int(proxy_info[1]))
                            profile.set_preference("network.proxy.ssl", proxy_info[0])
                            profile.set_preference("network.proxy.ssl_port", int(proxy_info[1]))
                            profile.set_preference("general.useragent.override", "whatever_useragent")
                            profile.set_preference("network.proxy.socks_version", 5)
                            profile.update_preferences()
                            print("Proxy changed.")
                            driver = webdriver.Firefox(firefox_profile=profile)
                            time.sleep(10)
                            i += 1
                        except:
                            print('Continuing...')
                    except:
                        try:
                            wait = WebDriverWait(driver, 10)
                            next_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'td.b:nth-child(12) > a:nth-child(1) > span:nth-child(2)')))
                            next_button.click()
                        except:
                            val = False
if __name__ == "__main__":
    main()