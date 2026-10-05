import csv
from selenium import webdriver
import time
PROXY = "5.58.85.32:43214"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=%s' % PROXY)
chrome_options.add_argument('--ignore_certificate-errors')
chrome_options.add_argument('--ignore-ssl-errors')
MAX_PAGE_NUM = 16
MAX_PAGE_DIG = 3
with open("contacts.csv", "w", newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Address", "Phone"])
    driver = webdriver.Chrome(options=chrome_options)
    for i in range(1, MAX_PAGE_NUM + 1):
        page_num = (MAX_PAGE_DIG - len(str(i))) * "0" + str(i)
        url = "https:
        driver.get(url)
        time.sleep(5)
        contacts = driver.find_elements_by_xpath('
        for contact in contacts:
            name = contact.find_element_by_xpath('.
            address = contact.find_element_by_xpath('.
            phone = contact.find_element_by_xpath('.
            writer.writerow([name, address, phone])
    driver.quit()
print("Scraping finished. Data saved to contacts.csv")