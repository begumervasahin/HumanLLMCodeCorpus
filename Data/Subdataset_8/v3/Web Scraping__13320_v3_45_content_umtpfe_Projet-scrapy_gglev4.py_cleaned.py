from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, WebDriverException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
def handle_captcha(driver):
    try:
        captcha_frame = driver.find_element(By.XPATH, '
        driver.switch_to.frame(captcha_frame)
        driver.find_element(By.XPATH, "
        print("CAPTCHA detected. Waiting for 120 seconds for manual solving.")
        time.sleep(120)
        driver.switch_to.default_content()
        return True
    except NoSuchElementException:
        return False
driver = webdriver.Firefox()
search_query = "chanel"
google_search_url = f"http:
while True:
    try:
        driver.get(google_search_url)
        continue_search = True
        while continue_search:
            try:
                search_results = driver.find_elements(By.XPATH, '
                for result in search_results:
                    print(result.text)
                next_button = driver.find_element(By.XPATH, '
                next_button.click()
            except NoSuchElementException:
                if handle_captcha(driver):
                    continue
                else:
                    continue_search = False
            except WebDriverException:
                continue_search = False
    except TimeoutException:
        print("Timeout occurred while loading page.")
    except Exception as e:
        print("An error occurred:", e)
driver.quit()