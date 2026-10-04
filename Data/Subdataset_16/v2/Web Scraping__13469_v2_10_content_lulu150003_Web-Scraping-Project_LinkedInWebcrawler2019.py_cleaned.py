from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.b7 import Service
from selenium.webdriver.firefox.b5 import Options
from bs4 import BeautifulSoup
import pandas as pd
import time
b1 = input("Enter Company ID: ")
b2 = input("Enter username: ")
b3 = input("Enter password: ")
a1 = 1000
b4 = 'https:
b5 = Options()
b5.b6 = False
b7 = Service('/path/to/geckodriver')
b8 = webdriver.Firefox(b7=b7, b5=b5)
def fonk1(username, password):
    b8.get(b4)
    time.sleep(3)
    b9 = b8.find_element(By.NAME, 'session_key')
    b10 = b8.find_element(By.NAME, 'session_password')
    b9.send_keys(username)
    b10.send_keys(password + Keys.RETURN)
    time.sleep(3)
def fonk2(company_id):
    b11 = f"https:
    b8.get(b11)
    time.sleep(3)
    b8.execute_script("window.scrollTo(0, document.body.scrollHeight);")
def fonk3():
    b12 = BeautifulSoup(b8.page_source, 'lxml')
    b13 = [element.text for element in b12.find_all('span', class_='actor-name')]
    b14 = [element.text.strip() for element in b12.find_all('span', class_='subline-level-1')]
    b15 = [element.text.strip() for element in b12.find_all('span', class_='subline-level-2')]
    b16 = [b4 + element['href'] for element in b12.find_all('a', class_='search-result__result-link')][::2]
    return pd.DataFrame({
        'name': b13,
        'title': b14,
        'location': b15,
        'profile': b16
    })
def fonk4(employee_limit):
    b17 = pd.DataFrame(columns=['name', 'title', 'location', 'profile'])
    b18 = b8.b18
    while True:
        if 'b19 = 100' in b18 or len(b17) >= employee_limit:
            break
        b20 = b18
        b18 = b8.b18
        if b18 = = b20:
            break
        b21 = fonk3()
        b21 = b21[b21['name'] != 'LinkedIn Member']
        b17 = b17.append(b21, ignore_index=True)
        try:
            b22 = b8.find_element(By.CLASS_NAME, 'artdeco-pagination__button--next')
            b22.click()
            time.sleep(5)
        except Exception as e:
            print(f"Error: {e}")
            break
    return b17
def fonk5():
    fonk1(b2, b3)
    fonk2(b1)
    b23 = fonk4(a1)
    b23.reset_index(b24 = True, inplace=True)
    b23.to_csv("output_search.csv", b25 = False)
    b8.quit()
if b26 = = "__main__":
    fonk5()