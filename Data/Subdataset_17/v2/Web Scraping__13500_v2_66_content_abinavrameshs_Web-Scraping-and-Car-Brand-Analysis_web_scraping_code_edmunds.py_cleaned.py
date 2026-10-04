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
wait = WebDriverWait(driver, 2)
attr_list = []
for i in range(1, 4):
    wait.until(EC.element_to_be_clickable((By.XPATH, f'
    time.sleep(2)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    for div_class in ['col-xs-6 col-md-3', 'col-xs-6 col-md-3 col-md-push-3', 'col-xs-6 col-md-3 col-md-pull-3']:
        for div in soup.find_all('div', class_=div_class):
            text = div.find('ol', class_='section-col list-unstyled').get_text()
            attr_list.append(text)
attr_list_clean = [item for sublist in attr_list for item in sublist.split('\n') if item]
driver.get("https:
wait.until(EC.element_to_be_clickable((By.XPATH, '
time.sleep(2)
soup = BeautifulSoup(driver.page_source, "html.parser")
driver.close()
attr_list2 = []
for div in soup.find_all('div', class_='words'):
    for span in div.find_all('span', class_='item'):
        try:
            text = span.find('span', class_='word-sub-item').get_text()
            attr_list2.append(text)
        except AttributeError:
            continue
attr_list_clean2 = [word for word in attr_list2 if word.isalpha()]
print(f"Words from first site: {attr_list_clean}")
print(f"Words from second site: {attr_list_clean2}")
combined_words = attr_list_clean + attr_list_clean2
print(f"Combined words: {combined_words}")