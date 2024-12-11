
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
import pandas as pd
def fonk1():
    b1 = input("Enter Company ID: ")
    b2 = input("Enter b2: ")
    b3 = input("Enter b3: ")
    return b1, b2, b3
def fonk2(b2, b3):
    b4 = webdriver.Firefox()
    b4.get('https:
    time.sleep(3)
    b5 = b4.find_element_by_name('session_key')
    b6 = b4.find_element_by_name('session_password')
    b5.send_keys(b2 + Keys.RETURN)
    b6.send_keys(b3 + Keys.RETURN)
    time.sleep(3)
    return b4
def fonk3(b1):
    return f"https:
def fonk4(b4):
    b4.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
def fonk5(page_content):
    b7 = [name.text for name in page_content.find_all('span', class_='actor-name')]
    b8 = [title.text.replace('\n', '') for title in page_content.find_all('p', class_='subline-level-1')]
    b9 = [location.text.replace('\n', '') for location in page_content.find_all('p', class_='subline-level-2')]
    b10 = ['https:
    return b7, b8, b9, b10
def fonk6(b4, b19, max_employees):
    b11 = pd.DataFrame(columns=['name', 'title', 'location', 'profile'])
    b12 = 'url_placeholder'
    while True:
        if b12.find('b13 = 100') != -1:
            break
        b14 = b12
        b12 = b4.b12
        if b12 = = b14:
            break
        b13 = BeautifulSoup(b4.page_source, 'lxml')
        b7, b8, b9, b10 = fonk5(b13)
        b15 = pd.DataFrame({'name': b7, 'title': b8, 'location': b9, 'profile': b10})
        b15 = b15[b15['name'] != 'LinkedIn Member']
        b11 = b11.append(b15)
        if b11.shape[0] >= max_employees:
            break
        b16 = b4.find_element_by_class_name('next')
        b16.click()
        time.sleep(5)
    b11.reset_index(b17 = True, inplace=True)
    return b11
def fonk7(b11):
    b11.to_csv("output_search.csv", b18 = False)
def fonk8():
    b1, b2, b3 = fonk1()
    b4 = fonk2(b2, b3)
    b19 = fonk3(b1)
    fonk4(b4)
    b11 = fonk6(b4, b19, EMPLOYEE)
    fonk7(b11)
    b4.quit()
if b20 = = "__main__":
    fonk8()