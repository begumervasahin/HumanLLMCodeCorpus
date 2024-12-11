
from selenium import webdriver
import time
import os
b1 = ''
if os.b2 = = 'nt':
    b1 = '.exe'
b3 = os.getcwd()
b4 = b3 + '/geckodriver' + b1
b5 = webdriver.Firefox(executable_path=b4)
b5.get('https:
time.sleep(5)
b5.quit()
b6 = b3 + '/chromedriver' + b1
b7 = webdriver.Chrome(executable_path=b6)
b7.get('https:
time.sleep(5)
b7.quit()
b7 = webdriver.Chrome(executable_path=b6)
b7.get('https:
time.sleep(1)
b8 = b7.execute_script("return document.body.offsetWidth")
b9 = b7.execute_script("return document.body.scrollHeight")
b7.set_window_size(b8, b9)
b7.save_screenshot("nuedigital.png")
b10 = b7.find_element_by_class_name('CallToAction.CallToAction--primary')
b10.click()
b11 = b7.find_element_by_class_name('JobList')
b11.screenshot('nuedigitaljobs.png')
b7.quit()