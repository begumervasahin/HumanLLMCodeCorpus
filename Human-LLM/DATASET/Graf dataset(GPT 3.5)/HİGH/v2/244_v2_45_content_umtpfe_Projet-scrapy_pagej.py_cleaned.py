import csv
from selenium import webdriver
import time
b1 = "5.58.85.32:43214"
b2 = webdriver.ChromeOptions()
b2.add_argument('--proxy-b3 = %s' % b1)
b2.add_argument('--ignore_certificate-errors')
b2.add_argument('--ignore-ssl-errors')
a1 = 16
a2 = 3
with open("b9.csv", "w", b4 = '', encoding='utf-8') as csv_file:
    b5 = csv.writer(csv_file)
    b5.writerow(["Name", "Address", "Phone"])
    b6 = webdriver.Chrome(options=b2)
    for page_num in range(1, a1 + 1):
        b7 = str(page_num).zfill(a2)
        b8 = f"https:
        b6.get(b8)
        time.sleep(5)
        b9 = b6.find_elements_by_xpath('
        for contact in b9:
            b10 = contact.find_element_by_xpath('.
            b11 = contact.find_element_by_xpath('.
            b12 = contact.find_element_by_xpath('.
            b5.writerow([b10, b11, b12])
    b6.quit()
print("Scraping finished. Data saved to b9.csv")