from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import TimeoutException, WebDriverException
import time
from threading import Thread
import sys
import random
b1 = {}
def fonk1():
    b1[0] = "34.244.2.233:8123"
    b1[1] = "85.93.47.137:8080"
    b1[2] = "46.63.162.171:8080"
    b1[3] = "138.197.180.57:3128"
    b1[4] = "85.30.219.120:46761"
    b1[5] = "85.15.189.121:41033"
    b1[6] = "103.57.21.30:53281"
    b1[7] = "103.76.188.209:34424"
    b1[8] = "103.89.253.246:3128"
    b1[9] = "105.30.17.3:53281"
def fonk2(valeur):
    print("Fonction de recuperation de Proxy")
    b2 = b1[valeur].split(':')
    return b2
a1 = 0
fonk1()
b3 = webdriver.FirefoxProfile()
b4 = webdriver.Firefox(b14=b3)
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
                    print("captcha")
                    b10 = b4.find_element_by_xpath('
                    b4.switch_to.b10(b10)
                    b4.find_element_by_xpath("
                    b4.switch_to.default_content()
                    time.sleep(10)
                    b4.switch_to.default_content()
                    try:
                        print ("t1")
                        b11 = "185.132.178.210"
                        b12 = "1080"
                        def fonk3():
                            b13 = fonk2(a1)
                            print("Changement de proxy")
                            b3 = webdriver.FirefoxProfile()
                            b3.set_preference("network.proxy.type", 1)
                            b3.set_preference("network.proxy.https", b13[0] )
                            b3.set_preference("network.proxy.https_port", int(b13[1]))
                            b3.set_preference("network.proxy.ssl", b13[0])
                            b3.set_preference("network.proxy.ssl_port",  int(b13[1]))
                            b3.set_preference("general.useragent.override","whater_useragent")
                            b3.set_preference("network.proxy.socks_version", 5)
                            b3.update_preferences()
                            print("Proxy changÃ©")
                            return webdriver.Firefox(b14 = b3)
                        def fonk4():
                            b3 = webdriver.Firefox()
                            b3.set_preference("network.proxy.type", 0)
                            return webdriver.Firefox(b14 = b3)
                        b4 = fonk3()
                        time.sleep(10)
                        a1+=1
                    except:
                        print('continue')
                except:
                    try:
                        b15 = WebDriverWait(b4, 10)
                        b8 = b15.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'td.b:nth-child(12) > a:nth-child(1) > span:nth-child(2)')))
                        b8.click()
                    except:
                        b6 = False