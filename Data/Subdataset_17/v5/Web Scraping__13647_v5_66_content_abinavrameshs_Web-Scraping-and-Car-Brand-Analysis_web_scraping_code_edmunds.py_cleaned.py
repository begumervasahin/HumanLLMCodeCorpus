from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
from bs4 import BeautifulSoup
driver_path = '/Users/abinavrameshsundararaman/Documents/McGill/Courses/Winter 2019/Advanced Info Systems/Group Assignment-2/chromedriver'
driver = webdriver.Chrome(executable_path=driver_path)
def extract_text_from_website(url, xpath_pattern):
    driver.get(url)
    driver.wait = WebDriverWait(driver, 2)
    attr_list = []
    for i in range(1, 4):
        xpath_text = xpath_pattern.format(i)
        driver.find_element_by_xpath(xpath_text).click()
        time.sleep(2)
        soup = BeautifulSoup(driver.page_source, "html.parser")
        for div in soup.find_all('div', class_=['col-xs-6 col-md-3', 'col-xs-6 col-md-3 col-md-push-3', 'col-xs-6 col-md-3 col-md-pull-3']):
            text = div.find('ol', class_='section-col list-unstyled').text
            attr_list.append(text)
    return attr_list
url1 = "https:
xpath_pattern1 = '
attr_list = extract_text_from_website(url1, xpath_pattern1)
attr_list2 = [item for sublist in [text.split("\n") for text in attr_list] for item in sublist]
sample_list = ['fairness', 'friendly and kind']
for item in sample_list:
    print(item)
url2 = "https:
driver.get(url2)
driver.wait = WebDriverWait(driver, 2)
driver.find_element_by_xpath('
time.sleep(2)
soup = BeautifulSoup(driver.page_source, "html.parser")
driver.close()
attr_list3 = [span.text for span in soup.find_all('span', class_='item')]
attr_list_clean2 = [text for text in attr_list3 if text.isalpha()]
print(len(attr_list2))
print(len(attr_list_clean2))
driver.quit()