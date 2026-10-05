from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
b1 = {
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
def fonk1(proxy_index):
    print("Changing proxy...")
    b2 = b1[proxy_index].split(':')
    b3 = webdriver.FirefoxProfile()
    b3.set_preference("network.proxy.type", 1)
    b3.set_preference("network.proxy.http", b2[0])
    b3.set_preference("network.proxy.http_port", int(b2[1]))
    b3.set_preference("network.proxy.ssl", b2[0])
    b3.set_preference("network.proxy.ssl_port", int(b2[1]))
    b3.update_preferences()
    return webdriver.Firefox(b4 = b3)
def fonk2():
    a1 = 0
    b5 = "http:
    b6 = webdriver.Firefox()
    b6.get(b5)
    while True:
        try:
            b7 = b6.find_elements(By.XPATH, '
            for result in b7:
                print(result.text)
            b8 = b6.find_element(By.XPATH, '
            b8.click()
        except NoSuchElementException:
            try:
                b9 = b6.find_element(By.XPATH, '
                b6.switch_to.b9(b9)
                b6.find_element(By.XPATH, "
                b6.switch_to.default_content()
                time.sleep(10)
                b6.switch_to.default_content()
                b6.quit()
                a1 += 1
                b6 = fonk1(a1)
                time.sleep(10)
            except NoSuchElementException:
                print("No CAPTCHA found.")
            except TimeoutException:
                print("Timeout occurred.")
                break
            except Exception as e:
                print("An error occurred:", str(e))
                break
if b10 = = "__main__":
    fonk2()