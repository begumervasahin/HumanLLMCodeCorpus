from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
def initialize_webdriver():
    driver_path = 'D:/geckodriver/geckodriver.exe'
    return webdriver.Firefox(executable_path=driver_path)
def input_date(driver, date):
    date_field = driver.find_element(By.ID, 'fecha_salida')
    date_field.click()
    date_field.clear()
    date_field.send_keys(date)
def fetch_and_print_dropdown_options(driver, dropdown_id):
    dropdown = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, dropdown_id))
    )
    options = dropdown.find_elements(By.TAG_NAME, 'option')
    for option in options:
        print(option.get_attribute('value'))
        sleep(1)
def process_flight_options(driver):
    flight_dropdown = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'flight'))
    )
    flights = flight_dropdown.find_elements(By.TAG_NAME, 'option')
    for flight in flights:
        flight.click()
        print(f"Selected flight: {flight.get_attribute('value')}")
        print("Hotel options:")
        fetch_and_print_dropdown_options(driver, 'hoteles')
        sleep(1)
def main():
    driver = initialize_webdriver()
    try:
        driver.get("http:
        input_date(driver, '2019-08-14')
        sleep(1)
        print("Flight options:")
        fetch_and_print_dropdown_options(driver, 'flight')
        print("Processing flight options and related hotels...")
        process_flight_options(driver)
        sleep(100)
    finally:
        driver.quit()
if __name__ == "__main__":
    main()