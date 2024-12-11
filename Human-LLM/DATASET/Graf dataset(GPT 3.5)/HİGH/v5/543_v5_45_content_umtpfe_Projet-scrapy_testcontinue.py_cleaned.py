import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
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
def fonk1(proxy_value):
    print("Attempting to change proxy...")
    b2 = b1[proxy_value].split(':')
    return b2
def fonk2():
    b3 = webdriver.FirefoxProfile()
    b4 = webdriver.Firefox(firefox_profile=b3)
    b5 = "http:
    b4.get(b5)
    while True:
        b4.get(b5)
        b6 = True
        while b6:
            try:
                b7 = b4.find_elements_by_xpath('
                for result in b7:
                    print(result.text)
                b8 = b4.find_element_by_xpath('
                b8.click()
            except NoSuchElementException:
                try:
                    b9 = WebDriverWait(b4, 10).until(EC.presence_of_element_located((By.XPATH, '
                except:
                    try:
                        print("Captcha encountered.")
                        b10 = b4.find_element_by_xpath('
                        b4.switch_to.b10(b10)
                        b4.find_element_by_xpath("
                        b4.switch_to.default_content()
                        time.sleep(10)
                        b4.switch_to.default_content()
                        try:
                            print("Attempting to change proxy...")
                            b2 = fonk1(i)
                            print("Changing proxy...")
                            b3 = webdriver.FirefoxProfile()
                            b3.set_preference("network.proxy.type", 1)
                            b3.set_preference("network.proxy.https", b2[0])
                            b3.set_preference("network.proxy.https_port", int(b2[1]))
                            b3.set_preference("network.proxy.ssl", b2[0])
                            b3.set_preference("network.proxy.ssl_port", int(b2[1]))
                            b3.set_preference("general.useragent.override", "whatever_useragent")
                            b3.set_preference("network.proxy.socks_version", 5)
                            b3.update_preferences()
                            print("Proxy changed.")
                            b4 = webdriver.Firefox(firefox_profile=b3)
                            time.sleep(10)
                            i += 1
                        except:
                            print('Continuing...')
                    except:
                        try:
                            b11 = WebDriverWait(b4, 10)
                            b8 = b11.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'td.b:nth-child(12) > a:nth-child(1) > span:nth-child(2)')))
                            b8.click()
                        except:
                            b6 = False
if b12 = = "__main__":
    fonk2()