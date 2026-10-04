from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
def setup_driver():
    driver_path = 'D:/geckodriver/geckodriver.exe'
    driver = webdriver.Firefox(executable_path=driver_path)
    return driver
def select_date(driver, date):
    date_input = driver.find_element(By.ID, 'fecha_salida')
    date_input.click()
    date_input.send_keys(date)
    date_input.click()
def print_dropdown_options(driver, dropdown_id):
    dropdown_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, f"
    )
    options = dropdown_element.find_elements(By.TAG_NAME, 'option')
    for option in options:
        option.click()
        print(option.get_attribute('value'))
        sleep(1)
def main():
    driver = setup_driver()
    try:
        driver.get("http:
        select_date(driver, '2019-08-14')
        sleep(1)
        print_dropdown_options(driver, 'flight')
        print_dropdown_options(driver, 'hoteles')
        sleep(100)
    finally:
        driver.quit()
if __name__ == "__main__":
    main()