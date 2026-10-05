import os
import csv
import re
import time
from selenium import webdriver
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
b1 = FirefoxProfile()
b1.set_preference("network.proxy.type", 1)
b1.set_preference("network.proxy.http", "200.37.54.10")
b1.set_preference("network.proxy.http_port", 57040)
b1.update_preferences()
a1 = 50
a2 = 5
b2 = webdriver.Firefox(firefox_profile=b1)
for i in range(1, a1 + 1):
    b3 = str(i).zfill(a2)
    b4 = f"http:
    b2.get(b4)
    b5 = b2.find_elements_by_xpath('
    b6 = len(b5)
    with open("idmail.csv", "w") as f:
        for item in b5:
            f.write(item.text + "\n")
            time.sleep(1)
    b2.close()
    print("Finished scraping page", i)
print("All pages scraped successfully.")