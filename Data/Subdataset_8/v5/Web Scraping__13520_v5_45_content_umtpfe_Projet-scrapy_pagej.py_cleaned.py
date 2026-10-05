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
CSV_FILENAME = "contacts.csv"
PAGE_LOAD_DELAY = 10
def construct_page_url(page_num):
    return f"https:
with open(CSV_FILENAME, "w") as csv_file:
    driver = webdriver.Chrome(options=chrome_options)
    for page_num in range(1, MAX_PAGE_NUM + 1):
        formatted_page_num = f"{page_num:03}"
        url = construct_page_url(formatted_page_num)
        driver.get(url)
        time.sleep(PAGE_LOAD_DELAY)
        contacts = driver.find_elements_by_xpath('
        for contact in contacts:
            csv_file.write(contact.text + ",\n")
    driver.close()
print("Finished writing contacts to CSV.")