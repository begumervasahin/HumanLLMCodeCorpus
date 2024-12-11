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
def fonk1(contact):
    b4 = contact.find_element_by_css_selector('.denomination-links.pj-lb.pj-link').text
    b5 = contact.find_element_by_css_selector('.adresse.pj-lb.pj-link').text
    b6 = contact.find_element_by_css_selector('.num').text
    return b4, b5, b6
with open("b12.csv", "w", b7 = '', encoding='utf-8') as csv_file:
    b8 = csv.writer(csv_file)
    b8.writerow(["Name", "Address", "Phone"])
    with webdriver.Chrome(b9 = b2) as driver:
        for page_num in range(1, a1 + 1):
            b10 = str(page_num).zfill(a2)
            b11 = f"https:
            driver.get(b11)
            time.sleep(5)
            b12 = driver.find_elements_by_css_selector('li.bi-bloc.blocs')
            for contact in b12:
                b4, b5, b6 = fonk1(contact)
                b8.writerow([b4, b5, b6])
print("Scraping finished. Data saved to b12.csv")