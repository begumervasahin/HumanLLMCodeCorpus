from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
import time
from bs4 import BeautifulSoup
driver_path = '/Users/abinavrameshsundararaman/Documents/McGill/Courses/Winter 2019/Advanced Info Systems/Group Assignment-2/chromedriver'
driver = webdriver.Chrome(executable_path= driver_path)
driver.get("https:
driver.wait = WebDriverWait(driver, 2)
driver.find_element_by_xpath('
time.sleep(2)
soup_stackoverflow = BeautifulSoup(driver.page_source,"html.parser")
attr_list = list()
for i in range(1,4):
   driver.wait = WebDriverWait(driver, 2)
   xpath_text = '
   driver.find_element_by_xpath(xpath_text).click()
   time.sleep(2)
   soup_stackoverflow = BeautifulSoup(driver.page_source,"html.parser")
   for div in soup_stackoverflow.findAll('div', attrs={'class':'col-xs-6 col-md-3'}):
       text=div.find('ol',attrs={'class':'section-col list-unstyled'}).text
       attr_list.append(text)
   for div in soup_stackoverflow.findAll('div', attrs={'class':'col-xs-6 col-md-3 col-md-push-3'}):
       text=div.find('ol',attrs={'class':'section-col list-unstyled'}).text
       attr_list.append(text)
   for div in soup_stackoverflow.findAll('div', attrs={'class':"col-xs-6 col-md-3 col-md-pull-3"}):
       text=div.find('ol',attrs={'class':'section-col list-unstyled'}).text
       attr_list.append(text)
len(attr_list)
attr_list2 = list()
for i in attr_list :
    lst = list()
    lst=i.split(sep="\n")
    for j in lst :
        attr_list2.append(j)
lst='\nfairness\nfriendly and kind\n'.split(sep="\n")
for i in lst :
    print(i)
driver_path = '/Users/abinavrameshsundararaman/Documents/McGill/Courses/Winter 2019/Advanced Info Systems/Group Assignment-2/chromedriver'
driver = webdriver.Chrome(executable_path= driver_path)
driver.get("https:
driver.wait = WebDriverWait(driver, 2)
driver.find_element_by_xpath('
time.sleep(2)
soup_stackoverflow = BeautifulSoup(driver.page_source,"html.parser")
driver.close()
attr_list3=list()
for div in soup_stackoverflow.findAll('div', attrs={'class':'words'}):
    for div1 in soup_stackoverflow.findAll('span', attrs={'class':'item'}):
        try :
            text=div1.find('span',attrs={'class':'word-sub-item'}).text
            attr_list3.append(text)
        except :
            continue
len(attr_list3)
attr_list_clean2=list()
for i in attr_list3 :
    if i.isalpha():
        attr_list_clean2.append(j)