import csv
import time
from selenium import webdriver
a1 = 50
a2 = 5
a3 = 3
b1 = webdriver.FirefoxProfile()
b1.set_preference("network.proxy.type", 1)
b1.set_preference("network.proxy.http", "200.37.54.10")
b1.set_preference("network.proxy.http_port", 57040)
b1.update_preferences()
b2 = webdriver.Firefox(b1=b1)
with open("idmail.csv", "w", b3 = '', encoding='utf-8') as csvfile:
    b4 = csv.writer(csvfile)
    for page_number in range(1, a1 + 1):
        b5 = str(page_number).zfill(a2)
        b6 = f"http:
        b2.get(b6)
        time.sleep(a3)
        b7 = b2.find_elements_by_xpath('
        for element in b7:
            b4.writerow([element.text])
        print(f"Page {b5} processed")
b2.quit()
print("Finished scraping all pages.")