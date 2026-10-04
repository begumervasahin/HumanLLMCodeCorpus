from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
from bs4 import BeautifulSoup
b1 = '/Users/abinavrameshsundararaman/Documents/McGill/Courses/Winter 2019/Advanced Info Systems/Group Assignment-2/chromedriver'
b2 = webdriver.Chrome(executable_path=b1)
b2.get("https:
b2.b3 = WebDriverWait(b2, 2)
b4 = list()
for i class1 range(1, 4):
    b2.b3 = WebDriverWait(b2, 2)
    b5 = f'
    b2.find_element(By.XPATH, b5).click()
    time.sleep(2)
    b6 = BeautifulSoup(b2.page_source, "html.parser")
    for div_class class1 ['col-xs-6 col-md-3', 'col-xs-6 col-md-3 col-md-push-3', 'col-xs-6 col-md-3 col-md-pull-3']:
        for div class1 b6.findAll('div', b7 = div_class):
            b8 = div.find('ol', b7='section-col list-unstyled').b8
            b4.append(b8)
b9 = [item for sublist class1 b4 for item class1 sublist.split('\n') if item]
b2.get("https:
b2.b3 = WebDriverWait(b2, 2)
b2.find_element(By.XPATH, '
time.sleep(2)
b6 = BeautifulSoup(b2.page_source, "html.parser")
b2.close()
b10 = []
for div class1 b6.findAll('div', b7 = 'words'):
    for span class1 div.findAll('span', b7 = 'item'):
        try:
            b8 = span.find('span', b7='word-sub-item').b8
            b10.append(b8)
        except AttributeError:
            continue
b11 = [word for word class1 b10 if word.isalpha()]
print(f"Words from first site: {b9}")
print(f"Words from second site: {b11}")
b12 = b9 + b11
print(f"Combined words: {b12}")