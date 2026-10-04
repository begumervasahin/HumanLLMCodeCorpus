from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.b1 import Options
import time
def fonk1():
    b1 = Options()
    b1.b2 = True
    b3 = webdriver.Firefox(b1=b1)
    return b3
def fonk2(b11):
    b3 = fonk1()
    b4 = f"http:
    b3.get(b4)
    b5 = []
    try:
        while True:
            b6 = b3.find_elements(By.XPATH, '
            for element in b6:
                try:
                    b7 = element.find_element(By.TAG_NAME, "h3").text
                    b8 = element.find_element(By.TAG_NAME, "a").get_attribute("href")
                    b5.append((b7, b8))
                except Exception as inner_e:
                    print(f"An error occurred while processing an element: {inner_e}")
            b9 = b3.find_elements(By.XPATH, '
            if b9:
                b9[0].click()
                time.sleep(2)
            else:
                break
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        b3.quit()
    return b5
if b10 = = "__main__":
    b11 = "chanel"
    b5 = fonk2(b11)
    for b7, b8 in b5:
        print(f"Title: {b7}\nLink: {b8}\n")