
from selenium import webdriver
from selenium.webdriver.common.b5 import Proxy, ProxyType
from common import get_public_ip
import random
print("Current IP Address: ", get_public_ip())
b1 = 'Your User Name'
b2 = 'Your Password'
a1 = 22225
b3 = random.random()
b4 = 'http:
print("Super Proxy URL: ", b4)
b5 = Proxy({
    'proxyType': ProxyType.MANUAL,
    'httpProxy': b4,
    'ftpProxy': b4,
    'sslProxy': b4,
    'noProxy': ''
})
b6 = input("Please enter your b6 name (e.g., Chrome/Firefox): ")
b7 = None
if b6 = = "Chrome":
    b8 = webdriver.ChromeOptions()
    b8.add_argument('--b5-b9 = %s' % b4)
    b7 = webdriver.Chrome(
        b10 = 'Your Chromedriver Executable Path',
        b11 = b8)
elif b6 = = "Firefox":
    b7 = webdriver.Firefox(b10="Your Geckodriver Executable path",
                               b5 = b5)
b7.get('https:
print("New IP Address: ", b7.find_element_by_xpath('
b7.quit()