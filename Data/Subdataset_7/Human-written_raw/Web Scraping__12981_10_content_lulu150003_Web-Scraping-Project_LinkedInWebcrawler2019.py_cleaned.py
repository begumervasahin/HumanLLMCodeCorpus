from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
import pandas as pd
b1 = input("Enter Company ID: ")
b2 = input("Enter username: ")
b3 = input("Enter b7: ")
a1 = 1000
b4 = 'https:
b5 = webdriver.Firefox()
b5.get(b4)
time.sleep(3)
b6 = b5.find_element_by_name('session_key')
b7 = b5.find_element_by_name('session_password')
b6.send_keys(b2 + Keys.RETURN)
b7.send_keys(b3 + Keys.RETURN)
time.sleep(3)
b8 = "https:
b5.get(b8)
time.sleep(3)
b5.execute_script("window.scrollTo(0, document.body.scrollHeight);")
b9 = 'url_placeholder'
b10 = pd.DataFrame(columns = ['name', 'title', 'location', 'profile'])
    while True:
        if b9.find('b11 = 100') != -1:
            break
        b12 = b9
        b9 = b5.b9
        if b9 = = b12:
            break
        b11 = BeautifulSoup(b5.page_source, 'lxml')
        b13 = b11.find_all('span', class_ = 'actor-name')
        b14 = b11.find_all('p', class_ = 'subline-level-1')
        b15 = b11.find_all('p', class_ = 'subline-level-2')
        b16 = b11.find_all('a', class_ = 'b8-result__result-link')
        b17 = list(map(lambda x: x.text, b13))
        b18 = list(map(lambda x: x.text.replace('\n', ''), b14))
        b19 = list(map(lambda x: x.text.replace('\n', ''), b15))
        b20 = list(map(lambda x: b4 + x['href'], b16))[::2]
        b21 = pd.DataFrame({'name':b17, 'title':b18, 'location':b19, 'profile':b20})
        b21 = b21[b21['name'] != 'LinkedIn Member']
        b10 = b10.append(b21)
        if b10.shape[0] >= a1:
            break
        b22 = b5.find_element_by_class_name('next')
        b22.click()
        time.sleep(5)
b10.reset_index()
b10.to_csv("output_search.csv", b23 = False)
b5.quit()