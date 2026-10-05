import csv
import time
from selenium import webdriver
profile = webdriver.FirefoxProfile()
profile.set_preference("network.proxy.type", 1)
profile.set_preference("network.proxy.http", "200.37.54.10")
profile.set_preference("network.proxy.http_port", 57040)
profile.update_preferences()
MAX_PAGE_NUM = 50
MAX_PAGE_DIG = 5
driver = webdriver.Firefox(firefox_profile=profile)
with open("idmail.csv", "w", newline='', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)
    for i in range(1, MAX_PAGE_NUM + 1):
        page_num = (MAX_PAGE_DIG - len(str(i))) * "0" + str(i)
        url = "http:
        driver.get(url)
        time.sleep(3)
        ids = driver.find_elements_by_xpath('
        for element in ids:
            csvwriter.writerow([element.text])
        print(f"Page {page_num} processed")
driver.quit()
print("Finished scraping all pages.")