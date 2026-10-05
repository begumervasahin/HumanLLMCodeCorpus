
from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
from common import get_public_ip
import random
def print_current_ip():
    print("Current IP Address: ", get_public_ip())
def generate_super_proxy_url(username, password, port):
    session_id = random.random()
    return 'http:
def configure_proxy(super_proxy_url):
    return Proxy({
        'proxyType': ProxyType.MANUAL,
        'httpProxy': super_proxy_url,
        'ftpProxy': super_proxy_url,
        'sslProxy': super_proxy_url,
        'noProxy': ''
    })
def initialize_driver(browser, proxy):
    if browser == "Chrome":
        options = webdriver.ChromeOptions()
        options.add_argument('--proxy-server=%s' % super_proxy_url)
        return webdriver.Chrome(
            executable_path='Your Chromedriver Executable Path',
            chrome_options=options)
    elif browser == "Firefox":
        return webdriver.Firefox(executable_path="Your Geckodriver Executable path",
                                  proxy=proxy)
def print_new_ip(driver):
    ip_element = driver.find_element_by_xpath('
    print("New IP Address: ", ip_element.text)
def main():
    print_current_ip()
    username = 'Your User Name'
    password = 'Your Password'
    port = 22225
    super_proxy_url = generate_super_proxy_url(username, password, port)
    print("Super Proxy URL: ", super_proxy_url)
    proxy = configure_proxy(super_proxy_url)
    browser = input("Please enter your browser name (e.g., Chrome/Firefox): ")
    driver = initialize_driver(browser, proxy)
    driver.get('https:
    print_new_ip(driver)
    driver.quit()
if __name__ == "__main__":
    main()