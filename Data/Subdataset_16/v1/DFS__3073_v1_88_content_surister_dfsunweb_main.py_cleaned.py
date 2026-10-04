from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
def fonk1():
    b1 = 'D:/geckodriver/geckodriver.exe'
    b2 = webdriver.Firefox(executable_path=b1)
    return b2
def fonk2(b2, date):
    b3 = b2.find_element(By.ID, 'fecha_salida')
    b3.click()
    b3.send_keys(date)
    b3.click()
def fonk3(b2, dropdown_id):
    b4 = WebDriverWait(b2, 10).until(
        EC.presence_of_element_located((By.XPATH, f"
    )
    b5 = b4.find_elements(By.TAG_NAME, 'option')
    for option in b5:
        option.click()
        print(option.get_attribute('value'))
        sleep(1)
def fonk4():
    b2 = fonk1()
    try:
        b2.get("http:
        fonk2(b2, '2019-08-14')
        sleep(1)
        fonk3(b2, 'flight')
        fonk3(b2, 'hoteles')
        sleep(100)
    finally:
        b2.quit()
if b6 = = "__main__":
    fonk4()