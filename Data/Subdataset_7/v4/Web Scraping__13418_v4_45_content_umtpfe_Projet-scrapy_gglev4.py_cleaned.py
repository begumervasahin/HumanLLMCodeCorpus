from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, WebDriverException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
def fonk1(b2):
    try:
        b1 = b2.find_element(By.XPATH, '
        b2.switch_to.b1(b1)
        b2.find_element(By.XPATH, "
        print("CAPTCHA detected. Waiting for 120 seconds for manual solving.")
        time.sleep(120)
        b2.switch_to.default_content()
        return True
    except NoSuchElementException:
        return False
b2 = webdriver.Firefox()
b3 = "http:
while True:
    try:
        b2.get(b3)
        b4 = True
        while b4:
            try:
                b5 = b2.find_elements(By.XPATH, '
                for result in b5:
                    print(result.text)
                b6 = b2.find_element(By.XPATH, '
                b6.click()
            except NoSuchElementException:
                if fonk1(b2):
                    continue
                else:
                    b4 = False
            except WebDriverException:
                b4 = False
    except TimeoutException:
        print("Timeout occurred while loading page.")
    except Exception as e:
        print("An error occurred:", e)
b2.quit()