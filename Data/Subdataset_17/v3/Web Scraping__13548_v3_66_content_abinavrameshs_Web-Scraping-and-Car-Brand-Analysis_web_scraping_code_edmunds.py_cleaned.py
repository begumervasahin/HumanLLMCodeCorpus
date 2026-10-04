from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
from bs4 import BeautifulSoup
driver_path = '/Users/abinavrameshsundararaman/Documents/McGill/Courses/Winter 2019/Advanced Info Systems/Group Assignment-2/chromedriver'
driver = webdriver.Chrome(executable_path=driver_path)
def scrape_words_to_use(driver, wait):
    driver.get("https:
    words_list = []
    for i in range(1, 4):
        wait.until(EC.element_to_be_clickable((By.XPATH, f'
        time.sleep(2)
        soup = BeautifulSoup(driver.page_source, "html.parser")
        for div_class in ['col-xs-6 col-md-3', 'col-xs-6 col-md-3 col-md-push-3', 'col-xs-6 col-md-3 col-md-pull-3']:
            for div in soup.find_all('div', class_=div_class):
                text = div.find('ol', class_='section-col list-unstyled').get_text()
                words_list.extend(text.split('\n'))
    return [word for word in words_list if word]
def scrape_describing_words(driver, wait):
    driver.get("https:
    wait.until(EC.element_to_be_clickable((By.XPATH, '
    time.sleep(2)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    driver.close()
    words_list = []
    for div in soup.find_all('div', class_='words'):
        for span in div.find_all('span', class_='item'):
            try:
                text = span.find('span', class_='word-sub-item').get_text()
                if text.isalpha():
                    words_list.append(text)
            except AttributeError:
                continue
    return words_list
wait = WebDriverWait(driver, 2)
words_from_first_site = scrape_words_to_use(driver, wait)
words_from_second_site = scrape_describing_words(driver, wait)
combined_words = words_from_first_site + words_from_second_site
print(f"Words from first site: {words_from_first_site}")
print(f"Words from second site: {words_from_second_site}")
print(f"Combined words: {combined_words}")