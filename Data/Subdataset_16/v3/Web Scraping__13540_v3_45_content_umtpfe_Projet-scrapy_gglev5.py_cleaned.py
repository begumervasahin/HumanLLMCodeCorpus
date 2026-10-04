from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.b1 import Options
import time
def fonk1():
    b1 = Options()
    b1.b2 = True
    b3 = webdriver.Firefox(b1=b1)
    return b3
def fonk2(b3):
    b4 = []
    b5 = b3.find_elements(By.XPATH, '
    for element in b5:
        try:
            b6 = element.find_element(By.TAG_NAME, "h3").text
            b7 = element.find_element(By.TAG_NAME, "a").get_attribute("href")
            b4.append((b6, b7))
        except Exception as e:
            print(f"An error occurred while processing an element: {e}")
    return b4
def fonk3(b3):
    b8 = b3.find_elements(By.XPATH, '
    if b8:
        b8[0].click()
        time.sleep(2)
        return True
    return False
def fonk4(b12):
    b3 = fonk1()
    b9 = f"http:
    b3.get(b9)
    b10 = []
    try:
        while True:
            b4 = fonk2(b3)
            b10.extend(b4)
            if not fonk3(b3):
                break
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        b3.quit()
    return b10
if b11 = = "__main__":
    b12 = "chanel"
    b4 = fonk4(b12)
    for b6, b7 in b4:
        print(f"Title: {b6}\nLink: {b7}\n")