
from selenium import webdriver
import time
import os
extension = ''
if os.name == 'nt':
    extension = '.exe'
current_directory = os.getcwd()
firefox_driver_path = current_directory + '/geckodriver' + extension
firefox_browser = webdriver.Firefox(executable_path=firefox_driver_path)
firefox_browser.get('https:
time.sleep(5)
firefox_browser.quit()
chrome_driver_path = current_directory + '/chromedriver' + extension
chrome_browser = webdriver.Chrome(executable_path=chrome_driver_path)
chrome_browser.get('https:
time.sleep(5)
chrome_browser.quit()
chrome_browser = webdriver.Chrome(executable_path=chrome_driver_path)
chrome_browser.get('https:
time.sleep(1)
total_width = chrome_browser.execute_script("return document.body.offsetWidth")
total_height = chrome_browser.execute_script("return document.body.scrollHeight")
chrome_browser.set_window_size(total_width, total_height)
chrome_browser.save_screenshot("nuedigital.png")
cookie_ok_button = chrome_browser.find_element_by_class_name('CallToAction.CallToAction--primary')
cookie_ok_button.click()
job_listings_section = chrome_browser.find_element_by_class_name('JobList')
job_listings_section.screenshot('nuedigitaljobs.png')
chrome_browser.quit()