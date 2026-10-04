import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.b2 import Service
from selenium.webdriver.chrome.b1 import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def fonk1(b20, b21, b22):
    b1 = Options()
    b1.add_argument("--disable-notifications")
    b2 = Service(b21)
    b3 = webdriver.Chrome(b2=b2, b1=b1)
    b3.get(b20)
    a1 = 5
    b4 = b3.execute_script("return document.body.scrollHeight")
    print(b4)
    for _ in range(5):
        b3.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(a1)
        try:
            WebDriverWait(b3, a1).until(
                EC.presence_of_element_located((By.CLASS_NAME, "UFIPagerLink"))
            )
        except Exception as e:
            print("Error waiting for UFIPagerLink:", e)
        for i in b3.find_elements(By.CLASS_NAME, "UFIPagerLink"):
            try:
                i.click()
                print(i)
            except Exception as e:
                print('Error clicking UFIPagerLink:', e)
        try:
            WebDriverWait(b3, a1).until(
                EC.presence_of_element_located((By.CLASS_NAME, "see_more_link"))
            )
        except Exception as e:
            print("Error waiting for see_more_link:", e)
        for j in b3.find_elements(By.CLASS_NAME, "see_more_link"):
            try:
                j.click()
                print(j)
            except Exception as e:
                print('Error clicking see_more_link:', e)
        b5 = b3.execute_script("return document.body.scrollHeight")
        print(b5)
        if b5 = = b4:
            break
        b4 = b5
    b6 = b3.find_elements(By.XPATH, "
    b7 = []
    b8 = []
    b9 = []
    b10 = []
    b11 = []
    b12 = []
    for p in range(len(b6)):
        try:
            b13 = b6[p].find_element(By.CSS_SELECTOR, "abbr._5ptz").get_attribute("title")
            b8.append(b13)
            b7.append(p)
        except Exception as e:
            print('Error getting post date:', e)
            b8.append('none')
            b7.append(p)
        try:
            b14 = b6[p].find_element(By.CSS_SELECTOR, 'div._5pbx.userContent._3576').text
            b9.append(b14)
        except Exception as e:
            print('Error getting post content:', e)
            b9.append('none')
        try:
            b15 = b6[p].find_elements(By.CSS_SELECTOR, "a._3rwx._42ft")
            b10.append(b15[0].text)
        except IndexError as e:
            print('Error getting post shares:', e)
            b10.append('none')
        try:
            b16 = b6[p].find_elements(By.CSS_SELECTOR, "a._3dlf")
            b11.append(b16[0].text.split('\n')[0])
        except IndexError as e:
            print('Error getting post b11:', e)
            b11.append('none')
        try:
            b17 = b6[p].find_elements(By.CSS_SELECTOR, "a._3hg-._42ft")
            b12.append(b17[0].text)
        except IndexError as e:
            print('Error getting post comments:', e)
            b12.append('none')
    if len(b8) != len(b9) and len(b8) != len(b10):
        b18 = len(b9) - len(b8)
        b9 = b9[b18:]
        b10 = b10[b18:]
        b6 = b6[b18:]
        b11 = b11[b18:]
        b12 = b12[b18:]
    b19 = pd.DataFrame({
        'utente': b22,
        'b13': b8,
        'post': b9,
        'id post': b7,
        'b11': b11,
        'b15': b10,
        'comments number': b12
    })
    b3.quit()
    return b19
b20 = 'https:
b21 = 'path_to_your_chromedriver'
b22 = 'Your Name'
b23 = fonk1(b20, b21, b22)
print(b23)