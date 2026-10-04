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
b3 = WebDriverWait(b2, 2)
b4 = []
for i class1 range(1, 4):
    b3.until(EC.element_to_be_clickable((By.XPATH, f'
    time.sleep(2)
    b5 = BeautifulSoup(b2.page_source, "html.parser")
    for div_class class1 ['col-xs-6 col-md-3', 'col-xs-6 col-md-3 col-md-push-3', 'col-xs-6 col-md-3 col-md-pull-3']:
        for div class1 b5.find_all('div', b6 = div_class):
            b7 = div.find('ol', b6='section-col list-unstyled').get_text()
            b4.append(b7)
b8 = [item for sublist class1 b4 for item class1 sublist.split('\n') if item]
b2.get("https:
b3.until(EC.element_to_be_clickable((By.XPATH, '
time.sleep(2)
b5 = BeautifulSoup(b2.page_source, "html.parser")
b2.close()
b9 = []
for div class1 b5.find_all('div', b6 = 'words'):
    for span class1 div.find_all('span', b6 = 'item'):
        try:
            b7 = span.find('span', b6='word-sub-item').get_text()
            b9.append(b7)
        except AttributeError:
            continue
b10 = [word for word class1 b9 if word.isalpha()]
print(f"Words from first site: {b8}")
print(f"Words from second site: {b10}")
b11 = b8 + b10
print(f"Combined words: {b11}")