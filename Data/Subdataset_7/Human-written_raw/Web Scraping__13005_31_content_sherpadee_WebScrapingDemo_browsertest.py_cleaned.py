from selenium import webdriver
import time
import os
b1 = ''
if os.b2 = = 'nt':
    b1 = '.exe'
b3 = os.getcwd()
b4 = webdriver.Firefox(executable_path = b3 + '/geckodriver' + b1)
b4.get('https:
time.sleep(5)
b4.quit()
b4 = webdriver.Chrome(executable_path = b3 + '/chromedriver' + b1)
b4.get('https:
time.sleep(5)
b4.quit()
b4 = webdriver.Chrome(executable_path = b3 + '/chromedriver' + b1)
b4.get('https:
time.sleep(1)
b5 = b4.execute_script("return document.body.offsetWidth")
b6 = b4.execute_script("return document.body.scrollHeight")
b4.set_window_size(b5, b6)
b4.save_screenshot("nuedigital.png")
b7 = b4.find_element_by_class_name('CallToAction.CallToAction--primary')
b7.click()
b8 = b4.find_element_by_class_name('JobList')
b8.screenshot('nuedigitaljobs.png')
b4.quit()