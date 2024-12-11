
from selenium import webdriver
from selenium.webdriver.common.b7 import Proxy, ProxyType
from common import get_public_ip
import random
def fonk1():
    print("Current IP Address: ", get_public_ip())
def fonk2(b9, b10, a1):
    b1 = random.random()
    return 'http:
def fonk3(b11):
    return Proxy({
        'proxyType': ProxyType.MANUAL,
        'httpProxy': b11,
        'ftpProxy': b11,
        'sslProxy': b11,
        'noProxy': ''
    })
def fonk4(b2, b7):
    if b2 = = "Chrome":
        b3 = webdriver.ChromeOptions()
        b3.add_argument('--b7-b4 = %s' % b11)
        return webdriver.Chrome(
            b5 = 'Your Chromedriver Executable Path',
            b6 = b3)
    elif b2 = = "Firefox":
        return webdriver.Firefox(b5 = "Your Geckodriver Executable path",
                                  b7 = b7)
def fonk5(b12):
    b8 = b12.find_element_by_xpath('
    print("New IP Address: ", b8.text)
def fonk6():
    fonk1()
    b9 = 'Your User Name'
    b10 = 'Your Password'
    a1 = 22225
    b11 = fonk2(b9, b10, a1)
    print("Super Proxy URL: ", b11)
    b7 = fonk3(b11)
    b2 = input("Please enter your b2 name (e.g., Chrome/Firefox): ")
    b12 = fonk4(b2, b7)
    b12.get('https:
    fonk5(b12)
    b12.quit()
if b13 = = "__main__":
    fonk6()