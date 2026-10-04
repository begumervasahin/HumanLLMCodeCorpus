from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
import time
from bs4 import BeautifulSoup
b1 = '/Users/abinavrameshsundararaman/Documents/McGill/Courses/Winter 2019/Advanced Info Systems/Group Assignment-2/chromedriver'
b2 = webdriver.Chrome(executable_path= b1)
b2.get("https:
b2.b3 = WebDriverWait(b2, 2)
b2.find_element_by_xpath('
time.sleep(2)
b4 = BeautifulSoup(b2.page_source,"html.parser")
b5 = list()
for i in range(1,4):
   b2.b3 = WebDriverWait(b2, 2)
   b6 = '
   b2.find_element_by_xpath(b6).click()
   time.sleep(2)
   b4 = BeautifulSoup(b2.page_source,"html.parser")
   for div in b4.findAll('div', b7 = {'class':'col-xs-6 col-md-3'}):
       b8 = div.find('ol',b7={'class':'section-col list-unstyled'}).b8
       b5.append(b8)
   for div in b4.findAll('div', b7 = {'class':'col-xs-6 col-md-3 col-md-push-3'}):
       b8 = div.find('ol',b7={'class':'section-col list-unstyled'}).b8
       b5.append(b8)
   for div in b4.findAll('div', b7 = {'class':"col-xs-6 col-md-3 col-md-pull-3"}):
       b8 = div.find('ol',b7={'class':'section-col list-unstyled'}).b8
       b5.append(b8)
len(b5)
b9 = list()
for i in b5 :
    b10 = list()
    b10 = i.split(sep="\n")
    for j in b10 :
        b9.append(j)
b10 = '\nfairness\nfriendly and kind\n'.split(sep="\n")
for i in b10 :
    print(i)
b1 = '/Users/abinavrameshsundararaman/Documents/McGill/Courses/Winter 2019/Advanced Info Systems/Group Assignment-2/chromedriver'
b2 = webdriver.Chrome(executable_path= b1)
b2.get("https:
b2.b3 = WebDriverWait(b2, 2)
b2.find_element_by_xpath('
time.sleep(2)
b4 = BeautifulSoup(b2.page_source,"html.parser")
b2.close()
b11 = list()
for div in b4.findAll('div', b7 = {'class':'words'}):
    for div1 in b4.findAll('span', b7 = {'class':'item'}):
        try :
            b8 = div1.find('span',b7={'class':'word-sub-item'}).b8
            b11.append(b8)
        except :
            continue
len(b11)
b12 = list()
for i in b11 :
    if i.isalpha():
        b12.append(j)