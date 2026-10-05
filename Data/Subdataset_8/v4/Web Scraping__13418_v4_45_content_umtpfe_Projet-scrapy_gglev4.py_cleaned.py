from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, WebDriverException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
def handle_captcha(driver):
    try:
        frame = driver.find_element(By.XPATH, '
        driver.switch_to.frame(frame)
        driver.find_element(By.XPATH, "
        print("CAPTCHA detected. Waiting for 120 seconds for manual solving.")
        time.sleep(120)
        driver.switch_to.default_content()
        return True
    except NoSuchElementException:
        return False
driver = webdriver.Firefox()
url = "http:
while True:
    try:
        driver.get(url)
        val = True
        while val:
            try:
                results = driver.find_elements(By.XPATH, '
                for result in results:
                    print(result.text)
                next_button = driver.find_element(By.XPATH, '
                next_button.click()
            except NoSuchElementException:
                if handle_captcha(driver):
                    continue
                else:
                    val = False
            except WebDriverException:
                val = False
    except TimeoutException:
        print("Timeout occurred while loading page.")
    except Exception as e:
        print("An error occurred:", e)
driver.quit()