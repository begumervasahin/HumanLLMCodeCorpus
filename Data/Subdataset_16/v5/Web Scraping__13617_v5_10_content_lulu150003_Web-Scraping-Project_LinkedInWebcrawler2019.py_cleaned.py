from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
from bs4 import BeautifulSoup
import pandas as pd
def fonk1():
    b1 = webdriver.Firefox()
    b1.get('https:
    time.sleep(3)
    return b1
def fonk2(b1, b12, b13):
    b2 = b1.find_element_by_name('session_key')
    b3 = b1.find_element_by_name('session_password')
    b2.send_keys(b12 + Keys.RETURN)
    b3.send_keys(b13 + Keys.RETURN)
    time.sleep(3)
def fonk3(b1, b11):
    b4 = f"https:
    b1.get(b4)
    time.sleep(3)
    b1.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
def fonk4(b1, b14):
    b5 = BeautifulSoup(b1.page_source, 'lxml')
    b6 = [name.text for name in b5.find_all('span', class_='actor-name')]
    b7 = [title.text.strip() for title in b5.find_all('p', class_='subline-level-1')]
    b8 = [location.text.strip() for location in b5.find_all('p', class_='subline-level-2')]
    b9 = [b14 + profile['href'] for profile in b5.find_all('a', class_='search-result__result-link')[::2]]
    b10 = {
        'name': b6,
        'title': b7,
        'location': b8,
        'profile': b9
    }
    return pd.DataFrame(b10)
def fonk5():
    b11 = input("Enter Company ID: ")
    b12 = input("Enter b12: ")
    b13 = input("Enter b13: ")
    a1 = 1000
    b14 = 'https:
    b1 = fonk1()
    fonk2(b1, b12, b13)
    fonk3(b1, b11)
    b15 = pd.DataFrame(columns=['name', 'title', 'location', 'profile'])
    b16 = 'url_placeholder'
    while True:
        if 'b5 = 100' in b16:
            break
        b17 = b16
        b16 = b1.b16
        if b16 = = b17:
            break
        b18 = fonk4(b1, b14)
        b18 = b18[b18['name'] != 'LinkedIn Member']
        b15 = b15.append(b18, ignore_index=True)
        if b15.shape[0] >= a1:
            break
        try:
            b19 = b1.find_element_by_class_name('next')
            b19.click()
        except NoSuchElementException:
            print("No more pages or navigation error.")
            break
        time.sleep(5)
    b15.reset_index(b20 = True, inplace=True)
    b15.to_csv("output_search.csv", b21 = False)
    b1.quit()
if b22 = = "__main__":
    fonk5()