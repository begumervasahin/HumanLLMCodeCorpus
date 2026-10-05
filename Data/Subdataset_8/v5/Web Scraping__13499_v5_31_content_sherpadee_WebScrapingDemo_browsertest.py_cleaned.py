from selenium import webdriver
import time
import os
def get_driver_path(browser_name):
    extension = '.exe' if os.name == 'nt' else ''
    return f"{os.getcwd()}/{browser_name}driver{extension}"
def launch_browser(browser, url):
    driver_path = get_driver_path(browser)
    driver = webdriver.Chrome(executable_path=driver_path)
    driver.get(url)
    return driver
def take_full_page_screenshot(driver, filename):
    total_width = driver.execute_script("return document.body.offsetWidth")
    total_height = driver.execute_script("return document.body.scrollHeight")
    driver.set_window_size(total_width, total_height)
    driver.save_screenshot(filename)
def accept_cookies(driver):
    cookie_ok_button = driver.find_element_by_class_name('CallToAction.CallToAction--primary')
    cookie_ok_button.click()
google_url = 'https:
job_board_url = 'https:
firefox_browser = launch_browser('gecko', google_url)
time.sleep(5)
firefox_browser.quit()
chrome_browser = launch_browser('chrome', google_url)
time.sleep(5)
chrome_browser.quit()
chrome_browser = launch_browser('chrome', job_board_url)
time.sleep(1)
take_full_page_screenshot(chrome_browser, "nuedigital.png")
accept_cookies(chrome_browser)
job_listings_section = chrome_browser.find_element_by_class_name('JobList')
job_listings_section.screenshot('nuedigitaljobs.png')
chrome_browser.quit()