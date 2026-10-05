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
with open("contacts.csv", "w") as csv_file:
    driver = webdriver.Chrome(options=chrome_options)
    for i in range(1, MAX_PAGE_NUM + 1):
        page_num = (MAX_PAGE_DIG - len(str(i))) * "0" + str(i)
        url = "https:
        driver.get(url)
        time.sleep(10)
        contacts = driver.find_elements_by_xpath('
        num_page_items = len(contacts)
        for j in range(num_page_items):
            csv_file.write(contacts[j].text + "," + "\n")
    driver.close()
print("Finished writing contacts to CSV.")