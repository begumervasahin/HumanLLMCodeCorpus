import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
b1 = "" <-HERE YOUR WORDPRESS USER, and PASSWORD
b2 = ""
b3 = webdriver.Chrome(executable_path="C:\\Users\.....\chromedriver.exe") <- HERE YOURS
b4 = [] <- HERE YOUR KEYWORDS
b5 = "https:
a1 = 0
b3.get('https:
time.sleep(3)
b6 = b3.find_element_by_xpath("
b6.send_keys(b1)
time.sleep(5)
b7 = b3.find_element_by_xpath("
b7.send_keys(b2)
b3.find_element_by_xpath("
time.sleep(8)
b3.find_element_by_xpath("
b8 = b3.find_element_by_xpath('
b8.send_keys(Keys.CONTROL,Keys.ALT, Keys.SHIFT, "m")
time.sleep(3)
for e in b4:
    print("PÃ¡gina" + e)
    b3.find_element_by_xpath("
    time.sleep(2)
    time.sleep(3)
    b8 = b3.find_element_by_xpath('
    b8.send_keys("[TOP 10] videos " + " " + e )
    b3.switch_to.window(b3.window_handles[1])
    time.sleep(3)
    b9 = "&sp=EgIQAQ%253D%253D"
    b3.get(b5+e+b9)
    b10 = b3.find_elements_by_xpath('
    time.sleep(5)
    b11 = (e)
    b12 = b10[:10]
    a2 = 0
    for i in b12 :
            a2+=1
            time.sleep(5)
            b13 = i.get_attribute("title")
            b14 = i.get_attribute("href")
            time.sleep(2)
            b3.switch_to.window(b3.window_handles[0])
            b8 = b3.find_element_by_xpath('
            b15 = b3.find_element_by_xpath('
            b15 = b3.find_element_by_xpath('
            time.sleep(2)
            b15.send_keys(Keys.ENTER)
            b15.send_keys(Keys.ENTER)
            b15.send_keys(a2)
            b15.send_keys(" ")
            b15.send_keys(". ")
            b15.send_keys(b13)
            b15.send_keys(Keys.ENTER)
            time.sleep(2)
            b15.send_keys(Keys.ENTER)
            time.sleep(2)
            b15.send_keys(b14)
            b15.send_keys(Keys.ENTER)
            b15.send_keys(Keys.ENTER)
            time.sleep(2)
            b15.send_keys(Keys.CONTROL, "b10")
            time.sleep(2)
            b3.switch_to.window(b3.window_handles[1])
    b3.switch_to.window(b3.window_handles[0])
    b15.send_keys(Keys.CONTROL, "b10")
    time.sleep(10)