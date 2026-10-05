import csv
import time
from selenium import webdriver
firefox_profile = webdriver.FirefoxProfile()
firefox_profile.set_preference("network.proxy.type", 1)
firefox_profile.set_preference("network.proxy.http", "200.37.54.10")
firefox_profile.set_preference("network.proxy.http_port", 57040)
firefox_profile.update_preferences()
MAX_PAGE_NUMBER = 50
MAX_PAGE_DIGITS = 5
driver = webdriver.Firefox(firefox_profile=firefox_profile)
with open("idmail.csv", "w", newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)
    for page_number in range(1, MAX_PAGE_NUMBER + 1):
        page_num_str = (MAX_PAGE_DIGITS - len(str(page_number))) * "0" + str(page_number)
        url = f"http:
        driver.get(url)
        time.sleep(3)
        page_content_elements = driver.find_elements_by_xpath('
        for element in page_content_elements:
            csv_writer.writerow([element.text])
        print(f"Page {page_num_str} processed")
driver.quit()
print("Finished scraping all pages.")