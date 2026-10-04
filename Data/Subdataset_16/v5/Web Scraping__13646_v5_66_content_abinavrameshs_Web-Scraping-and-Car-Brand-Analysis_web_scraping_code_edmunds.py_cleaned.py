from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
from bs4 import BeautifulSoup
b1 = '/Users/abinavrameshsundararaman/Documents/McGill/Courses/Winter 2019/Advanced Info Systems/Group Assignment-2/chromedriver'
b2 = webdriver.Chrome(executable_path=b1)
def fonk1(url, xpath_pattern):
    b2.get(url)
    b2.b3 = WebDriverWait(b2, 2)
    b4 = []
    for i in range(1, 4):
        b5 = xpath_pattern.format(i)
        b2.find_element_by_xpath(b5).click()
        time.sleep(2)
        b6 = BeautifulSoup(b2.page_source, "html.parser")
        for div in b6.find_all('div', b7 = ['col-xs-6 col-md-3', 'col-xs-6 col-md-3 col-md-push-3', 'col-xs-6 col-md-3 col-md-pull-3']):
            b8 = div.find('ol', b7='section-col list-unstyled').b8
            b4.append(b8)
    return b4
b9 = "https:
b10 = '
b4 = fonk1(b9, b10)
b11 = [item for sublist in [b8.split("\n") for b8 in b4] for item in sublist]
b12 = ['fairness', 'friendly and kind']
for item in b12:
    print(item)
b13 = "https:
b2.get(b13)
b2.b3 = WebDriverWait(b2, 2)
b2.find_element_by_xpath('
time.sleep(2)
b6 = BeautifulSoup(b2.page_source, "html.parser")
b2.close()
b14 = [span.b8 for span in b6.find_all('span', b7='item')]
b15 = [b8 for b8 in b14 if b8.isalpha()]
print(len(b11))
print(len(b15))
b2.quit()