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
def get_contact_info(contact):
    name = contact.find_element_by_css_selector('.denomination-links.pj-lb.pj-link').text
    address = contact.find_element_by_css_selector('.adresse.pj-lb.pj-link').text
    phone = contact.find_element_by_css_selector('.num').text
    return name, address, phone
with open("contacts.csv", "w", newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["Name", "Address", "Phone"])
    with webdriver.Chrome(options=chrome_options) as driver:
        for page_num in range(1, MAX_PAGE_NUM + 1):
            formatted_page_num = str(page_num).zfill(MAX_PAGE_DIG)
            url = f"https:
            driver.get(url)
            time.sleep(5)
            contacts = driver.find_elements_by_css_selector('li.bi-bloc.blocs')
            for contact in contacts:
                name, address, phone = get_contact_info(contact)
                csv_writer.writerow([name, address, phone])
print("Scraping finished. Data saved to contacts.csv")