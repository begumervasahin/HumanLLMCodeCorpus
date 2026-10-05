
from selenium import webdriver
import time
import os
def get_driver_path(browser_name):
    ext = '.exe' if os.name == 'nt' else ''
    return f"{os.getcwd()}/{browser_name}driver{ext}"
def open_browser_and_visit_url(browser, url):
    driver_path = get_driver_path(browser)
    browser_instance = webdriver.Chrome(executable_path=driver_path)
    browser_instance.get(url)
    return browser_instance
def wait_for(seconds):
    time.sleep(seconds)
def close_browser(browser_instance):
    browser_instance.quit()
firefox_browser = open_browser_and_visit_url('gecko', 'https:
wait_for(5)
close_browser(firefox_browser)
chrome_browser = open_browser_and_visit_url('chrome', 'https:
wait_for(5)
close_browser(chrome_browser)
chrome_browser = open_browser_and_visit_url('chrome', 'https:
wait_for(1)
total_width = chrome_browser.execute_script("return document.body.offsetWidth")
total_height = chrome_browser.execute_script("return document.body.scrollHeight")
chrome_browser.set_window_size(total_width, total_height)
chrome_browser.save_screenshot("nuedigital.png")
cookie_ok_button = chrome_browser.find_element_by_class_name('CallToAction.CallToAction--primary')
cookie_ok_button.click()
site = chrome_browser.find_element_by_class_name('JobList')
site.screenshot('nuedigitaljobs.png')
close_browser(chrome_browser)
