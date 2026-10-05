import os
import csv
import re
import time
from selenium import webdriver
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
profile = FirefoxProfile()
profile.set_preference("network.proxy.type", 1)
profile.set_preference("network.proxy.http", "200.37.54.10")
profile.set_preference("network.proxy.http_port", 57040)
profile.update_preferences()
MAX_PAGE_NUM = 50
MAX_PAGE_DIG = 5
driver = webdriver.Firefox(firefox_profile=profile)
for i in range(1, MAX_PAGE_NUM + 1):
    page_num = str(i).zfill(MAX_PAGE_DIG)
    url = f"http:
    driver.get(url)
    ids = driver.find_elements_by_xpath('
    num_page_items = len(ids)
    with open("idmail.csv", "w") as f:
        for item in ids:
            f.write(item.text + "\n")
            time.sleep(1)
    driver.close()
    print("Finished scraping page", i)
print("All pages scraped successfully.")