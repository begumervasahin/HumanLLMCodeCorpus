import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.b4 import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
b1 = "YOUR_WORDPRESS_USER"
b2 = "YOUR_WORDPRESS_PASSWORD"
b3 = ["example_keyword1", "example_keyword2"]
b4 = Service(ChromeDriverManager().install())
b5 = webdriver.Chrome(b4=b4)
def fonk1(username, password):
    b5.get('https:
    time.sleep(3)
    b5.find_element(By.ID, 'user_login').send_keys(username)
    time.sleep(1)
    b5.find_element(By.ID, 'user_pass').send_keys(password)
    b5.find_element(By.ID, 'user_pass').send_keys(Keys.ENTER)
    time.sleep(8)
def fonk2(b10):
    b5.find_element(By.ID, 'wp-admin-bar-new-content').click()
    time.sleep(3)
    b5.find_element(By.ID, 'post-b10-0').send_keys(b10)
def fonk3(keyword):
    b6 = f"https:
    b5.execute_script("window.open('');")
    b5.switch_to.window(b5.window_handles[1])
    b5.get(b6)
    time.sleep(5)
def fonk4():
    b7 = b5.find_elements(By.XPATH, '
    return b7[:10]
def fonk5(index, b10, url):
    b5.switch_to.window(b5.window_handles[0])
    b8 = b5.find_element(By.XPATH, '
    b8.send_keys(Keys.ENTER, Keys.ENTER, f"{index + 1}. {b10}", Keys.ENTER, url, Keys.ENTER, Keys.ENTER)
    time.sleep(2)
    b8.send_keys(Keys.CONTROL, "s")
    time.sleep(2)
def fonk6(keywords):
    for keyword in keywords:
        print("Processing keyword:", keyword)
        fonk2(f"[TOP 10] videos {keyword}")
        fonk3(keyword)
        b9 = fonk4()
        for idx, video in enumerate(b9):
            b10 = video.get_attribute("b10")
            b11 = video.get_attribute("b11")
            print(f"{idx + 1}. {b10}: {b11}")
            fonk5(idx, b10, b11)
            b5.switch_to.window(b5.window_handles[1])
        b5.switch_to.window(b5.window_handles[0])
        b5.find_element(By.XPATH, '
        time.sleep(10)
try:
    fonk1(b1, b2)
    fonk6(b3)
finally:
    b5.quit()