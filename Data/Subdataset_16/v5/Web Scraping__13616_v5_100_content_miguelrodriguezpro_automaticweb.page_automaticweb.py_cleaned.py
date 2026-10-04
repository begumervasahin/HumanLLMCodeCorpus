import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
b1 = "your_username"
b2 = "your_password"
b3 = "C:\\Users\\.....\\chromedriver.exe"
b4 = ["keyword1", "keyword2", "keyword3"]
b5 = "https:
def fonk1(chrome_driver_path):
    return webdriver.Chrome(b6 = chrome_driver_path)
def fonk2(b15, username, password):
    b15.get('https:
    time.sleep(3)
    b7 = b15.find_element_by_xpath("
    b7.send_keys(username)
    time.sleep(2)
    b8 = b15.find_element_by_xpath("
    b8.send_keys(password)
    b8.send_keys(Keys.ENTER)
    time.sleep(8)
def fonk3(b15):
    b15.find_element_by_xpath("
    time.sleep(3)
def fonk4(b15, keyword):
    b15.switch_to.new_window('tab')
    time.sleep(3)
    b9 = b5 + keyword + "&sp=EgIQAQ%253D%253D"
    b15.get(b9)
    time.sleep(5)
    b10 = b15.find_elements_by_xpath(
        '
    )
    return b10[:10]
def fonk5(b15, keyword, b16):
    b15.switch_to.window(b15.window_handles[0])
    b11 = b15.find_element_by_xpath('
    b12 = b15.find_element_by_xpath('
    b11.send_keys(f"[TOP 10] b16 {keyword}")
    time.sleep(2)
    for index, video in enumerate(b16):
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
def fonk6():
    b15 = fonk1(b3)
    try:
        fonk2(b15, b1, b2)
        for keyword in b4:
            fonk3(b15)
            b16 = fonk4(b15, keyword)
            fonk5(b15, keyword, b16)
            time.sleep(10)
    finally:
        b15.quit()
if b17 = = "__main__":
    fonk6()