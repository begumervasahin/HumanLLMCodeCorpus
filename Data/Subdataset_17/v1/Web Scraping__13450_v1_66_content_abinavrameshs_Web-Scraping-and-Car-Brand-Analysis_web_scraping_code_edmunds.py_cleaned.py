from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
from bs4 import BeautifulSoup
driver_path = '/Users/abinavrameshsundararaman/Documents/McGill/Courses/Winter 2019/Advanced Info Systems/Group Assignment-2/chromedriver'
driver = webdriver.Chrome(executable_path=driver_path)
driver.get("https:
driver.wait = WebDriverWait(driver, 2)
attr_list = list()
for i in range(1, 4):
    driver.wait = WebDriverWait(driver, 2)
    xpath_text = f'
    driver.find_element(By.XPATH, xpath_text).click()
    time.sleep(2)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    for div_class in ['col-xs-6 col-md-3', 'col-xs-6 col-md-3 col-md-push-3', 'col-xs-6 col-md-3 col-md-pull-3']:
        for div in soup.findAll('div', class_=div_class):
            text = div.find('ol', class_='section-col list-unstyled').text
            attr_list.append(text)
attr_list2 = [item for sublist in attr_list for item in sublist.split('\n') if item]
driver.get("https:
driver.wait = WebDriverWait(driver, 2)
driver.find_element(By.XPATH, '
time.sleep(2)
soup = BeautifulSoup(driver.page_source, "html.parser")
driver.close()
attr_list3 = []
for div in soup.findAll('div', class_='words'):
    for span in div.findAll('span', class_='item'):
        try:
            text = span.find('span', class_='word-sub-item').text
            attr_list3.append(text)
        except AttributeError:
            continue
attr_list_clean2 = [word for word in attr_list3 if word.isalpha()]
print(f"Words from first site: {attr_list2}")
print(f"Words from second site: {attr_list_clean2}")
combined_words = attr_list2 + attr_list_clean2
print(f"Combined words: {combined_words}")