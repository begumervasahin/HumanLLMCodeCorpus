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
b3 = input("Enter b10: ")
a1 = 1000
b4 = 'https:
b5 = Options()
b5.b6 = False
b7 = Service('/path/to/geckodriver')
b8 = webdriver.Firefox(b7=b7, b5=b5)
b8.get(b4)
time.sleep(3)
b9 = b8.find_element(By.NAME, 'session_key')
b10 = b8.find_element(By.NAME, 'session_password')
b9.send_keys(b2)
b10.send_keys(b3 + Keys.RETURN)
time.sleep(3)
b11 = f"https:
b8.get(b11)
time.sleep(3)
b8.execute_script("window.scrollTo(0, document.body.scrollHeight);")
b12 = pd.DataFrame(columns=['name', 'title', 'location', 'profile'])
b13 = b8.b13
while True:
    if 'b14 = 100' in b13:
        break
    b15 = b13
    b13 = b8.b13
    if b13 = = b15:
        break
    b14 = BeautifulSoup(b8.page_source, 'lxml')
    b16 = b14.find_all('span', class_='actor-name')
    b17 = b14.find_all('span', class_='subline-level-1')
    b18 = b14.find_all('span', class_='subline-level-2')
    b19 = b14.find_all('a', class_='b11-result__result-link')
    b20 = [name.text for name in b16]
    b21 = [title.text.strip() for title in b17]
    b22 = [location.text.strip() for location in b18]
    b23 = [b4 + profile['href'] for profile in b19][::2]
    b24 = pd.DataFrame({'name': b20, 'title': b21, 'location': b22, 'profile': b23})
    b24 = b24[b24['name'] != 'LinkedIn Member']
    b12 = b12.append(b24, ignore_index=True)
    if b12.shape[0] >= a1:
        break
    try:
        b25 = b8.find_element(By.CLASS_NAME, 'artdeco-pagination__button--next')
        b25.click()
        time.sleep(5)
    except:
        break
b12.reset_index(b26 = True, inplace=True)
b12.to_csv("output_search.csv", b27 = False)
b8.quit()