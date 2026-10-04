import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.b2 import Service
from selenium.webdriver.chrome.b1 import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def fonk1(b18):
    b1 = Options()
    b1.add_argument("--disable-notifications")
    b2 = Service(b18)
    b3 = webdriver.Chrome(b2=b2, b1=b1)
    return b3
def fonk2(b3, a1, b4 = 5):
    b5 = b3.execute_script("return document.body.scrollHeight")
    print(f"Initial page height: {b5}")
    for _ in range(b4):
        b3.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(a1)
        fonk3(b3, By.CLASS_NAME, "UFIPagerLink", a1)
        fonk3(b3, By.CLASS_NAME, "see_more_link", a1)
        b6 = b3.execute_script("return document.body.scrollHeight")
        print(f"New page height: {b6}")
        if b6 = = b5:
            break
        b5 = b6
def fonk3(b3, by, value, a1):
    try:
        WebDriverWait(b3, a1).until(
            EC.presence_of_element_located((by, value))
        )
        b7 = b3.find_elements(by, value)
        for element in b7:
            try:
                element.click()
                print(f"Clicked on: {element}")
            except Exception as e:
                print(f"Error clicking {value}: {e}")
    except Exception as e:
        print(f"Error waiting for {value}: {e}")
def fonk4(b9):
    id_post, b11, b12, b13, b14, b8 = [], [], [], [], [], []
    for p, post in enumerate(b9):
        id_post.append(p)
        b11.append(fonk5(post, By.CSS_SELECTOR, "abbr._5ptz", "title", 'none'))
        b12.append(fonk6(post, By.CSS_SELECTOR, 'div._5pbx.userContent._3576', 'none'))
        b13.append(fonk6(post, By.CSS_SELECTOR, "a._3rwx._42ft", 'none'))
        b14.append(fonk6(post, By.CSS_SELECTOR, "a._3dlf", 'none').split('\n')[0])
        b8.append(fonk6(post, By.CSS_SELECTOR, "a._3hg-._42ft", 'none'))
    return id_post, b11, b12, b13, b14, b8
def fonk5(post, by, value, attribute, default):
    try:
        return post.find_element(by, value).get_attribute(attribute)
    except Exception as e:
        print(f"Error getting attribute {attribute} for {value}: {e}")
        return default
def fonk6(post, by, value, default):
    try:
        return post.find_element(by, value).text
    except Exception as e:
        print(f"Error getting text for {value}: {e}")
        return default
def fonk7(b17, b18, b19):
    b3 = fonk1(b18)
    b3.get(b17)
    a1 = 5
    fonk2(b3, a1)
    b9 = b3.find_elements(By.XPATH, "
    id_post, b11, b12, b13, b14, b8 = fonk4(b9)
    b10 = min(len(b11), len(b12), len(b13), len(b14), len(b8))
    b11 = b11[:b10]
    b12 = b12[:b10]
    b13 = b13[:b10]
    b14 = b14[:b10]
    b8 = b8[:b10]
    b15 = pd.DataFrame({
        'utente': b19,
        'data': b11,
        'post': b12,
        'id post': id_post[:b10],
        'b14': b14,
        'share': b13,
        'comments number': b8
    })
    b3.quit()
    return b15
if b16 = = "__main__":
    b17 = 'https:
    b18 = 'path_to_your_chromedriver'
    b19 = 'Your Name'
    b20 = fonk7(b17, b18, b19)
    print(b20)