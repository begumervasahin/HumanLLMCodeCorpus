import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.b2 import Service
from selenium.webdriver.chrome.b1 import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def fonk1(b18, b19, b20):
    b1 = Options()
    b1.add_argument("--disable-notifications")
    b2 = Service(b19)
    b3 = webdriver.Chrome(b2=b2, b1=b1)
    b3.get(b18)
    a1 = 5
    b4 = b3.execute_script("return document.body.scrollHeight")
    print(f"Initial page height: {b4}")
    for _ in range(5):
        b3.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(a1)
        try:
            WebDriverWait(b3, a1).until(
                EC.presence_of_element_located((By.CLASS_NAME, "UFIPagerLink"))
            )
        except Exception as e:
            print(f"Error waiting for UFIPagerLink: {e}")
        for i in b3.find_elements(By.CLASS_NAME, "UFIPagerLink"):
            try:
                i.click()
                print(f"Clicked on: {i}")
            except Exception as e:
                print(f"Error clicking UFIPagerLink: {e}")
        try:
            WebDriverWait(b3, a1).until(
                EC.presence_of_element_located((By.CLASS_NAME, "see_more_link"))
            )
        except Exception as e:
            print(f"Error waiting for see_more_link: {e}")
        for j in b3.find_elements(By.CLASS_NAME, "see_more_link"):
            try:
                j.click()
                print(f"Clicked on: {j}")
            except Exception as e:
                print(f"Error clicking see_more_link: {e}")
        b5 = b3.execute_script("return document.body.scrollHeight")
        print(f"New page height: {b5}")
        if b5 = = b4:
            break
        b4 = b5
    b6 = b3.find_elements(By.XPATH, "
    id_post, times, b14, b15, b16, b7 = [], [], [], [], [], []
    for p in range(len(b6)):
        try:
            b8 = b6[p].find_element(By.CSS_SELECTOR, "abbr._5ptz").get_attribute("title")
            times.append(b8)
            id_post.append(p)
        except Exception as e:
            print(f"Error getting post date: {e}")
            times.append('none')
            id_post.append(p)
        try:
            b9 = b6[p].find_element(By.CSS_SELECTOR, 'div._5pbx.userContent._3576').text
            b14.append(b9)
        except Exception as e:
            print(f"Error getting post content: {e}")
            b14.append('none')
        try:
            b10 = b6[p].find_elements(By.CSS_SELECTOR, "a._3rwx._42ft")
            b15.append(b10[0].text)
        except IndexError as e:
            print(f"Error getting post shares: {e}")
            b15.append('none')
        try:
            b11 = b6[p].find_elements(By.CSS_SELECTOR, "a._3dlf")
            b16.append(b11[0].text.split('\n')[0])
        except IndexError as e:
            print(f"Error getting post b16: {e}")
            b16.append('none')
        try:
            b12 = b6[p].find_elements(By.CSS_SELECTOR, "a._3hg-._42ft")
            b7.append(b12[0].text)
        except IndexError as e:
            print(f"Error getting post comments: {e}")
            b7.append('none')
    if len(times) != len(b14) and len(times) != len(b15):
        b13 = len(b14) - len(times)
        b14 = b14[b13:]
        b15 = b15[b13:]
        b6 = b6[b13:]
        b16 = b16[b13:]
        b7 = b7[b13:]
    b17 = pd.DataFrame({
        'utente': b20,
        'b8': times,
        'post': b14,
        'id post': id_post,
        'b16': b16,
        'b10': b15,
        'comments number': b7
    })
    b3.quit()
    return b17
b18 = 'https:
b19 = 'path_to_your_chromedriver'
b20 = 'Your Name'
b21 = fonk1(b18, b19, b20)
print(b21)