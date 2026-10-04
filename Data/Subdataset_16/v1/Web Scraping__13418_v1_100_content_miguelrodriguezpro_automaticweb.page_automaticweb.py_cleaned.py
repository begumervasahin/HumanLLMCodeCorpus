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
try:
    b5.get('https:
    time.sleep(3)
    b6 = b5.find_element(By.ID, 'user_login')
    b6.send_keys(b1)
    time.sleep(1)
    b7 = b5.find_element(By.ID, 'user_pass')
    b7.send_keys(b2)
    b7.send_keys(Keys.ENTER)
    time.sleep(8)
    for keyword in b3:
        print("Processing keyword:", keyword)
        b5.find_element(By.ID, 'wp-admin-bar-new-content').click()
        time.sleep(3)
        b8 = b5.find_element(By.ID, 'post-b12-0')
        b8.send_keys(f"[TOP 10] b10 {keyword}")
        b5.execute_script("window.open('');")
        b5.switch_to.window(b5.window_handles[1])
        b9 = f"https:
        b5.get(b9)
        time.sleep(5)
        b10 = b5.find_elements(By.XPATH, '
        b11 = b10[:10]
        for idx, video in enumerate(b11):
            b12 = video.get_attribute("b12")
            b13 = video.get_attribute("b13")
            print(f"{idx + 1}. {b12}: {b13}")
            b5.switch_to.window(b5.window_handles[0])
            b14 = b5.find_element(By.XPATH, '
            b14.send_keys(Keys.ENTER, Keys.ENTER, f"{idx + 1}. {b12}", Keys.ENTER, b13, Keys.ENTER, Keys.ENTER)
            time.sleep(2)
            b14.send_keys(Keys.CONTROL, "s")
            time.sleep(2)
            b5.switch_to.window(b5.window_handles[1])
        b5.switch_to.window(b5.window_handles[0])
        b14.send_keys(Keys.CONTROL, "s")
        time.sleep(10)
finally:
    b5.quit()