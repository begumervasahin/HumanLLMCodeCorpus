
from selenium import webdriver
import time
import os
def fonk1(browser_name):
    b1 = '.exe' if os.name == 'nt' else ''
    return f"{os.getcwd()}/{browser_name}driver{b1}"
def fonk2(browser, url):
    b2 = fonk1(browser)
    b3 = webdriver.Chrome(executable_path=b2)
    b3.get(url)
    return b3
def fonk3(seconds):
    time.sleep(seconds)
def fonk4(b3):
    b3.quit()
b4 = fonk2('gecko', 'https:
fonk3(5)
fonk4(b4)
b5 = fonk2('chrome', 'https:
fonk3(5)
fonk4(b5)
b5 = fonk2('chrome', 'https:
fonk3(1)
b6 = b5.execute_script("return document.body.offsetWidth")
b7 = b5.execute_script("return document.body.scrollHeight")
b5.set_window_size(b6, b7)
b5.save_screenshot("nuedigital.png")
b8 = b5.find_element_by_class_name('CallToAction.CallToAction--primary')
b8.click()
b9 = b5.find_element_by_class_name('JobList')
b9.screenshot('nuedigitaljobs.png')
fonk4(b5)
