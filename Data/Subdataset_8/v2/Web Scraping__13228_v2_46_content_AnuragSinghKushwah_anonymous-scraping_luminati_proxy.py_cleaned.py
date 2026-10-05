from selenium import webdriver
import random
from selenium.webdriver.common.proxy import Proxy, ProxyType
from common import get_public_ip
def get_public_ip():
    return "Your Public IP"
print("Current Public IP Address: ", get_public_ip())
username = 'Your User Name'
password = 'Your Password'
port = 22225
session_id = random.random()
super_proxy_url = f'http:
print("Luminati Proxy URL: ", super_proxy_url)
proxy = Proxy({
    'proxyType': ProxyType.MANUAL,
    'httpProxy': super_proxy_url,
    'ftpProxy': super_proxy_url,
    'sslProxy': super_proxy_url,
    'noProxy': ''
})
print("Proxy Configuration: ", proxy)
browser = input("Please Enter your browser name (e.g., Chrome/Firefox): ")
driver = None
if browser.lower() == "chrome":
    options = webdriver.ChromeOptions()
    options.add_argument(f'--proxy-server={super_proxy_url}')
    driver = webdriver.Chrome(
        executable_path='Your Chromedriver Executable Path',
        options=options
    )
elif browser.lower() == "firefox":
    proxy.add_to_capabilities()
    driver = webdriver.Firefox(
        executable_path="Your Geckodriver Executable path",
        proxy=proxy
    )
driver.get('https:
print("IP Address After Setting Proxy: ", driver.find_element_by_xpath('
driver.quit()