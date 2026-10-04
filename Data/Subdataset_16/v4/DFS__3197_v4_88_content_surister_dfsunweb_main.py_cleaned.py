from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
def fonk1():
    b1 = 'D:/geckodriver/geckodriver.exe'
    return webdriver.Firefox(b2 = b1)
def fonk2(b6, date):
    b3 = b6.find_element(By.ID, 'fecha_salida')
    b3.click()
    b3.clear()
    b3.send_keys(date)
def fonk3(b6, dropdown_id):
    b4 = WebDriverWait(b6, 10).until(
        EC.presence_of_element_located((By.ID, dropdown_id))
    )
    b5 = b4.find_elements(By.TAG_NAME, 'option')
    for option in b5:
        print(option.get_attribute('value'))
        sleep(1)
def fonk4():
    b6 = fonk1()
    try:
        b6.get("http:
        fonk2(b6, '2019-08-14')
        sleep(1)
        print("Flight b5:")
        fonk3(b6, 'flight')
        b7 = WebDriverWait(b6, 10).until(
            EC.presence_of_element_located((By.ID, 'flight'))
        )
        b8 = b7.find_elements(By.TAG_NAME, 'option')
        for flight in b8:
            flight.click()
            print(f"Selected flight: {flight.get_attribute('value')}")
            print("Hotel b5:")
            fonk3(b6, 'hoteles')
            sleep(1)
        sleep(100)
    finally:
        b6.quit()
if b9 = = "__main__":
    fonk4()