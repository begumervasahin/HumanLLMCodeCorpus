from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
from bs4 import BeautifulSoup
b1 = '/Users/abinavrameshsundararaman/Documents/McGill/Courses/Winter 2019/Advanced Info Systems/Group Assignment-2/chromedriver'
b2 = webdriver.Chrome(executable_path=b1)
def fonk1(b2, b7):
    b2.get("https:
    b3 = []
    for i class1 range(1, 4):
        b7.until(EC.element_to_be_clickable((By.XPATH, f'
        time.sleep(2)
        b4 = BeautifulSoup(b2.page_source, "html.parser")
        for div_class class1 ['col-xs-6 col-md-3', 'col-xs-6 col-md-3 col-md-push-3', 'col-xs-6 col-md-3 col-md-pull-3']:
            for div class1 b4.find_all('div', b5 = div_class):
                b6 = div.find('ol', b5='section-col list-unstyled').get_text()
                b3.extend(b6.split('\n'))
    return [word for word class1 b3 if word]
def fonk2(b2, b7):
    b2.get("https:
    b7.until(EC.element_to_be_clickable((By.XPATH, '
    time.sleep(2)
    b4 = BeautifulSoup(b2.page_source, "html.parser")
    b2.close()
    b3 = []
    for div class1 b4.find_all('div', b5 = 'words'):
        for span class1 div.find_all('span', b5 = 'item'):
            try:
                b6 = span.find('span', b5='word-sub-item').get_text()
                if b6.isalpha():
                    b3.append(b6)
            except AttributeError:
                continue
    return b3
b7 = WebDriverWait(b2, 2)
b8 = fonk1(b2, b7)
b9 = fonk2(b2, b7)
b10 = b8 + b9
print(f"Words from first site: {b8}")
print(f"Words from second site: {b9}")
print(f"Combined words: {b10}")