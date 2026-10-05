
from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
from common import get_public_ip
import random
print("Current IP Address: ", get_public_ip())
username = 'Your User Name'
password = 'Your Password'
port = 22225
session_id = random.random()
super_proxy_url = 'http:
print("Super Proxy URL: ", super_proxy_url)
proxy = Proxy({
    'proxyType': ProxyType.MANUAL,
    'httpProxy': super_proxy_url,
    'ftpProxy': super_proxy_url,
    'sslProxy': super_proxy_url,
    'noProxy': ''
})
browser = input("Please enter your browser name (e.g., Chrome/Firefox): ")
driver = None
if browser == "Chrome":
    options = webdriver.ChromeOptions()
    options.add_argument('--proxy-server=%s' % super_proxy_url)
    driver = webdriver.Chrome(
        executable_path='Your Chromedriver Executable Path',
        chrome_options=options)
elif browser == "Firefox":
    driver = webdriver.Firefox(executable_path="Your Geckodriver Executable path",
                               proxy=proxy)
driver.get('https:
print("New IP Address: ", driver.find_element_by_xpath('
driver.quit()