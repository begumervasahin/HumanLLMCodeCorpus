import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
b1 = "your_username"
b2 = "your_password"
b3 = "C:\\Users\\.....\\chromedriver.exe"
b4 = ["keyword1", "keyword2", "keyword3"]
b5 = "https:
b6 = webdriver.Chrome(executable_path=b3)
def fonk1():
    b6.get('https:
    time.sleep(3)
    b7 = b6.find_element_by_xpath("
    b7.send_keys(b1)
    time.sleep(2)
    b8 = b6.find_element_by_xpath("
    b8.send_keys(b2)
    b8.send_keys(Keys.ENTER)
    time.sleep(8)
def fonk2():
    b6.find_element_by_xpath("
    time.sleep(3)
def fonk3(keyword):
    b6.switch_to.window(b6.window_handles[1])
    time.sleep(3)
    b9 = b5 + keyword + "&sp=EgIQAQ%253D%253D"
    b6.get(b9)
    time.sleep(5)
    b10 = b6.find_elements_by_xpath(
        '
    )
    return b10[:10]
def fonk4(keyword, b10):
    b6.switch_to.window(b6.window_handles[0])
    b11 = b6.find_element_by_xpath('
    b12 = b6.find_element_by_xpath('
    b11.send_keys(f"[TOP 10] b10 {keyword}")
    time.sleep(2)
    for index, video in enumerate(b10):
        b13 = video.get_attribute("title")
        b14 = video.get_attribute("href")
        b12.send_keys(Keys.ENTER)
        b12.send_keys(f"{index + 1}. {b13}")
        b12.send_keys(Keys.ENTER)
        b12.send_keys(b14)
        b12.send_keys(Keys.ENTER)
        time.sleep(1)
    b12.send_keys(Keys.CONTROL, "s")
    time.sleep(2)
fonk1()
for keyword in b4:
    fonk2()
    b10 = fonk3(keyword)
    fonk4(keyword, b10)
    time.sleep(10)
b6.quit()