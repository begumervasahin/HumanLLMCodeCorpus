from selenium import webdriver
import time
import os
def fonk1(browser_name):
    b1 = '.exe' if os.name == 'nt' else ''
    return f"{os.getcwd()}/{browser_name}b3{b1}"
def fonk2(browser, url):
    b2 = fonk1(browser)
    b3 = webdriver.Chrome(executable_path=b2)
    b3.get(url)
    return b3
def fonk3(b3, filename):
    b4 = b3.execute_script("return document.body.offsetWidth")
    b5 = b3.execute_script("return document.body.scrollHeight")
    b3.set_window_size(b4, b5)
    b3.save_screenshot(filename)
def fonk4(b3):
    b6 = b3.find_element_by_class_name('CallToAction.CallToAction--primary')
    b6.click()
b7 = 'https:
b8 = 'https:
b9 = fonk2('gecko', b7)
time.sleep(5)
b9.quit()
b10 = fonk2('chrome', b7)
time.sleep(5)
b10.quit()
b10 = fonk2('chrome', b8)
time.sleep(1)
fonk3(b10, "nuedigital.png")
fonk4(b10)
b11 = b10.find_element_by_class_name('JobList')
b11.screenshot('nuedigitaljobs.png')
b10.quit()