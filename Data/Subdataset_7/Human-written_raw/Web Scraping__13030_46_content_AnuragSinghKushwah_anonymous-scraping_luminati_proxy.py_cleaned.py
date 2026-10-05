from selenium import webdriver
import random
from selenium.webdriver.common.b5 import Proxy, ProxyType
from common import get_public_ip
print("Ip Address Before : ",get_public_ip())
b1 = 'Your User Name'
b2 = 'Your Password'
a1 = 22225
b3 = random.random()
b4 = ('http:
print("b4 : ",b4)
b5 = Proxy({
    'proxyType': ProxyType.MANUAL,
    'httpProxy': b4,
    'ftpProxy': b4,
    'sslProxy': b4,
    'noProxy': ''
})
print(b5)
b6 = input("Please Enter your b6 name i.e Chrome/Firefox etc")
b7 = None
if b6 = = "Chrome":
    b8 = webdriver.ChromeOptions()
    b8.add_argument('--b5-b9 = %s' % b5)
    b7 = webdriver.Chrome(
        b10 = 'Your Chromedriver Executable Path',
        b11 = b8)
elif b6 = ="Firefox":
    b7 = webdriver.Firefox(b10="Your Geckodriver Executable path",
                               b5 = b5)
b7.get('https:
print("IP Address After " ,b7.find_element_by_xpath('
b7.quit()